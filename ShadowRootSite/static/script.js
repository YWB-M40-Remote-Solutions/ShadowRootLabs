const text = [
"booting shadowroot...",
"initializing modules...",
"loading cybersecurity labs...",
"connecting to community...",
"ready.",
"",
"> join the discord and start hacking"
];

let line = 0;
let char = 0;

function type() {

if(line < text.length){

if(char < text[line].length){

document.getElementById("terminal-text").innerHTML += text[line].charAt(char);
char++;
setTimeout(type,40);

}else{

document.getElementById("terminal-text").innerHTML += "\n";
line++;
char = 0;
setTimeout(type,300);

}

}

}

type();