const insp = document.querySelector('[name="inspiracao"]');
const max_pv = document.querySelector('[name="max_pv"]');
const dpv = document.querySelector('[name="dado_de_vida"]');
const exp = document.querySelector('[name="exp"]');
let prof_bonus = document.getElementById('prof_bonus');
prof_bonus = parseInt(prof_bonus.value) || 0;

atributos = ['forca','destreza','constituicao','inteligencia','sabedoria','carisma'];

pericias = ['acrobacia','arcanismo','atletismo','atuacao','enganacao','furtividade','historia','intimidacao','intuicao','investigacao','animais','medicina','natureza','percepcao','persuasao','prestidigitacao','religiao','sobrevivencia'];

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

// Valor liquido dos atributos brutos
for (let i = 0; i < atributos.length; i++) {
    const atributo = atributos[i];
    atr[atributo].textContent = Math.floor((brut[atributo].value - 10)/2);
    salva[atributo].textContent = check_salva[atributo].checked ? Math.floor((brut[atributo].value - 10)/2) + parseInt(prof_bonus.textContent) : Math.floor((brut[atributo].value - 10)/2);
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

    peri_[pericia].textContent = check_peri[pericia].checked ? Math.floor((brut[relacao[pericia]].value - 10)/2) + prof_bonus : Math.floor((brut[relacao[pericia]].value - 10)/2);

}



console.log("Script carregado com sucesso!1.0");


