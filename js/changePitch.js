function changePitch(){

    switch (mode){
        case 0: {
            // toggle between two notes
            if  (toggle){
                nextNote(440, duration);
            }
            else {
                nextNote(660, duration);

            }
            toggle = !toggle
            break;

        }
        case 1: {
        // Walk up scale repeatedly
            step = (step+1) % range;
            nextNote(ragaStepToPitch(step, base), duration);
            break;

        }

        case 2: {
        // Walk up and down
            if (toggle){
                if (step < range-1) {
                    step += 1;
                    console.log("stepped up");
                }

                else {
                    toggle = false;
                    step--;
                }
            }
            else{
                if (step > 0) {
                    step--;
                }
                else {
                    toggle = true;
                    step++;
                }
            }
            nextNote(ragaStepToPitch(step,base), duration);
            break;

        }

        case 3:{
        //  oscillator to random raga step
            nextNote(ragaStepToPitch(Math.floor(Math.random() * range), base), duration);
            break;
        }

        case 4: {
        // Walk up or down with probability .5
            if (step == 0){
                step += 1;
            }
            else if (step == range-1){
                step -= 1;
            }
            else {
                if (Math.random() >= .5 ){
                    step += 1;
                }
                else {
                    step -= 1;
                }
            }
            nextNote(ragaStepToPitch(step,base), duration);
            break;
        }

        case 5: {
        // up with probability .4, .1 (for 1 step, 2 step) down with probability (.4, .1)
            var downTwo, downOne, upOne, upTwo, sameNote;
            if (step == 0){
                downOne = 0;
            }
            else {
                downOne = .4;
            }

            if (step < 2){
                downTwo = 0;
            }
            else {
                downTwo = .1;
            }

            if (step == (range-1)){
                upOne = 0;
            }
            else {
                upOne = .4;
            }

            if (step > (range-3)){
                upTwo = 0;
            }
            else {
                upTwo = .1;
            }
            sameNote = 0.02;

            console.log("step: " + step + " relative probs: " +[downTwo, downOne, sameNote, upOne, upTwo]);
            index = sampleEvenly([downTwo, downOne, sameNote, upOne, upTwo]);
            index = index - 2;
            step = step + index;
            console.log(index)
            nextNote(ragaStepToPitch(step,base), duration);
            break;
        }

        case 6: {
        // up with probability .4, .1 (for 1 step, 2 step) down with probability (.4, .1)
        // Also double probability of moving in same direction as last step
            var downTwo, downOne, upOne, upTwo, sameNote;
            if (step == 0){
                downOne = 0;
            }
            else {
                downOne = .4;
            }

            if (step < 2){
                downTwo = 0;
            }
            else {
                downTwo = .1;
            }

            if (step == (range-1)){
                upOne = 0;
            }
            else {
                upOne = .4;
            }

            if (step > (range-3)){
                upTwo = 0;
            }
            else {
                upTwo = .1;
            }
            sameNote = 0.02;


            console.log("step: " + step + " relative probs: " +[downTwo, downOne, sameNote, upOne, upTwo]);

            var multiplier = 4;
            if (lastStep > 0){
                upOne *= multiplier;
                upTwo *= multiplier;

            }
            else if (lastStep < 0){
                downOne *= multiplier;
                downTwo *= multiplier;
            }

            index = sampleEvenly([downTwo, downOne, sameNote, upOne, upTwo]);
            index = index - 2;

            lastStep = index;

            step = step + index;
            console.log(index)
            nextNote(ragaStepToPitch(step,base), duration);
            break;
        }

    //Set oscillator
    }
};
