import {connection_link} from './connection_link.js';
console.log("teste");
const CL = new connection_link();
const urlLogin = CL.getUrl("/login");

async function login(){
    const _email = document.getElementById("email").value;
    const _password = document.getElementById("password").value;

    const dataLogin = {email: _email, password: _password}
    try {
        const response = await fetch(urlLogin,{
            method: 'POST',
            headers: {'Content-type' : 'application/json',}, 
            body: JSON.stringify(dataLogin),
        })

        const data = await response.json();

        if(response.ok && data){
           return window.location.href = "/";
        }
        alert("Usuário incorreto"); //Precisa fazer alterar o elemento do DOM.
    }
    catch(e){
        console.log("Error: ", e.message);
    }
}

const urlRegister = CL.getUrl("/register");
async function register(){
    const _email = document.getElementById("emailR").value;
    const _password = document.getElementById("passwordR").value;
    const _confirmation = document.getElementById("passwordC").value;

    const dataRegister = {email: _email, password: _password, confirmation: _confirmation}
    try {
        const response = await fetch(urlRegister,{
            method: 'POST',
            headers: {'Content-type' : 'application/json'}, 
            body: JSON.stringify(dataRegister),
        })

        const data = await response.json();

        if(response.ok && data){
            window.location.href = "/";
        }
    }
    catch(e){
        console.log("Error: ", e.message);
    }
}

document.querySelector('._form_login').addEventListener('submit', function(event) {
    event.preventDefault();
    login();
});

document.querySelector('._form_createAcc').addEventListener('submit', function(event) {
    event.preventDefault();
    register();
});

const urlOAuth = CL.getUrl("/authorize/google");

document.querySelector("#oauth").addEventListener("click", () => {
    console.log(urlOAuth);
    window.location.href = urlOAuth;
})