//Estilizacao
function alternateEye(){
    const pass = document.getElementById("password");
    const eye = document.getElementById("btn-senha");
    
    if(pass.type === 'password'){
        pass.setAttribute("type", "text");
        eye.classList.replace('bi-eye', 'bi-eye-slash');
    }else{
        pass.setAttribute("type", "password");
        eye.classList.replace('bi-eye-slash', 'bi-eye');
    }
}

function toggleAnimation(type){
    const box = document.getElementById("Box");

    if(type === "login"){
        box.animate([
            {
                transform: "translateX(0px)", 
                borderRadius: "0 2em 2em 0em",
            },
            {
                transform: "translateX(-400px)", 
                borderRadius: "2em 0 0 2em",
            }
        ], {
            duration: 800,
            fill: "forwards",
            easing: "ease-in-out"
        });
    }else if(type === "register"){
        box.animate([
            {
                transform: "translateX(-400px)", 
                borderRadius: "2em 0 0 2em",
            },
            {
                transform: "translateX(0px)", 
                borderRadius: "0 2em 2em 0em",
            }
        ], {
            duration: 800,
            fill: "forwards",
            easing: "ease-in-out"
        });
    }
}