import {interactableOBJ} from "./interactableOBJ.js";

const elementIOBJ = [];
let id = 0;

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

function createButtonType(Type){
    let idCount;
    idCount = "card"+id; 
    id++;

    switch(Type){
        case "quadraticEquation" : 
        elementIOBJ.push(new interactableOBJ(
            idCount, 
            "quadraticEquation", 
            "ax^2 + bx + c = 0", 
            "Uma equação do segundo grau é uma igualdade matemática em que a incógnita (geralmente representada pela letra (x) possui 2 como seu maior expoente. Ela pode ser escrita na forma geral: ax^2 + bx + c = 0"
        )); 
        break;

        case "sum" : 
        elementIOBJ.push(new interactableOBJ(idCount, 
            "sum", 
            "x + y = 0", 
            "A soma simples é a operação matemática básica de juntar duas ou mais quantidades para encontrar um valor total. Ela é representada pelo sinal de adição (+), onde os números somados são chamados de parcelas e o resultado é a própria soma."
        )); 
        break;

        case "sub" : 
        elementIOBJ.push(new interactableOBJ(idCount, 
            "sub", 
            "x - y = 0", 
            "A subtração simples é a operação matemática básica de determinar a diferença entre duas quantidades. Ela é representada pelo sinal de subtração (-), em que o número do qual se retira uma quantidade é chamado de minuendo, o número retirado é o subtraendo e o resultado da operação é denominado diferença."
        )); 
        break;

        case "div" : 
        elementIOBJ.push(new interactableOBJ(
            idCount, 
            "div", 
            "\\frac{a}{b} = 0", 
            "A divisão simples é a operação matemática básica de repartir uma quantidade em partes iguais ou determinar quantas vezes um número está contido em outro. Ela é representada pelo sinal de divisão (÷) ou pela barra (/), em que o número a ser dividido é chamado de dividendo, o número pelo qual se divide é o divisor, o resultado é o quociente e, quando a divisão não é exata, o valor restante é chamado de resto.."
        )); 
        break;

        case "mult" :
        elementIOBJ.push(new interactableOBJ(
            idCount, 
            "mult", 
            "x * y = 0", 
            "A divisão simples é a operação matemática básica de repartir uma quantidade em partes iguais ou determinar quantas vezes um número está contido em outro. Ela é representada pelo sinal de divisão (÷) ou pela barra (/), em que o número a ser dividido é chamado de dividendo, o número pelo qual se divide é o divisor, o resultado é o quociente e, quando a divisão não é exata, o valor restante é chamado de resto."
        )); 
        break;

        case "sqrt":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "sqrt",
            "\\sqrt{x}",
            "A raiz quadrada é a operação que determina qual número, multiplicado por ele mesmo, resulta no valor informado."
        ));
        break;

        case "nthRoot":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "nthRoot",
            "\\sqrt[n]{x}",
            "A raiz de índice n representa o número que, elevado ao índice informado, resulta no valor desejado."
        ));
        break;

        case "power":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "power",
            "x^{n}",
            "A potenciação representa a multiplicação sucessiva de uma base por ela mesma."
        ));
        break;

        case "subscript":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "subscript",
            "x_{n}",
            "O subscrito é utilizado para identificar índices, elementos de sequências e variáveis relacionadas."
        ));
        break;

        case "fraction":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "fraction",
            "\\frac{a}{b}",
            "A fração representa uma divisão entre duas quantidades."
        ));
        break;

        case "integral":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "integral",
            "\\int_a^b f(x) dx",
            "A integral é utilizada para calcular áreas, acumulações e outras grandezas no cálculo."
        ));
        break;

        case "sumNotation":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "sumNotation",
            "\\sum_{i=1}^{n} i",
            "O somatório representa a soma de uma sequência de valores."
        ));
        break;

        case "product":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "product",
            "\\prod_{i=1}^{n} i",
            "O produtório representa o produto de uma sequência de valores."
        ));
        break;

        case "limit":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "limit",
            "\\lim_{x\\to0} f(x)",
            "O limite descreve o comportamento de uma função quando a variável se aproxima de um determinado valor."
        ));
        break;

        case "derivative":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "derivative",
            "\\frac{d}{dx}f(x)",
            "A derivada representa a taxa de variação instantânea de uma função."
        ));
        break;

        case "partial":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "partial",
            "\\frac{\\partial f}{\\partial x}",
            "A derivada parcial é utilizada em funções com duas ou mais variáveis."
        ));
        break;

        case "vector":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "vector",
            "\\vec{v}",
            "Um vetor representa uma grandeza com módulo, direção e sentido."
        ));
        break;

        case "bar":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "bar",
            "\\overline{AB}",
            "A barra superior é utilizada em segmentos de reta, médias e diversas notações matemáticas."
        ));
        break;

        case "parentheses":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "parentheses",
            "\\left(\\frac{a}{b}\\right)",
            "Parênteses ajustáveis acompanham automaticamente o tamanho da expressão."
        ));
        break;

        case "brackets":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "brackets",
            "\\left[x+y\\right]",
            "Colchetes ajustáveis são usados para agrupar expressões matemáticas."
        ));
        break;

        case "absolute":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "absolute",
            "\\left|x\\right|",
            "O valor absoluto representa a distância de um número até o zero na reta numérica."
        ));
        break;

        case "infinity":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "infinity",
            "\\infty",
            "O símbolo do infinito representa uma quantidade ilimitada."
        ));
        break;

        case "pi":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "pi",
            "\\pi",
            "π é a constante que representa a razão entre o comprimento de uma circunferência e seu diâmetro."
        ));
        break;

        case "theta":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "theta",
            "\\theta",
            "A letra grega θ é frequentemente utilizada para representar ângulos."
        ));
        break;

        case "alpha":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "alpha",
            "\\alpha",
            "A letra grega α é amplamente utilizada como variável em matemática e física."
        ));
        break;

        case "beta":
        elementIOBJ.push(new interactableOBJ(
            idCount,
            "beta",
            "\\beta",
            "A letra grega β é utilizada em diversas áreas da matemática, estatística e física."
        ));
        break;
    }
    checkElementsOnDOM();
}

document.getElementById("quadraticButton").addEventListener("click", () => {
    createButtonType("quadraticEquation");
});

document.getElementById("sumButton").addEventListener("click", () => {
    createButtonType("sum");
});

document.getElementById("subButton").addEventListener("click", () => {
    createButtonType("sub");
});

document.getElementById("multButton").addEventListener("click", () => {
    createButtonType("mult");
});

document.getElementById("divButton").addEventListener("click", () => {
    createButtonType("div");
});

document.getElementById("sqrtButton").addEventListener("click", () => {
    createButtonType("sqrt");
});

document.getElementById("nthRootButton").addEventListener("click", () => {
    createButtonType("nthRoot");
});

document.getElementById("powerButton").addEventListener("click", () => {
    createButtonType("power");
});

document.getElementById("subscriptButton").addEventListener("click", () => {
    createButtonType("subscript");
});

document.getElementById("integralButton").addEventListener("click", () => {
    createButtonType("integral");
});

document.getElementById("sumNotationButton").addEventListener("click", () => {
    createButtonType("sumNotation");
});

document.getElementById("productButton").addEventListener("click", () => {
    createButtonType("product");
});

document.getElementById("limitButton").addEventListener("click", () => {
    createButtonType("limit");
});

document.getElementById("derivativeButton").addEventListener("click", () => {
    createButtonType("derivative");
});

document.getElementById("partialButton").addEventListener("click", () => {
    createButtonType("partial");
});

document.getElementById("vectorButton").addEventListener("click", () => {
    createButtonType("vector");
});

document.getElementById("barButton").addEventListener("click", () => {
    createButtonType("bar");
});

document.getElementById("parenthesesButton").addEventListener("click", () => {
    createButtonType("parentheses");
});

document.getElementById("bracketsButton").addEventListener("click", () => {
    createButtonType("brackets");
});

document.getElementById("absoluteButton").addEventListener("click", () => {
    createButtonType("absolute");
});

document.getElementById("infinityButton").addEventListener("click", () => {
    createButtonType("infinity");
});

document.getElementById("piButton").addEventListener("click", () => {
    createButtonType("pi");
});

document.getElementById("thetaButton").addEventListener("click", () => {
    createButtonType("theta");
});

document.getElementById("alphaButton").addEventListener("click", () => {
    createButtonType("alpha");
});

document.getElementById("betaButton").addEventListener("click", () => {
    createButtonType("beta");
});



