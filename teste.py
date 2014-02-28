#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:01:34 2014

@author: bruno.arine
"""

import re

# PatternH: regex de hora
# retorno: [0] hora    [1] minuto   [2] meio minuto   [3] periodo do dia para desambiguacao
patternH = "\s(?:as|a)\s(uma|duas|[0-9]+)(?:\shora[s?]|h|\:|\se)\s*(meia|\d*)\s*(da tarde|da manha)?"

# PatternD: regex de data definida
# retorno: [0] dia    [1] mes    [2] ano
patternD = "\s(?:dia|em)\s(\d+)(?:\sde\s)?(janeiro|fevereiro|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro|\d+)?(?:\sde\s)?(\d{2,4})?"

# PatternO: regex de data ordenada (semana que vem, proximo dia util etc.)
# retorno: <a fazer>
patternO = "(?<=^proxim|que vem$).+(hora|dia util|dia|fim de semana|semana|mes|ano|segunda-feira|terca-feira|quarta-feira|quinta-feira|sexta-feira|sabado|domingo).+(que vem)?"

# Uma lista de testes
lista = ["fazer almoco as 3h da manha do dia 29 de dezembro",
         "levar lista de exercicio para o beto dia 28",
         "reuniao dia 25 as 2:30h",
         "encontro com a ana as 8 e meia dia 2 de outubro de 98",
         "concerto as 8 horas dia 7",
         "levar os 2 homens pra cadeia dia 5 de abril as 8 e 12",
         "levar o cachorro pra passear a uma e meia da manha",
         "sair com a ana dia 29 de agosto de 2015 as 9 e 50 da manha",
         "acender 7 velas a uma e meia da manha",
         "tomar banho sabado que vem"]
         
for item in lista:
    print item    
    print "H:", re.findall(patternH,item)
    print "D:", re.findall(patternD,item)
  # print "O:", re.findall(patternO,item) <-- dando erro >:(
    print ""
