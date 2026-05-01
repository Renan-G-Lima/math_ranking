class Calculator{
    //add the value (item) to result in DOM.
    add(item){
        const result = document.querySelector(".result");
        if(result.innerHTML === "0" || result.innerHTML === "Error."){
            result.innerHTML = "";
            return result.innerHTML += item;
        }
        return result.innerHTML += item;
    }
    
    //add operators like +, -, *, /, ( or ) to result in DOM.
    addOperation(item){
        const result = document.querySelector(".result");
        const lastEntrie = this.#checkLastEntrie();

        if(item === ")" && lastEntrie.lastEntrie !== "+"){
            return result.innerHTML += ")"; 
        }

        if(lastEntrie.bool){
            let modifiedResult = this.#removeLastEntrie();
            switch(item){
                case "+" : modifiedResult += "+"; break;
                case "-" : modifiedResult += "-"; break;
                case "*" : modifiedResult += "*"; break;
                case "/" : modifiedResult += "/"; break;
                case "(" : modifiedResult += "*("; break;
            }
            return result.innerHTML = modifiedResult;
        }

        switch(item){
            case "+" : return result.innerHTML += "+";
            case "-" : return result.innerHTML += "-";
            case "*" : return result.innerHTML += "*";
            case "/" : return result.innerHTML += "/";
            case "(" : return result.innerHTML += "*(";
        }
    }

    //checks if de last entrie on result is a operator, case yes, remove the last item and substitues for a new operator.
    #checkLastEntrie(){
        const result = document.querySelector(".result").innerHTML;
        let lastEntrie = result[result.length-1];

        switch(lastEntrie){
            case "+" : return {bool: true};
            case "-" : return {bool: true};
            case "*" : return {bool: true};
            case "/" : return {bool: true};
            case "(" : return {bool: true};
            default : return {bool: false};
        }
    }

    //remove the last entrie in result element, if is a ( remove * too.
    #removeLastEntrie(){
        const result = document.querySelector(".result").innerHTML;
        let currentResult = "";
        let lastEntrie = result[result.length-1];

        if(lastEntrie == "("){
            for(let i = 0; i < result.length-2; i++){
                currentResult += result[i];
            }
            return currentResult;
        }
        for(let i = 0; i < result.length-1; i++){
            currentResult += result[i];
        }
        return currentResult;
    }

    clearResult(){
        const result = document.querySelector(".result");
        result.innerHTML = "0";
    }

    getResult(){
        const result = document.querySelector(".result");
        try{
            return result.innerHTML = eval(result.innerHTML);
        } catch(e){
            return result.innerHTML = "Error."
        }
    }

    erase(){
        const result = document.querySelector(".result");
        let removeLast = "";
        for(let i = 0; i < result.innerHTML.length-1; i++){
            removeLast += result.innerHTML[i];
        }
        result.innerHTML = removeLast;
    }
}

const c = new Calculator;

