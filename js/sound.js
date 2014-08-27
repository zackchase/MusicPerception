
var audioCtx = new (window.AudioContext || window.webkitAudioContext)(); // define audio context
var gainNode = audioCtx.createGain();

var justIntonation = false;


gainNode.connect(audioCtx.destination);



var base = 220;
var r = Math.pow(2, 1/12);



function justPitch (base, step) {

    while( step >= 12){
        base = base * 2;
        step -= 12;
    }
    return base * justLookup[step];

}


justLookup = {
    0:1,
    1:16/15,
    2:9/8,
    3:6/5,
    4:5/4,
    5:4/3,
    6:7/5,
    7:3/2,
    8:8/5,
    9:5/3,
    10:7/4,
    11:15/8,
}

var pentatonicRagaCodes = [

    {index: 0, name: "HamsaDvani", scale: [0,2,4,7,11]},
    {index: 1, name: "Major", scale: [0,2,4,7,9]},
    {index: 2, name: "Minor", scale: [0,3,5,7,10]},
    {index: 3, name: "Raga Bhupali Todi", scale: [0,1,3,7,8]},
    {index: 4, name: "Raga Kalvati", scale: [0,4,7,9,10]},
    {index: 5, name: "Raga Madhuvanti", scale: [0,3,6,7,11]},
    {index: 6, name: "Raga Marwa Vibhas", scale: [0,1,4,7,9]},
    {index: 7, name: "Raga Gunkali", scale: [0,1,5,7,8]},

];

var chosenRaga = pentatonicRagaCodes[1].scale;
            var scale = 0;

function ragaStepToPitch(step, base){
    //console.log("ragasteptopitchcalled! step: " + step + " base: " + base);
    var local_base = base;
    var local_step = step
    while (local_step >= 5) {
        local_base *= 2;
        local_step -= 5;

    }
    return stepToPitch(chosenRaga[local_step], local_base);
}


function stepToPitch (step, base){

    if (justIntonation){
        pitch = justPitch(base,step);
        console.log("Step: " + step + ", Base: " + base + ", Pitch: " + pitch);


    }
    else {
        pitch = base * Math.pow(r, step);
        console.log("Step: " + step + ", Base: " + base + ", Pitch: " + pitch);
    }
    return pitch;

}


// Set the method of producing scale tones
var mode = 6;

var toggle = true;
var range = 15;
var step = Math.floor(Math.random() * range);
gainNode.gain.value = .5;
var interval = 175;

var duration = .92 * interval;
var lastStep = 0;

var currentIntervalID;



function beginScale(){
    console.log("startScale() called: ");
    currentIntervalID = setInterval(changePitch, interval);
}

//startScale();
function stopScale(){
    console.log("stopScale called");
    clearInterval(currentIntervalID);
}


var scaleOn = true;

$("#pauseButton").click(function(){
    clearInterval(currentIntervalID);
});


function oscillatorToggle (){

    if (oscillatorOn) {
        clearInterval(currentIntervalID);
    }
    else {
        currentIntervalID = setInterval(changePitch, interval);

    }
    oscillatorOn = !oscillatorOn;
};



function nextNote(freq, duration){
    var newOsc = audioCtx.createOscillator()    ;
    newOsc.connect(gainNode);
    newOsc.type = "square";
    newOsc.frequency.value = freq;
    newOsc.start();



    setTimeout(function(){
        newOsc.stop();
        delete newOsc;
    }, duration );

}



