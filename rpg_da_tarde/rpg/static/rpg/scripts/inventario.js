document.querySelectorAll('button.decrementar').forEach(function(eachButton) {
    eachButton.addEventListener('click', function(event) {
        event.preventDefault();
        const itemId = this.getAttribute('data-id');
        const quantidadeInput = document.querySelector(`input.quantidade-input[data-id="${itemId}"]`);
        console.log('Decrementar item:', itemId);
        if (!quantidadeInput) return;
        let quantidadeAtual = parseInt(quantidadeInput.value, 10) || 0;
        if (quantidadeAtual > 0) {
            quantidadeAtual -= 1;
        } else {
            quantidadeAtual = 0;
        }
        quantidadeInput.value = quantidadeAtual;
    });
});