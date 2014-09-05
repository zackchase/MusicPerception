
var leftScale = 6;
var centerScale = 0;
var rightScale = 0;
var numCorrect = 0;
var numTotal = 0;
var surveyData;


comparisonList = generateComparisons(10);

// comparisonList = [

//     [2,2,1, "left"],
//     [3,3,2, "left"],
//     [1,1,3, "left"],
//     [4,1,1, "right"],
//     [4,4,2, "left"],
//     [3,4,4, "right"],
//     [3,0,0,"right"],
//     [0,1,1, "right"],
//     [4,4,0, "left"],
//     [2,0,0, "right"],


// ];

// var questionTimes = Array.apply(null, new Array(comparisonList.length)).map(Number.prototype.valueOf,0);
var startTime;
var finishTime;
// var score = [];
// var clicks = zeros([comparisonList.length, 3])

// for (var i = 0; i<comparisonList.length; i++){
//     score.push("blank");
// }

function Rectangle(x,y,w,h,ctx,fill,highlight,scale){

    this.x = x||0;
    this.y = y||0;
    this.w = w||1;
    this.h = h||1;
    this.active = false;
    this.currentScale = 0;
    this.scale = scale || 0;
    this.ctx = ctx;
    this.fill = fill || "#AAAAAA";
    this.highlight = highlight || "#AAAAAA";
    this.clicks = 0;
}

Rectangle.prototype.draw = function(){

    if (this.active){
        this.ctx.fillStyle = this.highlight;
        this.ctx.fillRect(this.x ,this.y ,this.w, this.h);
        this.ctx.lineWidth = 10;
        ctx.strokeStyle = "#75E6FF";
        this.ctx.strokeRect(this.x +5 ,this.y +5,this.w -10, this.h-10);
    }
    else {
        console.log("drawing");
        this.ctx.fillStyle = this.fill;
        this.ctx.fillRect(this.x ,this.y ,this.w, this.h);
    }
}


Rectangle.prototype.trigger = function(){

    if (this.active == true){
        deactivateAll(shapes);

    }
    else {
        deactivateAll(shapes);
        this.activate();
    }
}




Rectangle.prototype.activate = function() {

    this.clicks += 1;
    console.log("activating: ");
    console.log("starting scale #: " + this.scale)
    chosenRaga = pentatonicRagaCodes[this.scale].scale;
    console.log("attempting to call startScale();")
    beginScale(currentIntervalID);
    this.active = true;
    this.draw();
    console.log(this);

}

Rectangle.prototype.deactivate = function(){
    console.log("deactivating: ");
    console.log(this);
    if (this.active == true){
        stopScale();
    }
    this.active = false;
    this.draw();

}

function Arrow(x,y,w,h,ctx,direction,fill){
    this.x = x||0;
    this.y = y||0;
    this.w = w||1;
    this.h = h||1;
    this.direction = direction;
    this.ctx = ctx;
    this.fill = fill || "#AAAAAA";
}

Arrow.prototype.draw = function(){
    this.ctx.fillStyle = this.fill;

    this.ctx.beginPath();
    if (this.direction == "left"){
        this.ctx.moveTo(this.x,this.y+this.h/2);
        this.ctx.lineTo(this.x + this.w, this.y);
        this.ctx.lineTo(this.x+this.w,this.y + this.h);
        this.ctx.fill();
    }
    else if (this.direction =="right"){
        this.ctx.moveTo(this.x,this.y);
        this.ctx.lineTo(this.x, this.y + this.h);
        this.ctx.lineTo(this.x+this.w,this.y + this.h/2);
        this.ctx.fill();
    }
}

Arrow.prototype.activate = function(){
    console.log(this);
}

Arrow.prototype.deactivate = function(){

}

Arrow.prototype.trigger = function(){

    finishTime = new Date().getTime();
    comparisonList[numTotal].timeSpent = finishTime - startTime;
    comparisonList[numTotal].clicksLeft = leftRectangle.clicks;
    comparisonList[numTotal].clicksCenter = centerRectangle.clicks;
    comparisonList[numTotal].clicksRight = rightRectangle.clicks;

    numTotal += 1;

    console.log("arrow triggered: deactivating all controls and registering guess");
    deactivateAll(shapes);

    // define this function to use API: registerGuess("direction");



    if (this.direction == comparisonList[numTotal-1].rightDirection){
        numCorrect += 1;
        console.log("made it to modal call (success)");
        $("#successModal").modal();
        comparisonList[numTotal-1].answerCorrect = true;

    }
    else {
        console.log("made it to modal call (fail)")
        $("#failModal").modal();
        comparisonList[numTotal-1].answerCorrect = false;
    }

    if (numTotal >= comparisonList.length){
        //End the game
        $("#surveyModal").modal();
    }

    $("#scorePanel").html("<h1>Score: " + numCorrect + "/" + numTotal + "</h1>");

    //register result with server
    $.ajax({
        type:"POST",
        url:"http://127.0.0.1:8000/post_comparison/",
        data: comparisonList[numTotal-1],

        success: function(){
            console.log("Success - registered comparison result with server")
        }
    });


    loadNextQuestion();
    updateProgress();

}


var canvas = document.getElementById("canvas");

if (canvas.getContext){
    var ctx = canvas.getContext("2d");
    var height = canvas.height;
    var width = canvas.width;

    var leftRectangle = new Rectangle(50,125,200,200, ctx, "rgb(100,35,100)", "rgb(230,81,230)", leftScale);
    var centerRectangle = new Rectangle (320,45,360,360, ctx, "rgb(35,100,103)", "rgb(81,230,230)", centerScale);
    var rightRectangle = new Rectangle(750,125,200,200, ctx, "rgb(100,100,35)","rgb(230,230,81)", rightScale);
    var leftArrow = new Arrow(260,175, 50, 100, ctx, "left", "rgb(0,0,0)");
    var rightArrow = new Arrow(690, 175, 50, 100, ctx, "right", "rgb(0,0,0)");

    shapes = [leftRectangle, centerRectangle, rightRectangle, leftArrow, rightArrow];
    drawShapes(shapes);


}

function drawShapes(shapes) {
    shapes.forEach(function(shape){
        shape.draw();
    });
}

$(canvas).mousedown(function myDown(e) {
  var position = $(canvas).position();
  var mouseX = e.pageX-position.left;
  var mouseY = e.pageY-position.top;

  console.log("Event: x,y = " + mouseX+","+mouseY);

  shapes.forEach(function(shape){

        if ((shape.x <= mouseX && mouseX <= (shape.x + shape.w)) && (shape.y<= mouseY && mouseY <= shape.y + shape.h)) {
            shape.trigger();
        }
    });

});

function deactivateAll(shapes){
    shapes.forEach(function(shape){
        shape.deactivate();
    });
}


function loadNextQuestion(){

    console.log("loading next question");

    if (numTotal < comparisonList.length){
        leftRectangle.scale = comparisonList[numTotal].leftScale;
        centerRectangle.scale = comparisonList[numTotal].centerScale;
        rightRectangle.scale = comparisonList[numTotal].rightScale;
        correctArrow = comparisonList[numTotal].correctDirection;
    }

    newColors = permutation(colors.length, 3);
    leftRectangle.fill = colors[newColors[0]][0];
    leftRectangle.highlight = colors[newColors[0]][1];
    centerRectangle.fill = colors[newColors[1]][0];
    centerRectangle.highlight = colors[newColors[1]][1];
    rightRectangle.fill = colors[newColors[2]][0];
    rightRectangle.highlight = colors[newColors[2]][1];


    deactivateAll(shapes);

    startTime = new Date().getTime();
    leftRectangle.clicks = centerRectangle.clicks = rightRectangle.clicks = 0;

    if(numTotal == comparisonList.length){
        $(".nextButton").html("Finish by completing our survey");
    }

}

loadNextQuestion();


var progCanvas = document.getElementById("progCanvas");

if (progCanvas.getContext){
    var progCtx = progCanvas.getContext("2d");
    var progHeight = progCanvas.height;
    var progWidth = progCanvas.width;

    var progIncrement = progWidth / comparisonList.length;


}

function updateProgress(){
    var x, y, w, h;
    for(var i=0; i< comparisonList.length; i++){
        x = progIncrement * i;
        y = 0;

        console.log("made it to the loop in update progress. Filling: " + comparisonList[i] )

        if (comparisonList[i].answerCorrect == null){
            console.log("made it to the blank fill")
            progCtx.fillStyle = "rgb(200,200,200)";
            progCtx.fillRect(x, y ,progIncrement, progHeight);
            progCtx.lineWidth = 1;
            progCtx.strokeStyle = "#ffffff";
            progCtx.strokeRect(x + 1 ,y + 1, progIncrement -2, progHeight -2);
        }

        else if (comparisonList[i].answerCorrect ){
            console.log("made it to the right fill")
            progCtx.fillStyle = "#3071a9";
            progCtx.fillRect(x, y ,progIncrement, progHeight);
            progCtx.lineWidth = 1;
            progCtx.strokeStyle = "#ffffff";
            progCtx.strokeRect(x + 1 ,y + 1, progIncrement -2, progHeight -2);
        }

        else if (comparisonList[i].answerCorrect == 0){
            console.log("made it to the right fill")
            progCtx.fillStyle = "#c9302c";
            progCtx.fillRect(x, y ,progIncrement, progHeight);
            progCtx.lineWidth = 1;
            progCtx.strokeStyle = "#ffffff";
            progCtx.strokeRect(x + 1 ,y + 1, progIncrement -2, progHeight -2);
        }


    }
}

updateProgress();


// Send results to the server
$("#submitSurvey").click(function(e){
    e.preventDefault();


    // capture survey information
    // capture scores
    // bundle it all into one JSON object
    // pass to server
    $("#surveyModal").hide();
    var age = $("#surveyAge").val();
    var nationality = $("#surveyNationality").val();
    var handedness = $("#surveyHandedness").val();
    var lessons = $("#surveyLessons").val();
    var sing = $("#surveySing").val();
    var styles = $("#surveyStyle").val();
    var email = $("#surveyEmail").val();

    surveyData = {
        "age": age,
        "nationality": nationality,
        "handedness": handedness,
        "lessons": lessons,
        "sing": sing,
        "email": email,

    }

    console.log("surveyData: " + surveyData);

    $.ajax({
        type:"POST",
        url:"http://127.0.0.1:8000/post_survey/",
        data: surveyData,

        success: function(){
            $("#completeModal").modal();
        }
    });

});


