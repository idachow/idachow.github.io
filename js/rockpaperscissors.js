for (var i = 10; i <= 0; i--) {
    console.log(10);
    console.log(i);
}

var userChoice = prompt("Do you choose rock, paper or scissors???");

if(userChoice === "rock") {
    alert("You have chosen rock!");
}
    else if(userChoice === "paper") {
        alert("You have chosen paper!");
    }
        else if(userChoice === "scissors") {
            alert("You have chosen scissors!");
        } 
            else {
                prompt("Please choose rock, paper or scissors.");
            }

var computerChoice = Math.random();

if (computerChoice < 0.34) {
    computerChoice = "rock";
} 
else if(computerChoice <= 0.67) {
    computerChoice = "paper";
} 
else {
    computerChoice = "scissors";
 console.log("Computer: " + computerChoice);
}

var compare = function(choice1,choice2) {
    if (choice1 === choice2) {
        return ("The result is a tie!");
    }
    else if(choice1 === "rock") {
        if(choice2 === "scissors") {
            return "Rock wins";
        }
        else {
            return("Paper wins");
        }
    }
    else if(choice1 === "paper") {
        if(choice2 === "rock") {
            return("Paper wins wins");
        }
        else {
            return("Scissors wins");
        }
    }
    else if(choice1 === "scissors") {
        if(choice2 === "paper") {
            return("Scissors wins");
        }
        else {
            return("Rock wins");
        } 
    }
}

   

compare(userChoice,computerChoice);
