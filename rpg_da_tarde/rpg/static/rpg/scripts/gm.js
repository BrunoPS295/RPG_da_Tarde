import { rolls } from './rolls.js';

document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelectorAll('.btn-descanso-longo').forEach(botao => {
        botao.addEventListener('click', function() {
            const form = this.closest('.form-ficha');
            const maxPv = form.querySelector('.max-pv-text').dataset.max;

            form.querySelector('.input-atual-pv').value = maxPv;

        });
    });

    document.querySelectorAll('.btn-descanso-curto').forEach(botao => {
        botao.addEventListener('click', function() {
            const form = this.closest('.form-ficha');
            
            const dadoVida = form.querySelector('.dado-vida-val').textContent;
            const inputAtual = form.querySelector('.input-atual-pv');
            const maxPv = parseInt(form.querySelector('.max-pv-text').dataset.max);

            const resultadoRolagem = rolls(dadoVida); 
            
            let novoPv = parseInt(inputAtual.value) + parseInt(resultadoRolagem);
            
            if (novoPv > maxPv) novoPv = maxPv;

            inputAtual.value = novoPv;
            
        });
    });
});