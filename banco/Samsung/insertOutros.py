from models import *

transmissaos= ["Contato sexual", "Contato direto com a pessoa ou objeto contaminado", "Picada de mosquitos", "O vírus pode ser transmitido pelo ar por meio de gotículas que escapam quando uma pessoa infectada tosse, espirra ou fala", "Contato direto com a saliva e/ou lábios de pessoas contaminados", "Contato com fluidos corporais", "São transmitidas por contaminação sanguínea, ou seja, pelo uso compartilhado de materiais cortantes, como agulhas, aparelhos de barbear e alicates de unha", "Ingestão de alimentos contaminados", "Fezes do barbeiro", "Ingestão de água e/ou alimentos contaminados", "Ingestão de carne de porco contaminada com larvas", "Penetração da larva através da pele", "Consumo de água e/ou alimentos contaminados com ovos", "Ingestão de ovos", "Urina de rato contaminada", "Picada de pernilongo", "Ferimentos ou lesões na pele"]
prevencaos=["Uso de presevartivos", "Identificação e tratamento dos doentes", "Tomar cuidado ao estar em ambientes com possível contaminação", 
"Educação sanitária", "Lavar e cozinhar bem os alimentos", "Ingerir apenas água tratada", "Vacina", "Medicamentos antivirais", "Tratada naturalmente pelo organismo", "Combate ao inseto transmissor", "Condições habitacionais adequadas", "Combate aos mosquitos", "Uso de presevartivos", "Cozinhar bem as carnes", "Evitar banho em lagoas com caramujo", "Lavar bem os alimentos"]

for nome in prevencaos:
    prevencao = Prevencoes(nome=nome)
    prevencao.save()

for nome in transmissaos:
    transmissao = Transmicaos(nome=nome)
    transmissao.save()
