//console.log("HELLO JULIET PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM
const randomNumber = Math.floor(Math.random() * 100 + 1);
function numberGuess(){
    //alert(randomNumber);
    var x = document.getElementById("guessField").value; 
    if(x==randomNumber){
    } else if (x > randomNumber){
        document.getElementById("guess").innerHTML = "You guessed too high, guess again";
        let node = document.createElement("LI"); 
        let textnode = document.createTextNode(x)
        node.appendChild(textnode);
        document.getElementById("list").appendChild(node)
    } else { 
        document.getElementById("guess").innerHTML = "You guessed too low, guess again";
        let node = document.createElement("LI"); 
        let textnode = document.createTextNode(x)
        node.appendChild(textnode);
        document.getElementById("list").appendChild(node)
    }
};

