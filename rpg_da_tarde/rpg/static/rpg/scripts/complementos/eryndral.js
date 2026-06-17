const exp = document.querySelector('[name="experiencia"]');
let mana_box = document.getElementById("mana-value");
let buttons = document.querySelectorAll(".magic");
let exp_value = parseInt(exp.value) || 0;

const tabela_mana = [4, 6, 14, 17, 27, 32, 38, 44, 57, 64, 73, 73, 83, 83, 94, 94, 107, 114, 123, 133];
const custo_mana = [2, 3, 5, 6, 7, 9, 10, 11, 13];
const tabelaXP = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000];

// Calculo mana
//let exp_value = 900;
let nivel = 1;

for (let i = 0; i < tabelaXP.length; i++) {
    if (exp_value >= tabelaXP[i]) {
        nivel = i + 1;
    }
}

let mana = tabela_mana[nivel - 1];
mana_box.textContent = mana;
console.log("Mana do personagem: ", mana);
console.log("Nível do personagem: ", nivel);

let x = document.addEventListener("click", (event) => {
    for (let i = 0; i < buttons.length; i++) {
        if (event.target.id === `magic_${i + 1}`) {
            if (mana >= custo_mana[i]) {
                mana -= custo_mana[i];
                mana_box.textContent = mana;
                console.log(`Usou magia ${i + 1}. Mana restante: ${mana}`);
            } else {
                console.log("Mana insuficiente para usar a magia.");
            }
        }
    }
});
