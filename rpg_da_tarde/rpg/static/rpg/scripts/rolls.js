document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const input = document.getElementById('input').value;
            const output = document.getElementById('output_container');
            let resultado = rolls(input);
            console.log("ress: ", resultado);
            
            const separator = document.createElement('p');
            separator.textContent = '----------------------------------------------------------------------';
            output.appendChild(separator);
            
            // Adiciona cada resultado em um p diferente
            for (let i = 0; i < resultado.length; i++){
                const p = document.createElement('p');
                p.textContent = resultado[i];
                output.appendChild(p);
            }
        });
    }
});

// Tem q adicionar aql paranaue de equação com 

export function rolls(input){
    // valores antes e depois do d
    let dice = []
    // Retorno do rolador"
    let rolada = 0
    // Todos os valores em lista do input
    let res = [];
    // Serve só para juntar no caso de duas variaveis fazerem parte de uma "partes"
    let op = 0
    // Ja diz o nome
    let sub_partes = []

    let partes = input.split(',');

    input = input.toLowerCase(); 

    function rolador(dice){
        rolada = 0
        if (dice.length == 2){
            for (let ii = 0; ii < dice[0]; ii++){
                let calc = Math.floor(Math.random() * dice[1] + 1)
                rolada += calc 
                console.log("Atual rolada: ", rolada)
                console.log("Face: ", calc)
            }
        }
        else{
            rolada = dice[0]
            console.log("resultado: ",rolada)
        }
        return rolada;
    }    

    for (let i = 0; i < partes.length; i++){
        console.log("Parte: ", partes[i])

        // Soma
        if (partes[i].includes("+")){
            sub_partes = partes[i].split("+")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                op += parseInt(rolador(dice))
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Subtração
        else if (partes[i].includes("-")){
            sub_partes = partes[i].split("-")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                op -= parseInt(rolador(dice))
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Multiplicação
        else if (partes[i].includes("*")){
            sub_partes = partes[i].split("*")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                op *= parseInt(rolador(dice))
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Divisão
        else if (partes[i].includes("/")){
            sub_partes = partes[i].split("/")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                op /= parseInt(rolador(dice))
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Vantagem
        else if (partes[i].includes("!")){
            let cont = 0;
            for (let letra of dice) {
                if (letra === '!') contador++;
                dice.slice(cont)
            }
            dice = partes[i].split("d")
            for(let j = -1; j < cont; j++){
                dice[0] = dice[0].slice(1)
                console.log("dice",dice)
                if (op > rolador(dice)){
                    res[i] = op
                }
                else{
                    op = rolador(dice)
                    res[i] = op
                }
                console.log("op: ",op)
            }
        }

        // Desvantagem
        else if (partes[i].includes("_")){
            dice = partes[i].split("d")
            for(let j = 0; j !==2; j++){
                dice[0] = dice[0].slice(1)
                console.log("dice",dice)
                if (op < rolador(dice)  && op != 0 ){
                    res[i] = op
                }
                else{
                    op = rolador(dice)
                    res[i] = op
                }
                console.log("op: ",op)
            }
        }

        else if (partes[i].includes("d")){
            dice = partes[i].split("d");
            res[i] = rolador(dice)
            }

        else{
            res[i] = parseInt(partes[i])
        }
        
    }
    console.log(res)
    return res
}
