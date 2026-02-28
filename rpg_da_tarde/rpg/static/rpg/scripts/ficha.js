import { rolls } from './rolls.js';

const input_i_pv = document.querySelector('[name="i_pv"]')
const max_pv = document.querySelector('[name="max_pv"]');
const atual_pv = document.getElementById("pv_value")
const temp_pv = document.getElementById("temp_pv")
const dpv = document.querySelector('[name="dado_de_vida"]');
const exp = document.querySelector('[name="experiencia"]');
let exp_value = parseInt(exp.value) || 0;

const ca_value = document.getElementById("ca_value");
const ini_value = document.getElementById("ini_value");
const desl_value = document.getElementById("desl_value");
const form = document.getElementById("form")

let prof_bonus_element = document.getElementById('prof_bonus');
let prof_bonus_value = parseInt(prof_bonus_element.value) || 0;

const atributos = ['forca','destreza','constituicao','inteligencia','sabedoria','carisma'];

const pericias = ['acrobacia','arcanismo','atletismo','atuacao','enganacao','furtividade','historia','intimidacao','intuicao','investigacao','animais','medicina','natureza','percepcao','persuasao','prestidigitacao','religiao','sobrevivencia'];

let brut = {};
let atr = {};
let salva = {};
let check_salva = {};
let check_peri = {};
let peri_ = {};


for (let i = 0; i < atributos.length; i++) {
    const atributo = atributos[i];
    check_salva[atributo] = document.getElementById('check_salva_' + atributo);
    brut[atributo] = document.getElementById('brut_' + atributo); 
    atr[atributo] = document.getElementById('atr_' + atributo);   
    salva[atributo] = document.getElementById('salva_' + atributo); 

}

for (let i = 0; i < pericias.length; i++) {
    const pericia = pericias[i];
    check_peri[pericia] = document.getElementById('check_' + pericia);
    peri_[pericia] = document.getElementById(pericia);
}

let modificadores = {};

let itens = document.querySelectorAll('.item-card');

// itens brut
itens.forEach(item => {
    let atr_mod = item.getAttribute('data-target'); 
    let mod = item.getAttribute('data-mod');       
    if (atr_mod && atr_mod.includes("atr")) {
         
        
        if (!modificadores[atr_mod]) {
            modificadores[atr_mod] = "";
        }
        
        modificadores[atr_mod] += mod; 
    }
});
for (let atr_mod in modificadores) {
    let atr_mod_clean = atr_mod.replace("atr_", "").replace("atr", "");
    let valorbase = parseInt(atr[atr_mod_clean].textContent) || 0;
    
    let equacaoFinal = valorbase + modificadores[atr_mod]; 
    let resultado = new Function('return ' + equacaoFinal)();
    atr[atr_mod_clean].textContent = Math.floor(resultado);
    console.log(`Cálculo final de ${atr_mod}: ${equacaoFinal} = ${Math.floor(resultado)}`);
        
    
}

for (let i = 0; i < atributos.length; i++) {
    const atributo = atributos[i];


    let valor_bruto = parseInt(brut[atributo].value) || 0;
    let modificador = Math.floor((valor_bruto - 10) / 2);


    atr[atributo].textContent = parseInt(atr[atributo].textContent)  + modificador;
    

    let bonus_prof = check_salva[atributo].checked ? prof_bonus_value : 0;
    let total_salva = parseInt(atr[atributo].textContent) + bonus_prof;


    salva[atributo].textContent = total_salva;
}


let relacao = {
    'acrobacia': 'destreza', 'arcanismo': 'inteligencia', 'atletismo': 'forca',
    'atuacao': 'carisma', 'enganacao': 'carisma', 'furtividade': 'destreza',
    'historia': 'inteligencia', 'intimidacao': 'carisma', 'intuicao': 'sabedoria',
    'investigacao': 'inteligencia', 'animais': 'sabedoria', 'medicina': 'sabedoria',
    'natureza': 'inteligencia', 'percepcao': 'sabedoria', 'persuasao': 'carisma',
    'prestidigitacao': 'destreza', 'religiao': 'inteligencia', 'sobrevivencia': 'sabedoria'
};

for (let i = 0; i < pericias.length; i++) {
    const pericia = pericias[i];
    const atributo_base = relacao[pericia];
    
    let mod_base = parseInt(atr[atributo_base].textContent) || 0;
    
    let total_pericia = check_peri[pericia].checked ? (mod_base + prof_bonus_value) : mod_base;
    
    peri_[pericia].textContent = total_pericia;
}

const tabelaXP = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000];

// Calculo nivel
let nivel = 1;
for (let i = 0; i < tabelaXP.length; i++) {
    if (exp_value >= tabelaXP[i]) {
        nivel = i + 1;
    }
}
console.log("Nível do personagem: ", nivel);

let ca = 10 + parseInt(atr['destreza'].textContent);
ca_value.textContent = ca;

let ini = parseInt(atr['destreza'].textContent);
ini_value.textContent = ini;

let deslocamento = 9;
desl_value.textContent = deslocamento;


//Calculo vida
let i_pv = parseInt(input_i_pv.value);
let pv = parseInt(max_pv.value);
let consti = parseInt(atr['constituicao'].textContent);

while (i_pv < nivel){
    if (i_pv === 0){
        if (dpv.value.includes("d")){
            let max_rollpv = dpv.value.toLowerCase().split('d')
            // Correção de segurança no parse
            let faces = parseInt(max_rollpv[1]) || 0;
            pv += faces + consti;
        }
        else{
            pv += (parseInt(dpv.value) || 0) + consti
        }
    }
    else{
        let rollResult = rolls(dpv.value);
        pv += (parseInt(rollResult[0]) || 0) + consti;
    }
    i_pv++
    console.log(`Nível ${i_pv}: PV total: ${pv}`);
}

if (pv !== parseInt(max_pv.value) || parseInt(input_i_pv.value) !== i_pv){
    max_pv.value = pv
    input_i_pv.value = i_pv 

}

console.log(atual_pv.textContent)
temp_pv.textContent = atual_pv.textContent - pv

// Salva morte
const checksSucesso = document.querySelectorAll('.check-sucesso');
const checksFalha = document.querySelectorAll('.check-falha');
const inputSucessos = document.getElementById('input_sucessos');
const inputFalhas = document.getElementById('input_falhas');
const inputMorteStatus = document.getElementById('input_morte_status');

function calcularMorte() {
    const qtdSucessos = document.querySelectorAll('.check-sucesso:checked').length;
    const qtdFalhas = document.querySelectorAll('.check-falha:checked').length;
    
    if(inputSucessos) inputSucessos.value = qtdSucessos;
    if(inputFalhas) inputFalhas.value = qtdFalhas;

    if (qtdFalhas >= 3) {
        if(inputMorteStatus) inputMorteStatus.value = "True";
        form.requestSubmit();
    } else {
        if(inputMorteStatus) inputMorteStatus.value = "False";
    }
}

checksSucesso.forEach(box => box.addEventListener('change', calcularMorte));
checksFalha.forEach(box => box.addEventListener('change', calcularMorte));

// Habilidades
let btn_ataque = document.querySelectorAll(".btn_ataque");
btn_ataque.forEach(btn => {
    btn.addEventListener('click', () => ataque(btn));
});

function ataque(btn_ataque){
    let ataque_id = btn_ataque.getAttribute('data-id');
    let acerto = document.getElementById("acerto" + ataque_id);
    let dano = document.getElementById("dano" + ataque_id);

    let acerto_res = document.getElementById("acerto_res" + ataque_id);
    let dano_res = document.getElementById("dano_res" + ataque_id);
    
    if(acerto && acerto_res) acerto_res.textContent = rolls(acerto.textContent);
    if(dano && dano_res) dano_res.textContent = rolls(dano.textContent);
};

itens.forEach(item => {
    console.log(".")
    let atr_mod = item.getAttribute('data-target');
    let mod = item.getAttribute('data-mod');
    console.log("Atributo modificado: ", atr_mod, "Modificador: ", mod);
    if (atr_mod.includes("brut")){
        console.log("Brut")
    }
    else if (atr_mod.includes("salva")){
        atr_mod = atr_mod.replace("salva", "");
        console.log("Salva:" , salva[atr_mod].textContent, "Mod: ", mod);
        mod = salva[atr_mod].textContent + mod;
        console.log("Salva total: ", mod);
        mod = new Function('return ' + mod)();
        console.log("Salva total: ", mod);
        console.log("Atributo modificado: ", atr_mod, "Modificador: ", mod);
        salva[atr_mod].textContent = mod;
    }
    else if (atr_mod.includes("peri")){
        atr_mod = atr_mod.replace("peri", "");
        console.log("Pericia:" , peri_[atr_mod].textContent, "Mod: ", mod);
        mod = peri_[atr_mod].textContent + mod;
        console.log("Pericia total: ", mod);
        mod = new Function('return ' + mod)();
        console.log("Pericia total: ", mod);
        console.log("Atributo modificado: ", atr_mod, "Modificador: ", mod);
        peri_[atr_mod].textContent = mod;
    }
    else{
        console.log("None")
    };
});


itens.forEach(item => {
    let target = item.getAttribute('data-target'); 
    let mod = item.getAttribute('data-mod');

    if (!target) return; 

    try {
        if (target.includes("peri") || pericias.includes(target.replace("peri_", ""))) {
            let chave = target.replace("peri_", "").replace("peri", "");
            if (peri_[chave]) {
                let base = parseInt(peri_[chave].textContent) || 0;
                peri_[chave].textContent = Math.floor(eval(base + mod));
            }
        } 
        else if (target.includes("salva") || atributos.includes(target.replace("salva_", ""))) {
            if (!modificadores[target]) {
                modificadores[target] = "";
            }
            modificadores[target] += mod;
            for (let atr_mod in modificadores) {
                let atr_mod_clean = atr_mod.replace("salva", "");
                let valorbase = parseInt(salva[atr_mod_clean].textContent) || 0;
                let equacaoFinal = valorbase + modificadores[atr_mod];
                let resultado = new Function('return ' + equacaoFinal)();
                salva[atr_mod_clean].textContent = Math.floor(resultado);
                console.log(`Cálculo final de salva ${atr_mod_clean}: ${equacaoFinal} = ${Math.floor(resultado)}`);
            }
        }

        else if (target === "ca" || target === "ca_value") {
            let base = parseInt(ca_value.textContent) || 0;
            ca_value.textContent = Math.floor(eval(base + mod));
        }
        else if (target === "iniciativa" || target === "ini_value") {
            let base = parseInt(ini_value.textContent) || 0;
            ini_value.textContent = Math.floor(eval(base + mod));
        }
        else if (target === "deslocamento" || target === "desl_value") {
            let base = parseInt(desl_value.textContent) || 0;
            desl_value.textContent = Math.floor(eval(base + mod));
        }
        else if (target === "max_pv") {
            let base = parseInt(max_pv.value) || 0;
            max_pv.value = Math.floor(eval(base + mod));
        }
    } catch (e) {
        console.log("Erro no item: " + target);
    }
});