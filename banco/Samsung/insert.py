# -*- coding: cp1252 -*-

from models import *

doencas = [
{"nome":"AIDS", "agente":"HIV", "tipo":"VIRUS", "sintomas":[1, 3, 5, 6, 11, 18, 19, 20, 21], "prevencao":[0,1], "transmicao":[0]},
{"nome":"MENIGINTE", "agente":"ENTEROVÍRUS-ARBOVÍRUS-OUTROS", "tipo":"VIRUS", "sintomas":[6,8,9], "prevencao":[2], "transmicao":[1]},
{"nome":"DENGUE", "agente":"AEDES AEGYPTI", "tipo":"VIRUS", "sintomas":[2, 3, 6, 9, 11, 21, 22], "prevencao":[3,1,4,5], "transmicao":[15]},
{"nome":"ZYKA VÍRUS", "agente":"AEDES AEGYPTI", "tipo":"VIRUS", "sintomas":[3, 6, 11, 22, 23], "prevencao":[1,3,4,5], "transmicao":[15]},
{"nome":"VARÍOLA", "agente":"ORTHOPOXVIRUS", "tipo":"VIRUS", "sintomas":[2, 3, 6, 9, 12], "prevencao":[1,6], "transmicao":[3]},
{"nome":"RAIVA", "agente":"LYSSAVIRUS", "tipo":"VIRUS", "sintomas":[3, 24, 25, 26, 27], "prevencao":[6], "transmicao":[3]},
{"nome":"HERPES", "agente":"HERPES SIMPLEX", "tipo":"VIRUS", "sintomas":[12, 21, 28], "prevencao":[7], "transmicao":[4]},
{"nome":"EBOLA", "agente":"FILOVIRUS", "tipo":"VIRUS", "sintomas":[3, 9, 12, 19, 22], "prevencao":[1], "transmicao":[5]},
{"nome":"CAXUMBA", "agente":"PARAMIXOVÍRUS", "tipo":"VIRUS", "sintomas":[3, 6, 22, 30, 31], "prevencao":[8], "transmicao":[4]},
{"nome":"HPV", "agente":"PAPILOMA VÍRUS HUMANO", "tipo":"VIRUS", "sintomas":[32, 33], "prevencao":[1,12], "transmicao":[0]},
{"nome":"POLIOMELITE", "agente":"POLIOVÍRUS", "tipo":"VIRUS", "sintomas":[3,  6,  12,  22,  27, 34], "prevencao":[1,6], "transmicao":[4]},
{"nome":"HEPATITE", "agente":"HAV-HNV-HDV", "tipo":"VIRUS", "sintomas":[3, 12, 22,  30, 35, 36], "prevencao":[7], "transmicao":[6]},
{"nome":"FEBRE AMARELA", "agente":"ARN", "tipo":"VIRUS", "sintomas":[3, 6, 12, 22, 30, 37, 38], "prevencao":[6,1, 3], "transmicao":[2]},
{"nome":"CHAGAS", "agente":"TRIPONOSSOMA CRUZI", "tipo":"PROTOZOARIOS", "sintomas":[6, 9, 19, 26, 50, 51 ], "prevencao":[9, 10], "transmicao":[8]},
{"nome":"TOXOPLASMOSE", "agente":"TOXOPLASMA GONDII", "tipo":"PROTOZOARIOS", "sintomas":[3, 16, 52, 53 ], "prevencao":[3,1,5], "transmicao":[7]},
{"nome":"LEISHMANIOSE", "agente":"LEISSHMANIA", "tipo":"PROTOZOARIOS", "sintomas":[1, 3, 30, 54, 55 ], "prevencao":[1,9], "transmicao":[2]},
{"nome":"MALÁRIA", "agente":"PLASMODIUM", "tipo":"PROTOZOARIOS", "sintomas":[3, 6, 18,  56 ], "prevencao":[1,9], "transmicao":[2]},
{"nome":"TRICOMONÍASE", "agente":"TRICHOMONAS VAGINALIS", "tipo":"PROTOZOARIOS", "sintomas":[58, 59, 60], "prevencao":[0,1], "transmicao":[1]},
{"nome":"GARDÍASE", "agente":"GIARDIA LAMBLIA", "tipo":"PROTOZOARIOS", "sintomas":[3, 6, 18, 56], "prevencao":[1,4], "transmicao":[7]},
{"nome":"TENIASE", "agente":"TAENIA SOLIUM", "tipo":"PLATELMINTOS E NEMATELMINTOS", "sintomas":[3, 6, 11, 19, 30, 47, 48, 49], "prevencao":[4,13], "transmicao":[10]},
{"nome":"ESQUISTOSSOMOSE", "agente":"SCHISTOSOMA MANSONI", "tipo":"PLATELMINTOS E NEMATELMINTOS", "sintomas":[0, 2, 3, 6, 10, 26,30], "prevencao":[3,1,4,5], "transmicao":[11]},
{"nome":"LOMBRIGA", "agente":"ASCARIS LUMBRICOIDE", "tipo":"PLATELMINTOS E NEMATELMINTOS", "sintomas":[9, 12, 19, 22, 46], "prevencao":[3,1,4,5], "transmicao":[9]},
{"nome":"CISTICERCOSE", "agente":"TAENIA SOLIUM", "tipo":"PLATELMINTOS E NEMATELMINTOS", "sintomas":[6, 11, 44, 45], "prevencao":[4,13], "transmicao":[13]},
{"nome":"ELEFANTISES", "agente":"WUCHERERIA BANCROFTI", "tipo":"PLATELMINTOS E NEMATELMINTOS", "sintomas":[3, 11, 21, 26, 41, 42, 43], "prevencao":[1,11], "transmicao":[2]},
{"nome":"TUBERCULOSE", "agente":"MYCOBACTERIUM TUBERCULOSIS", "tipo":"BACTERIAS", "sintomas":[0, 1, 2, 3], "prevencao":[6,1,4], "transmicao":[1]},
{"nome":"LEPRA", "agente":"MYCOBACTERIUM LEPRAE", "tipo":"BACTERIAS", "sintomas":[4, 21], "prevencao":[1,4], "transmicao":[1]},
{"nome":"DIFTERIA", "agente":"BORTELA PERTUSSIS", "tipo":"BACTERIAS", "sintomas":[3, 16, 26, 38,39], "prevencao":[4,6], "transmicao":[1]},
{"nome":"COQUELUCHE", "agente":"CORYNEBACTERIUM DIPHTHERIAE", "tipo":"BACTERIAS", "sintomas":[0,5], "prevencao":[4,6], "transmicao":[1]},
{"nome":"TÉTANO", "agente":"CLOSTRIDIUM TETANI", "tipo":"BACTERIAS", "sintomas":[3, 7,8], "prevencao":[4,6], "transmicao":[16]},
{"nome":"MENIGINTE CÓCITA", "agente":"MENINGOCOCO", "tipo":"BACTERIAS", "sintomas":[3, 8,9], "prevencao":[4,6], "transmicao":[1]},
{"nome":"GONORREIA", "agente":"NEISSERIA GONORRHEAGE", "tipo":"BACTERIAS", "sintomas":[3, 13, 14 , 15,16], "prevencao":[0,1], "transmicao":[0]},
{"nome":"SIFILIS", "agente":"TREPONEMA POLIDIUM", "tipo":"BACTERIAS", "sintomas":[3, 11, 21, 27, 31,40], "prevencao":[1,4,6], "transmicao":[0]},
{"nome":"LEPTOSPIROSE", "agente":"LEPTOSPIRA INTERROGANS", "tipo":"BACTERIAS", "sintomas":[3, 10,11], "prevencao":[4, 15], "transmicao":[14]},
               ]
for d in doencas:
    doenca = Doencas(nome=d['nome'], tipo=d['tipo'], agente=d['agente'], sintomas=[], prevencao=[], transmicao=[])
    doenca.save()
    for s in d['sintomas']:
        sintoma = Sintomas.query.all()
        try:
            doenca.sintomas.append(sintoma[s])
            doenca.save()
        except IndexError:
            print("Error")
    
    for p in d['prevencao']:
        prevencaos = Prevencoes.query.all()
        doenca.prevencao.append(prevencaos[p])
        doenca.save()

    for t in d['transmicao']:
        transmicaos = Transmicaos.query.all()
        doenca.transmicao.append(transmicaos[t])
        doenca.save()


