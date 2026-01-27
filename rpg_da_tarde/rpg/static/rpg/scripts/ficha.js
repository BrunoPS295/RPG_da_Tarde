import { rolls } from './rolls.js';

const insp = document.querySelector('[name="inspiracao"]');
const i_pv = document.querySelector('[name="i_pv"]')
const max_pv = document.querySelector('[name="max_pv"]');
const dpv = document.querySelector('[name="dado_de_vida"]');
const exp = document.querySelector('[name="experiencia"]');
let exp_value = parseInt(exp.textContent) || 0;

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

const tabelaXP = [
    0,       // Nível 1 
    300,     // Nível 2
    900,     // Nível 3
    2700,    // Nível 4
    6500,    // Nível 5
    14000,   // Nível 6
    23000,   // Nível 7
    34000,   // Nível 8
    48000,   // Nível 9
    64000,   // Nível 10
    85000,   // Nível 11
    100000,  // Nível 12
    120000,  // Nível 13
    140000,  // Nível 14
    165000,  // Nível 15
    195000,  // Nível 16
    225000,  // Nível 17
    265000,  // Nível 18
    305000,  // Nível 19
    355000   // Nível 20
];

// Calculo nivel
for (let i = 0; i < tabelaXP.length; i++) {
    if (exp_value >= tabelaXP[i]) {
        var nivel = i + 1;
    }
}
console.log("Nível do personagem: ", nivel);

for (let i = 0; i < atributos.length; i++) {
    const atributo = atributos[i];
    
    // atributos
    check_salva[atributo] = document.getElementById('check_salva_' + atributo);
    brut[atributo] = document.getElementById('brut_' + atributo);
    atr[atributo] = document.getElementById('atr_' + atributo);
    salva[atributo] = document.getElementById('salva_' + atributo);

    // Valor liquido dos atributos brutos
    atr[atributo].textContent = Math.floor((brut[atributo].value - 10)/2);
    
    salva[atributo].textContent = check_salva[atributo].checked ? Math.floor((brut[atributo].value - 10)/2) + prof_bonus_value : Math.floor((brut[atributo].value - 10)/2);
}

// pericias
let relacao = {
        'acrobacia': 'destreza',
        'arcanismo': 'inteligencia',
        'atletismo': 'forca',
        'atuacao': 'carisma',
        'enganacao': 'carisma',
        'furtividade': 'destreza',
        'historia': 'inteligencia',
        'intimidacao': 'carisma',
        'intuicao': 'sabedoria',
        'investigacao': 'inteligencia',
        'animais': 'sabedoria',
        'medicina': 'sabedoria',
        'natureza': 'inteligencia',
        'percepcao': 'sabedoria',
        'persuasao': 'carisma',
        'prestidigitacao': 'destreza',
        'religiao': 'inteligencia',
        'sobrevivencia': 'sabedoria'
    };

for (let i = 0; i < pericias.length; i++) {
    const pericia = pericias[i];
    check_peri[pericia] = document.getElementById('check_' + pericia);
    peri_[pericia] = document.getElementById(pericia);

    peri_[pericia].textContent = check_peri[pericia].checked ? Math.floor((brut[relacao[pericia]].value - 10)/2) + prof_bonus_value : Math.floor((brut[relacao[pericia]].value - 10)/2);

}

// CA, Iniciativa e Deslocamento
let ca = 10 + parseInt(atr['destreza'].textContent);
ca_value.textContent = ca;

let ini = parseInt(atr['destreza'].textContent);
ini_value.textContent = ini;

let deslocamento = 9;
desl_value.textContent = deslocamento;




//pv maximo
let dpv_value = rolls(dpv.value);

if (parseInt(i_pv.value) != nivel){
    max_pv.textContent += (parseInt(dpv_value) + parseInt(atr['constituicao'].textContent));
    i_pv.value = parseInt(i_pv.value) + 1
    console.log("indice de vida: ",i_pv.value);
    //form.requestSubmit()
}



console.log("Script carregado com sucesso!1.2");