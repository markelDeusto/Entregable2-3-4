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