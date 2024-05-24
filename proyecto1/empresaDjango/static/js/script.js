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

let boton = document.getElementById('boton_estado');
   boton.addEventListener('click', actualizarEstado);


function actualizarEstado(event) {


      event.preventDefault()
       const cod_pedido = event.currentTarget.dataset.codPedido;
       const estado = true;
       console.log( cod_pedido)
       // Crear la solicitud fetch
       fetch(`${cod_pedido}/actualizar_estado` , {


           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
               'X-CSRFToken': getCookie('csrftoken')
           },
           body: JSON.stringify({ estado: estado })
       })
       .then(response => response.json())
       .then(data => {
           if (data.status === 'success') {
               console.log('Estado actualizado correctamente');
               // Opcionalmente, actualiza el DOM para reflejar el cambio
           } else {
               console.error('Error al actualizar el estado:', data.message);
           }
       })
           .catch(error=> console.log('Error', error))


   }
     // Get CSRF token
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
    let celdOcult = document.querySelector(".celda_ocult")
    let btnMost = document.getElementById("mostrar")

    for (let i = 0; i < prods.length; i++) {
        prods[i].style.display = "table-row";
    }

    celdOcult.style.display = "table-row"
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


document.addEventListener('DOMContentLoaded', function() {
    const cod_pedido_input = document.getElementById('id_cod_pedido');
    const boton_siguiente =document.getElementsByClassName("boton_siguiente")[0];
    let contenedorMensaje = document.getElementById("mensaje");

    cod_pedido_input.addEventListener('focusout', () => {
        if (!validarCodigoPedido(cod_pedido_input.value)) {
            contenedorMensaje.textContent = "El código de pedido debe estar compuesto de 4 letras y 2 números en ese orden"
            cod_pedido_input.focus();
            boton_siguiente.disabled = true;
        }else {
            contenedorMensaje.textContent = "";
            boton_siguiente.disabled = false;
        }
    });

    function validarCodigoPedido(cod_pedido) {
        const comprobacion = /^[a-zA-Z]{4}\d{2}$/;
        return comprobacion.test(cod_pedido);
    }
});


