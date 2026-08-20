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
    if(selectedCard.offsetTop - newY < 0){
        selectedCard.style.top = 0 + 'px';
    }else if(selectedCard.offsetTop - newY > window.innerHeight - selectedCard.offsetHeight){
        selectedCard.style.top = (window.innerHeight - selectedCard.offsetHeight) + 'px';
    }

    selectedCard.style.left = (selectedCard.offsetLeft - newX) + 'px';
    if(selectedCard.offsetLeft - newX < 0){
        selectedCard.style.left = 0 + 'px';
    } else if(selectedCard.offsetLeft - newX > window.innerWidth - selectedCard.offsetWidth){
        selectedCard.style.left = (window.innerWidth - selectedCard.offsetWidth) + 'px';
    }
    
    //console.log({newX, newY});
    //console.log({startX, startY});
}

function mouseUp(e){
    document.removeEventListener('mousemove', mouseMove);
}


document.querySelector("#toggleMenu").addEventListener("click", function(){
    const leftMenu = document.querySelector(".leftMenu");
    const toggleButton = document.querySelector("#toggleMenu");
    leftMenu.style.visibility = leftMenu.style.visibility === "hidden" ? "visible" : "hidden";
    
    if(leftMenu.style.visibility === "hidden"){
        toggleButton.style.left = "0px";
        toggleButton.textContent = "▶";
    } else {
        toggleButton.style.left = "300px";
        toggleButton.textContent = "◀";
    }
});
