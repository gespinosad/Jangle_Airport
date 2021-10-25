eventListeners()

function eventListeners() {
    const formulario = document.querySelector("#form");
    formulario.addEventListener('submit', validar);
}

function validar(e) {
    e.preventDefault();

    const edad = parseInt(document.querySelector('#age').value);

    if (edad >= 20){
        swal.fire({
            icon: "success",
            title: "Bienvenido",
            text: "Edad apropiada"
        })
    } else {
        swal.fire({
            icon: "error",
            title: "Rechazado",
            text: "Edad inapropiada"
        })
    }
}