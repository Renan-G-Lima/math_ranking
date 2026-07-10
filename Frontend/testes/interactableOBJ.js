export class interactableOBJ{
    id;
    type;
    construction;
    description;
    
    constructor(ID, type, construction, description = null){
        this.id = ID;
        this.type = type;
        this.construction = construction;
        this.description = description;
    }

    generateDOMElement(container){
        let div = document.createElement("div");
        div.className = "card";
        div.id = this.id;

        let p = document.createElement("p");
        let span = document.createElement("span");
        span.className = "formObj";

        let formula = this.construction;
        
        span.textContent = formula;
        p.appendChild(span);
        div.appendChild(p);
        container.appendChild(div);
        window.MQ.MathField(div);
    }
}