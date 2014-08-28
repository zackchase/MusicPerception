

function permutation(n, r){

    var result = [];
    var selection;

    while (true) {

        console.log("in while loop");

        selection = Math.floor(Math.random() * n);
        if (result.indexOf(selection) > -1){
            continue;
        }
        else{
            result.push(selection);
        }
        if (result.length == r){
            break;
        }
    }
    return result;
}
