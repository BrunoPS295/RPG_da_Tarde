import { rolls } from './rolls.js';
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const input = document.getElementById('input');
            const output = document.getElementById('output_container');
            let resultado = rolls(input.value);
            console.log("ress: ", resultado);
            
            const separator = document.createElement('p');
            separator.textContent = '----------------------------------------------------------------------';
            output.appendChild(separator);
            
            
            for (let i = 0; i < resultado.length; i++){
                const p = document.createElement('p');
                p.textContent = resultado[i];
                output.appendChild(p);
            }
        });
    }
});