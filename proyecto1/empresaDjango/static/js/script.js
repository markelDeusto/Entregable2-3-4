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



  let boton = document.getElementsByClassName('boton_estado')
    boton = addEventListener('click', actualizarEstado)


function actualizarEstado(event) {

        event.preventDefault();
        const checkbox = event.currentTarget;
        const estado = 'True';
        const cod_pedido = checkbox.getAttribute("data-cod_pedido");
        // Crear la solicitud fetch
        fetch('pedido/', {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': 'csrfToken'
            },
            body: JSON.stringify({ estado: estado, cod_pedido: cod_pedido })
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