
function randomInteger(range){
    return Math.floor(Math.random() * range);
}



function sampleEvenly(probabilities){
    var total = 0;
    var position = Math.random() * sum(probabilities);

    for (var i=0; i< probabilities.length; i++){
        total += probabilities[i];

        if (position < total){
            return i;
        }

    }
}

function sum(numberList) {
    var total = 0;
    for (var i =0; i<numberList.length; i++){
        total += numberList[i];
    }
    return total;
}
