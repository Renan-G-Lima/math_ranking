//API's
async function login(){
    let _email = document.getElementById("email").value;
    let _password = document.getElementById("password").value;

    const url = "http://127.0.0.1:5500/login";

    try {
        const response = await fetch(url,{
            method: 'POST',
            headers: {
                'Content-type' : 'application/json',
            }, 
            body: JSON.stringify({email: _email, password: _password}),
        })

        const data = await response.json();

        console.log(data);

    }
    catch(e){
        console.log("Error: ", e.message);
    }

}

//Estilization

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