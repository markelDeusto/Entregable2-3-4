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