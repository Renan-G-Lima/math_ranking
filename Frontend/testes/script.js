let newX = 0;
let newY = 0;
let startX = 0;
let startY = 0;

let selectedCard = null;
let latestSelected = null;

document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("mousedown", function(e) {
        latestSelected = selectedCard;

        selectedCard = e.target.closest(".card");
        if(latestSelected == null){
            latestSelected = selectedCard;
        }
        if(!card) return;

        console.log("Card selecionado:", selectedCard);
        console.log("ID:", selectedCard.id);

        mouseDown(e);
        isSelected(e);
    });
});

function isSelected(e){
    if(latestSelected !== selectedCard && latestSelected !== null){
        latestSelected.style.border = "none";
    }

    selectedCard.style.border = "white solid 2px";
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

