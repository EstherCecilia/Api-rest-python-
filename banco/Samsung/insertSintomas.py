from models import *

sintomas = ["Tosse persistente", "Perda de peso", "Cansaço", "Febre", "Perda a sensibilidade na região afetada (ao tato, dor e temperatura)","Tosse seca","Dor de cabeça",
"Contrações musculares involuntárias","Rigidez na nuca e na mandíbula","Vômitos","Calafrios","Dores musculares e nas articulações","Fortes dores pelo corpo",
"Dor ou ardor ao urinar", "Vontade frequente para urinar","Corrimento branco-amarelado, semelhante ao pus","Dor de garganta","Aumento do fígado e baço",
"Suores noturnos","Diarreia","Candidíase oral ou genital que não passa","Manchas avermelhadas e pequenas bolinhas vermelhas ou feridas na pele","Moleza e dor no corpo",
"Coceira","Alterações de comportamento", "Espasmos ao sentir água ou vento", "Mal-estar geral","Dor de garganta","Úlceras na região dos genitais","Coceira",
"Perda de apetite","Dor ao mastigar e engolir","Verrugas genitais na vagina, pênis e ânus","Aparecimento de prurido, queimação, dor e sangramento","Dor ou rigidez nos braços e nas pernas",
"Amarelamento da pele e olhos","Urina escura","Fotofobia","Dificuldade em respirar","Corrimento nasal","Aparecimento de gânglios inchados nas axilas e pescoço"
"Dores sem causa aparente da região acometida","Aumento de volume no membro afetado e da rugosidade da pele","Inchaço na virilha","Confusão mental","Palpitações",
"Presença de vermes nas fezes","Irritabilidade","Aumento do apetite","Enjoo","Inchaço e vermelhidão no local da picada do inseto","Inchaço de um olho",
"Aumento dos gânglios linfáticos","Dores abdominais","Anemia","Indisposição","Tremores","Corrimento vaginal","Coceira vaginal e sensação de queimação","Vermelhidão genital e urgência urinária"]




for nome in sintomas:
    sintoma = Sintomas(nome=nome)
    sintoma.save()
