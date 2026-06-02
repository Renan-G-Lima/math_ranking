import {connection_link} from './connection_link.js';
const CL = new connection_link();
const urlGetProblem = CL.getUrl("/problems");

async function getProblem(){
    const type = document.querySelector(".types").value;
    const difficulty = document.querySelector(".difficulty").value;

    let problem = "";
    try{
        const response = await fetch(`${urlGetProblem}?type=${type}&difficulty=${difficulty}`);

        problem = await response.json();
        console.log(problem)
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