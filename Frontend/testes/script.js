let newX = 0;
let newY = 0;
let startX = 0;
let startY = 0;

let selectedCard = null;
let latestSelected = null;



document.addEventListener("mousedown", function(e) {
        latestSelected = selectedCard;

        selectedCard = e.target.closest(".card");

        if(!selectedCard) return;

        if(latestSelected !== selectedCard && latestSelected !== null){
            latestSelected.style.border = "none";
        }
    
        //selectedCard.style.border = "white solid 2px";

        console.log("Card selecionado:", selectedCard);
        console.log("ID:", selectedCard.id);

        mouseDown(e);
    });

function isSelected(e){

}

function mouseDown(e){
    console.log("mouseDown")
    startX = e.clientX;
    startY = e.clientY;

    document.addEventListener('mousemove', mouseMove);
    document.addEventListener('mouseup', mouseUp);
}

function mouseMove(e){
    newX = startX - e.clientX;
    newY = startY - e.clientY;

    startX = e.clientX;
    startY = e.clientY;

    selectedCard.style.top = (selectedCard.offsetTop - newY) + 'px';
    selectedCard.style.left = (selectedCard.offsetLeft - newX) + 'px';
    
    //console.log({newX, newY});
    //console.log({startX, startY});
}

function mouseUp(e){
    document.removeEventListener('mousemove', mouseMove);
}

function isColliding(card){
    const cards = document.querySelectorAll(".card");

    const rect = card.getBoudingClientRect();
    
    for(const other  of cards){
        continue;
    }
        const rectO = other.getBoudingClientRect();

        const collision = 
        rect.left < rectO.right && rect.right > rect0.left && rect.top < rectO.bottom && rect.bottom > rectO.top;

        if(collision){
            return true;
        }
    

}
