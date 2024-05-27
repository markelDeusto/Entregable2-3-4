//AUMENTAR/DISMINUIR TEXTO

document.addEventListener('DOMContentLoaded', function () {
    // Seleccionar todos los elementos de texto del body
    const elementosTexto = document.querySelectorAll("body *");

    // Coger los tamaños de fuente iniciales
    elementosTexto.forEach(elemento => {
        let tamanoInicial = window.getComputedStyle(elemento).fontSize;
        tamanoInicial = parseFloat(tamanoInicial);
        elemento.setAttribute('data-tamano-inicial', tamanoInicial);
    });

    let aument = document.getElementById('aumentar');
    let dismin = document.getElementById('disminuir');

    // Verificación de que los botones existen antes de agregar el event listener
    if (aument && dismin) {
        aument.addEventListener('click', aumentarTexto);
        dismin.addEventListener('click', disminuirTexto);
    }

    function aumentarTexto() {
        elementosTexto.forEach(elemento => {
            let tamano = parseFloat(elemento.getAttribute('data-tamano-inicial'));
            let nuevoTamano = tamano + 2;
            elemento.style.fontSize = nuevoTamano + 'px';
            elemento.setAttribute('data-tamano-inicial', nuevoTamano);
        });
    }

    function disminuirTexto() {
        elementosTexto.forEach(elemento => {
            let tamano = parseFloat(elemento.getAttribute('data-tamano-inicial'));
            let nuevoTamano = tamano - 2;
            elemento.style.fontSize = nuevoTamano + 'px';
            elemento.setAttribute('data-tamano-inicial', nuevoTamano);
        });
    }


    //FETCH

    function clicarCheckbox(event) {
        const checkbox = event.target;
        const cod_pedido = checkbox.dataset.id;
        const url = checkbox.dataset.url;
        const estado = checkbox.checked;
        actualizarEstado(url, estado, cod_pedido);
    }

    // Función para enviar el estado actualizado al servidor
    function actualizarEstado(url, estado, cod_pedido) {
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Añadir el token CSRF
            },
            body: JSON.stringify({estado: estado})
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                actualizarTexto(cod_pedido, data.estado);
                if (data.estado) {
                    document.getElementById("checkbox_" + cod_pedido).disabled = true;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    // Función para obtener el token CSRF de las cookies
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

    // Función para actualizar el texto basado en el estado
    function actualizarTexto(cod_pedido, estado) {
        const textoEstado = document.getElementById("textoEstado_" + cod_pedido);
        textoEstado.textContent = estado ? 'Enviado' : 'En proceso';
    }

    // Añadir el event listener a todos los checkboxes
    document.querySelectorAll('.checkbox input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('click', clicarCheckbox);
    });


    //MOSTRAR/OCULTAR INFORMACIÓN

    let mostrar = document.getElementById('mostrar');
    let ocultar = document.getElementById('ocultar');

    //Verificación de que los botones existen antes de agregar el EventListener
    if (mostrar && ocultar) {
        mostrar.addEventListener('click', mostrarProductos);
        ocultar.addEventListener('click', ocultarProductos);
    }

    function mostrarProductos() {
        let prods = document.getElementsByClassName("productos_mostrar");
        let btnOcult = document.getElementById("ocultar");
        let celdOcult = document.querySelector(".celda_ocult");
        let btnMost = document.getElementById("mostrar");

        for (let i = 0; i < prods.length; i++) {
            prods[i].style.display = "table-row";
        }

        celdOcult.style.display = "table-row";
        btnOcult.style.display = "block";
        btnMost.style.display = "none";
    }

    function ocultarProductos() {
        let prods = document.getElementsByClassName("productos_mostrar");
        let btnMost = document.getElementById("mostrar");
        let btnOcult = document.getElementById("ocultar");

        for (let i = 0; i < prods.length; i++) {
            prods[i].style.display = "none";
        }

        btnMost.style.display = "block";
        btnOcult.style.display = "none";
    }


    // VALIDACIÓN CODIGO PEDIDO

    const cod_pedido_input = document.getElementById('id_cod_pedido');
    const boton_siguiente = document.getElementsByClassName("boton_siguiente")[0];
    let contenedorMensaje = document.getElementById("mensaje");

    if (cod_pedido_input && boton_siguiente && contenedorMensaje) {
        cod_pedido_input.addEventListener('focusout', () => {
            if (!validarCodigoPedido(cod_pedido_input.value)) {
                contenedorMensaje.textContent = "* El código de pedido debe estar compuesto de 4 letras y 2 números en ese orden *";
                contenedorMensaje.style.color = "red"
                contenedorMensaje.style.fontWeight = "bolder"
                cod_pedido_input.focus();
                boton_siguiente.disabled = true;
            } else {
                contenedorMensaje.textContent = "";
                boton_siguiente.disabled = false;
            }
        });
    }

    function validarCodigoPedido(cod_pedido) {
        const comprobacion = /^[a-zA-Z]{4}\d{2}$/;
        return comprobacion.test(cod_pedido);
    }
});
