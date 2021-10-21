const nombre = document.getElementById("name")
const apellido = document.getElementById("lastname")
const documento = document.getElementById("identificacion")
const edad = document.getElementById("age")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const pass_confirm = document.getElementById("password__confirm")
const form = document.getElementById("form")
const url = window.location="/";

form.addEventListener("submit", e=>{
    e.preventDefault()
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/

    function nota(x, z){
        y = y;
        Swal.fire({
            title: x,
            html: z,
            timer: 2500,
            timerProgressBar: true,
            didOpen: () => {
                Swal.showLoading()
            }
        }).then(y);
    }

    function redireccionar(){
        setTimeout(url, 5000);
    }

    if(nombre.value.length < 3){
        titulo = "Nombre";
        mensaje = 'Falta ingresar el nombre';
        y = nombre.focus();
        nota(titulo,mensaje);
        return false;
    }
    if (apellido.value.length == 0) {
        titulo = "Apellido";
        mensaje = 'Falta ingresar el apellido';
        y = apellido.focus();
        nota(titulo,mensaje);   
        return false;
    }
    if (documento.value.length < 5 || documento.value.length > 10) {
        titulo = "Documento";
        mensaje = 'La cantidad de digitos en su documento no es valida.';
        y = documento.focus();
        nota(titulo,mensaje);
        return false;
    }
    if(edad.value.length == 0){
        titulo = "Edad";
        mensaje = 'Falta ingresar la edad. Se requiere que seas mayor de edad para registrarte.';
        y = edad.focus();
        nota(titulo,mensaje);
        return false;
    }
    if(!regexEmail.test(email.value)){
        titulo = "Email";
        mensaje = 'El email no es valida. Ejemplo: correo@email.com';
        y = email.focus();
        nota(titulo,mensaje);
        return false;
    }
    if(pass.value.length < 8){
        titulo = "Contraseña";
        mensaje = 'Debe de tener mínimo 8 dígitos y ahora tiene ' + pass.value.length;
        y = pass.focus();
        nota(titulo,mensaje);
        return false;
    }
    if(pass_confirm.value.length != pass.value.length){
        titulo = "Confirmación de contraseña";
        mensaje = '¡Debe de ir la misma contraseña!';
        y = pass_confirm.focus();
        nota(titulo,mensaje);
        return false;
    }else{
        titulo = "¡Registrado exitosamente!";
        mensaje = 'Bienvenido ' + nombre + ' esperamos que disfrutes de tu instancia.';
        y = "";
        nota(titulo,mensaje);
        return redireccionar();
    }
})

