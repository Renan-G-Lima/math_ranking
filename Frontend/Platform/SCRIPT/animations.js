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

function toggleAnimation(type) {
    const box = document.getElementById("Box");

    if (layoutStyle === 0) {
        if (type === "login") {
            box.animate([
                {
                    right: "0",
                    borderRadius: "0 2em 2em 0em"
                },
                {
                    right: "50%",
                    borderRadius: "2em 0 0 2em"
                }
            ], {
                duration: 800,
                fill: "forwards",
                easing: "ease-in-out"
            });

        } else if (type === "register") {
            box.animate([
                {
                    right: "50%",
                    borderRadius: "2em 0 0 2em"
                },
                {
                    right: "0",
                    borderRadius: "0 2em 2em 0em"
                }
            ], {
                duration: 800,
                fill: "forwards",
                easing: "ease-in-out"
            });
        }
    }
}

window.addEventListener('resize', function(){
    let width = window.innerWidth;

    if(width <= 480){
        return layoutStyle = 1;
    }
    return layoutStyle = 0;
});

let layoutStyle = 0;