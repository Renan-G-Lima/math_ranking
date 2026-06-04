import {connection_link} from './connection_link.js';
const CL = new connection_link();
const urlGetProblem = CL.getUrl("/problems");

let problem = "";
async function getProblem(){
    const type = document.querySelector(".types").value;
    const difficulty = document.querySelector(".difficulty").value;

    try{
        const response = await fetch(`${urlGetProblem}?type=${type}&difficulty=${difficulty}`);

        problem = await response.json();
        console.log(problem);
    }
    catch(e){
        console.log("Error: ", e.message);
    }

    const problemText = document.querySelector("._question_text");
    const problemValues = `${problem.payload.x} + ${problem.payload.y}`;
    problemText.innerHTML = problemValues;
}

const buttonGet = document.querySelector("#getProblem");
buttonGet.addEventListener("click", function(){
    getProblem();
});

const urlResponse = CL.getUrl("/submit_test");
async function sendSolution(){
    const solution = document.querySelector("#sendResolution").value;
    /*
    const response = await fetch(urlResponse, {
        method: 'POST',
        headers: {'Content-type' : 'application/json'}, 
        body: JSON.stringify(solution),
    })

    response = await response.json();

    console.log(response);*/
    const params = new URLSearchParams({
        x: problem.payload.x,
        y: problem.payload.y,
        operation: "+",
        answer: solution
    });
    
    const response = await fetch(`${urlResponse}?${params}`);
    
    console.log(await response.json());
}

const buttonSend = document.querySelector("#buttonSend");

buttonSend.addEventListener("click", function(){
    sendSolution();
})