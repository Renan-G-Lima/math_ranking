//API's
//Porta do servidor
const url = "http://127.0.0.1:5500/login";

async function login(){
    const _email = document.getElementById("email").value;
    const _password = document.getElementById("password").value;

    const dataLogin = {email: _email, password: _password}
    try {
        const response = await fetch(url,{
            method: 'POST',
            headers: {'Content-type' : 'application/json',}, 
            body: JSON.stringify({dataLogin}),
        })

        const data = await response.json();

    }
    catch(e){
        console.log("Error: ", e.message);
    }

}

async function register(){
    const _email = document.getElementById(emailR).value;
    const _password = document.getElementById(passwordR).value;
    const _confirmation = document.getElementById(passwordC).value;

    const dataRegister = {email: _email, password: _password, confirmation: _confirmation}
    try {
        const response = await fetch(url,{
            method: 'POST',
            headers: {'Content-type' : 'application/json',}, 
            body: JSON.stringify({dataRegister}),
        })

        if(response.ok){
            const data = await response.json();
            localStorage.setItem('acess_token', response.token);
            window.location.href = "home.html";
        }
    }
    catch(e){
        console.log("Error: ", e.message);
    }
}

async function checkAcessToken(acToken){
    try{
    const response = await fetch(url,{
        method: 'POST',
        headers: {'Content-type' : 'application/json',},
        body: JSON.stringify( {acessToken: acToken}),
    })

        if(response.ok){
            return true
        }
    return false;
    }
    catch(e){
        console.log("Error: ", e.message);
    }
}
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