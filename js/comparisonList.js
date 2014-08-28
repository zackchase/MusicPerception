function generateComparisons(numberOfComparisons){

    // pick left scale
    // pick right scale
    // flip coin to pick center scale
    // set value of correct scale ("right" or "left")
    //

    var comparisonList = [];

    for (var i = 0; i < numberOfComparisons; i++){

        var leftScale, centerScale, rightScale, correctDirection;

        // pick left scale
        leftScale = Math.floor(Math.random() * pentatonicRagaCodes.length);
        rightScale = Math.floor(Math.random() * (pentatonicRagaCodes.length-1));
        if (rightScale == leftScale){
            rightScale = pentatonicRagaCodes.length - 1;
        }
        // pick right scale
        // flip coin to pick center scale
        if (Math.random() > .5){
            centerScale = leftScale;
            correctDirection = "left";
        }
        else {
            centerScale = rightScale;
            correctDirection = "right";
        }

        // set value of correct scale ("right" or "left")
        //


        var oneComparison = {
            "leftScale": leftScale,
            "centerScale": centerScale,
            "rightScale": rightScale,
            "rightDirection": correctDirection,   // "left" or "right"
            "answerCorrect": null, // "right" or "wrong" ---- or should it be {0,1}?
            "timeSpent": 0, // amount of time spent (in milliseconds)
            "interval": interval,  // length of each note in milliseconds
            "justIntonation": justIntonation, // true of false
            "mode": mode,   // system used to choose notes
            "clicks_left": 0,
            "clicks_center": 0,
            "clicks_right": 0,
        }

        comparisonList.push(oneComparison);
    }
    return comparisonList;
}
