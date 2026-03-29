import {connection_link} from './connection_link.js';

const CL = new connection_link();
const url = CL.getUrl();

async function login(){
    const _email = document.getElementById("email").value;
    const _password = document.getElementById("password").value;

    const dataLogin = {email: _email, password: _password}
    try {
        const response = await fetch(url,{
            method: 'POST',
            headers: {'Content-type' : 'application/json',}, 
            body: JSON.stringify(dataLogin),
        })

        const data = await response.json();

        if(response.ok && data){
            return window.location.href= 'home.html';
        }
        alert("Usuário incorreto"); 
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

document.querySelector('._form_login').addEventListener('submit', function(event) {
    event.preventDefault();
    login();
});