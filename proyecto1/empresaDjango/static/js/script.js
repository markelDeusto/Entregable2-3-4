const elementosTexto = document.querySelectorAll("body *");


let boton = document.getElementById('boton_estado')
let aument = document.getElementById('aumentar')
let dismin = document.getElementById('disminuir')

aument.addEventListener('click', aumentarTexto)
dismin.addEventListener('click', disminuirTexto)

function aumentarTexto(){

    elementosTexto.forEach(elemento => {
        let tamano = window.getComputedStyle(elemento).fontSize;
        tamano = parseFloat(tamano) ;
        tamano = (tamano + 2);
        elemento.style.fontSize = (tamano ) + 'px'
    })
}

function disminuirTexto(){

    elementosTexto.forEach(elemento => {
        let tamano = window.getComputedStyle(elemento).fontSize;
        tamano = parseFloat(tamano) ;
        tamano = (tamano - 2);
        elemento.style.fontSize = (tamano ) + 'px'
    })
}

document.addEventListener('DOMContentLoaded', (event) => {
    let boton = document.getElementById('boton_estado');
    boton.addEventListener('click', actualizarEstado);
});


function actualizarEstado(event) {

        event.preventDefault();
        const estado = 'True';
        const cod_pedido = event.currentTarget.getAttribute("data-cod_pedido");
        console.log(cod_pedido)
        // Crear la solicitud fetch
        fetch('<str:cod_pedido>/actualizar_estado', {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ estado: estado })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error al actualizar el estado');
            }
        })
        .then(data => {
            if (data.status === 'success') {
                console.log('Estado actualizado correctamente');
            } else {
                console.log('Error al actualizar el estado:', data.errors);
            }
        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
        });
    }

    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let mostrar = document.getElementById('mostrar')

mostrar.addEventListener('click', mostrarProductos)

let ocultar = document.getElementById('ocultar')

ocultar.addEventListener('click', ocultarProductos)
function mostrarProductos(){
    let prods = document.getElementsByClassName("productos_mostrar")
    let btnOcult = document.getElementById("ocultar")
    let btnMost = document.getElementById("mostrar")

    for (let i = 0; i < prods.length; i++) {
        prods[i].style.display = "block";
    }

    btnOcult.style.display = "block"
    btnMost.style.display = "none"

}

function ocultarProductos(){
    let prods = document.getElementsByClassName("productos_mostrar")
    let btnMost = document.getElementById("mostrar")
    let btnOcult = document.getElementById("ocultar")

    for (let i = 0; i < prods.length; i++) {
        prods[i].style.display = "none";
    }

    btnMost.style.display = "block"
    btnOcult.style.display = "none"
}

