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
            
            // Adiciona cada resultado em um p diferente
            for (let i = 0; i < resultado.length; i++){
                const p = document.createElement('p');
                p.textContent = resultado[i];
                output.appendChild(p);
            }
        });
    }
});

//console.log(rolls("(2 -- 4) * 2"))

export function rolls(input){
    input = input.toLowerCase().trim();
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
    // Partes da equação
    let partes = input.split(',');

    function rolador(dice){
        rolada = 0;
        if (Array.isArray(dice) && dice.length === 2){
            for (let ii = 0; ii < count; ii++){
                let calc = Math.floor(Math.random() * faces) + 1;
                rolada += calc;
                console.log("Atual rolada: ", rolada);
                console.log("Face: ", calc);
            }
        } else {
            const valor = Array.isArray(dice) ? dice[0] : dice;
            rolada = parseInt(val);
            console.log("resultado: ", rolada);
        }
        return rolada;
    }    

    for (let i = 0; i < partes.length; i++){
        while (partes[i].includes('(')) {
        op = 0
        partes[i] = partes[i].replace(/\(([^()]+)\)/g, (match, input) => {
            console.log(match, input)
            return rolls(input);
        });
        }

        console.log("Parte: ", partes[i])
        op = 0

        // Soma
        if (partes[i].includes("+")){
            sub_partes = partes[i].split("+")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                if (j == 0){
                    op = parseInt(rolador(dice))
                }else{
                    op += parseInt(rolador(dice))
                }
                
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Subtração
        else if (partes[i].includes("--")){
            sub_partes = partes[i].split("--")
            console.log("sub_partes: ",sub_partes)
            for(let j = 0; j < sub_partes.length; j++){
                dice = sub_partes[j].split("d")
                console.log("dice",dice, dice.length)
                if (j == 0){
                    op = parseFloat(rolador(dice))
                }else{
                    op -= parseFloat(rolador(dice))
                }
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
                if (j == 0){
                    op = parseFloat(rolador(dice))
                }else{
                    op *= parseFloat(rolador(dice))
                }
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
                if (j == 0){
                    op = parseFloat(rolador(dice))
                }else{
                    op /= parseFloat(rolador(dice))
                }
                console.log("op: ",op)
            }
            res[i] = op
        }

        // Vantagem
        else if (partes[i].includes("!")){
            const expr = partes[i].replace(/!/g, '');
            dice = expr.split("d");
            // roll two times and take the highest
            const first = rolador(dice.slice());
            const second = rolador(dice.slice());
            res[i] = Math.max(first, second);
            console.log("vantagem - rolls:", first, second, "->", res[i]);
        }

        // Desvantagem
        else if (partes[i].includes("_")){
            const expr = partes[i].replace(/_/g, '');
            dice = expr.split("d");
            const first = rolador(dice.slice());
            const second = rolador(dice.slice());
            res[i] = Math.min(first, second);
            console.log("desvantagem - rolls:", first, second, "->", res[i]);
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
