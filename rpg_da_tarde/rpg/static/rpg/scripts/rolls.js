export function rolls(input){
    input = input.toLowerCase().trim();
    // Retorno do rolador"
    let rolada = 0
    // Todos os valores em lista do input
    let res = [];
    // Serve só para juntar no caso de duas variaveis fazerem parte de uma "partes"
    let op = []
    // Partes da equação
    let partes = input.split(',');

    console.log("Partes: ", partes)

    function rolador(especial, qtd, faces){
        rolada = 0;
        let op = [];
        if (especial.includes("!")){
            for (let y = 0; y < 2; y++){
              op[y] = parseInt(rolador("", qtd, faces));
              console.log("Op: ", op[y])
            }
            rolada = Math.max(...op);
        }
        else if(especial.includes("_")){
            for (let y = 0; y < 2; y++){
              op[y] = parseInt(rolador("", qtd, faces));
              console.log("Op: ", op[y])
        }
            rolada = Math.min(...op);
        }
        else{
            for (let ii = 0; ii < qtd; ii++){
                let calc = Math.floor(Math.random() * faces) + 1;
                rolada += calc;
                console.log("Atual rolada: ", rolada);
                console.log("Face: ", calc);
            }
        }
        return rolada;
    }    

    for (let i = 0; i < partes.length; i++){

        console.log("Parte: ", partes[i])

        op = 0

        let dice = partes[i].toLowerCase().replace(/([!_]?)(\d+)d(\d+)/g, (match, especial, qtd, faces) => {
            console.log("Dice: ", match, especial, qtd, faces)
            let total = rolador(especial, qtd, faces);
            console.log("Parte antes do replace: ", partes[i])
            return total;
        });

        
        res[i] = new Function('return ' + dice)();
        console.log("Dice depois do replace final: ", dice)
        console.log("Res: ", res[i])
        
    }
    console.log(res)
    return res
}
