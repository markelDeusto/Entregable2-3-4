let aument = document.getElementById('aumentar')
aument.addEventListener('click', aumentarTexto)

let dismin = document.getElementById('disminuir')
dismin.addEventListener('click', disminuirTexto)

function aumentarTexto(event){
    let body = document.querySelector('body');

    let currentFontSize = parseFloat(window.getComputedStyle(body).fontSize) / parseFloat(window.getComputedStyle(document.documentElement).fontSize );

    let newFontSize = parseFloat(currentFontSize) + 0.2;

    body.style.fontSize = newFontSize + 'rem';
}

function disminuirTexto(event){
    let body = document.querySelector('body');

    let currentFontSize = parseFloat(window.getComputedStyle(body).fontSize) / parseFloat(window.getComputedStyle(document.documentElement).fontSize );

    let newFontSize = parseFloat(currentFontSize) - 0.2;

    body.style.fontSize = newFontSize + 'rem';
}