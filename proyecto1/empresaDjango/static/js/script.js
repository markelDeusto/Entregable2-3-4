const elementosTexto = document.querySelectorAll("body *");

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



    document.addEventListener("DOMContentLoaded", function() {
        // Obtener el token CSRF
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Agregar event listeners a todos los checkboxes
        document.querySelectorAll('[id^="estado_cambiar_"]').forEach(function(checkbox) {
            checkbox.addEventListener("change", function(event) {
                actualizarEstado(event, csrfToken);
            });
        });
    });

function actualizarEstado(event, csrfToken) {
        event.preventDefault();
        const checkbox = event.currentTarget;
        const estado = checkbox.checked;
        const pedidoCod = checkbox.getAttribute("data-pedido");

        // URL de la vista que maneja la actualización del estado
        const url = `/actualizar_estado_pedido/${pedidoCod}/`;

        // Crear la solicitud fetch
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
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