import {interactableOBJ} from "./interactableOBJ.js";

const elementIOBJ = [];
let id = 0;
document.querySelector("#gerar").addEventListener('click', function(e){
    e.preventDefault();
    let idCount;
    idCount = "card"+id;
    id++;
    elementIOBJ.push(new interactableOBJ(idCount, "quadraticEquation", "ax^2 + bx + c = 0", "Uma equação do segundo grau é uma igualdade matemática em que a incógnita (geralmente representada pela letra (x) possui 2 como seu maior expoente. Ela pode ser escrita na forma geral: ax^2 + bx + c = 0"));
    console.log(elementIOBJ);
    checkElementsOnDOM();
    elementIOBJ.push(new interactableOBJ(idCount, "sum", "x + y = 0", "A soma simples é a operação matemática básica de juntar duas ou mais quantidades para encontrar um valor total. Ela é representada pelo sinal de adição (+), onde os números somados são chamados de parcelas e o resultado é a própria soma."));
    console.log(elementIOBJ);
    checkElementsOnDOM();
})

function checkElementsOnDOM(){
    const cardContainer = document.querySelector("#container");
    elementIOBJ.forEach(interactableOBJ =>{
        try{
            let iOBJ = document.querySelector(`#${interactableOBJ.id}`);
            if(iOBJ === null){
                interactableOBJ.generateDOMElement(cardContainer);
            }
        }
        catch(e) {
            console.log(e);
        }
    })
}

