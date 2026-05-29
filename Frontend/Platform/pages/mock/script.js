function alternateEye(){
    const pass = document.querySelector(".password")
    const eye = document.querySelector("#btn-senha");
    
    if(pass.type === 'password'){
        pass.setAttribute("type", "text");
        eye.classList.replace('bi-eye', 'bi-eye-slash');
    }else{
        pass.setAttribute("type", "password");
        eye.classList.replace('bi-eye-slash', 'bi-eye');
    }
}