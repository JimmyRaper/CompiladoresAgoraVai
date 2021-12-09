
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIDnonassocABRE_PARENTESEABRE_COLCHETE ABRE_PARENTESE ATE ATRIBUICAO DIFERENCA DIVISAO DOIS_PONTOS ENTAO ESCREVA E_LOGICO FECHA_COLCHETE FECHA_PARENTESE FIM FLUTUANTE ID IGUAL INTEIRO LEIA MAIOR MAIOR_IGUAL MAIS MENOR MENOR_IGUAL MENOS MULTIPLICACAO NEGACAO NUM_INTEIRO NUM_NOTACAO_CIENTIFICA NUM_PONTO_FLUTUANTE OU_LOGICO REPITA RETORNA SE SENAO VIRGULA\n    programa : lista_declaracoes\n    \n    lista_declaracoes : lista_declaracoes declaracao\n                     | declaracao\n    \n    declaracao : declaracao_variaveis\n                | inicializacao_variaveis\n                | declaracao_funcao\n    \n    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n    \n    inicializacao_variaveis : atribuicao\n    \n    lista_variaveis : lista_variaveis VIRGULA var\n                            | var\n    \n    var : ID\n        | ID indice\n    \n    indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE\n            | ABRE_COLCHETE expressao FECHA_COLCHETE\n    \n    tipo : INTEIRO\n        | FLUTUANTE\n    \n    declaracao_funcao : tipo cabecalho \n                    | cabecalho \n    \n    cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM\n    \n    lista_parametros : lista_parametros VIRGULA parametro\n                | parametro\n                | vazio\n    \n    parametro : tipo DOIS_PONTOS ID\n            | parametro ABRE_COLCHETE FECHA_COLCHETE\n    \n    corpo : corpo acao\n        | vazio\n    \n    acao : expressao\n        | declaracao_variaveis\n        | se\n        | repita\n        | leia\n        | escreva\n        | retorna\n    \n    se : SE expressao ENTAO corpo FIM\n          | SE expressao ENTAO corpo SENAO corpo FIM\n    \n    repita : REPITA corpo ATE expressao\n    \n    atribuicao : var ATRIBUICAO expressao\n    \n    leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE\n    \n    escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE\n    \n    retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE\n    \n    expressao : expressao_logica\n                | atribuicao\n    \n    expressao_logica : expressao_simples\n                    | expressao_logica operador_logico expressao_simples\n    \n    expressao_simples : expressao_aditiva\n                    | expressao_simples operador_relacional expressao_aditiva\n    \n    expressao_aditiva : expressao_multiplicativa\n                    | expressao_aditiva operador_soma expressao_multiplicativa\n    \n    expressao_multiplicativa : expressao_unaria\n                            | expressao_multiplicativa operador_multiplicacao expressao_unaria\n    \n    expressao_unaria : fator\n                    | operador_soma fator\n                    | operador_negacao fator\n    \n    operador_relacional : MENOR\n                        | MAIOR\n                        | IGUAL\n                        | DIFERENCA\n                        | MENOR_IGUAL\n                        | MAIOR_IGUAL\n    \n    operador_soma : MAIS\n                | MENOS\n    \n    operador_logico : E_LOGICO\n                | OU_LOGICO\n    \n    operador_negacao : NEGACAO\n    \n    operador_multiplicacao : MULTIPLICACAO\n                            | DIVISAO\n    \n        fator : ABRE_PARENTESE expressao FECHA_PARENTESE\n            | var\n            | chamada_funcao\n            | numero\n    \n    numero : NUM_INTEIRO\n        | NUM_PONTO_FLUTUANTE\n        | NUM_NOTACAO_CIENTIFICA\n    \n    chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE\n    \n    lista_argumentos : lista_argumentos VIRGULA expressao\n                    | expressao\n                    | vazio\n    \n        vazio :\n    '
    
_lr_action_items = {'NUM_NOTACAO_CIENTIFICA':([18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[26,-12,26,-11,-10,-7,-70,-73,-45,26,-60,-43,-71,26,-11,-61,-69,-51,-64,-68,-72,-42,-41,26,-47,-49,26,-37,26,-14,-58,-57,-56,-55,-59,26,-54,-52,-68,26,-62,-63,26,-53,-66,26,-65,-78,-9,-48,-67,-46,-44,-50,-26,26,-13,26,-74,-27,-31,-33,-29,-30,26,-32,-25,-28,-78,26,26,26,-78,26,-38,-39,26,-40,-36,-78,-34,26,-35,]),'VIRGULA':([19,20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,46,48,49,51,55,63,64,65,69,78,79,80,81,82,83,84,85,86,87,90,91,92,94,110,],[-78,-12,-11,-10,52,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,73,-21,-22,-37,-14,-52,-68,-78,-53,-9,-48,-67,-46,-76,93,-77,-44,-50,-20,-23,-24,-13,-74,-75,]),'MULTIPLICACAO':([20,25,26,32,34,36,37,39,40,44,45,55,63,64,69,79,80,86,92,94,],[-12,-70,-73,-71,-11,-69,-51,-68,-72,72,-49,-14,-52,-68,-53,72,-67,-50,-13,-74,]),'ESCREVA':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,100,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,100,-78,-38,-39,100,-40,-36,-78,-34,100,-35,]),'ATE':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,78,79,80,81,85,86,88,92,94,95,96,97,98,103,105,107,108,109,115,121,122,124,125,127,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-9,-48,-67,-46,-44,-50,-26,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,120,-38,-39,-40,-36,-34,-35,]),'ABRE_PARENTESE':([5,15,18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,99,100,103,104,105,106,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[19,19,28,-12,28,-11,-10,-7,-70,-73,-45,28,-60,-43,-71,28,65,-61,-69,-51,-64,-68,-72,-42,-41,28,-47,-49,28,-37,28,-14,-58,-57,-56,-55,-59,28,-54,-52,-68,28,-62,-63,28,-53,-66,28,-65,-78,-9,-48,-67,-46,-44,-50,-26,28,-13,28,-74,-27,-31,-33,-29,111,112,-30,28,-32,114,-25,-28,-78,28,28,28,-78,28,-38,-39,28,-40,-36,-78,-34,28,-35,]),'$end':([1,3,6,7,9,10,11,13,14,17,20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,78,79,80,81,85,86,92,94,101,],[-6,-1,0,-18,-3,-5,-8,-4,-2,-17,-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-9,-48,-67,-46,-44,-50,-13,-74,-19,]),'IGUAL':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,58,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,58,-50,-13,-74,]),'SE':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,104,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,104,-78,-38,-39,104,-40,-36,-78,-34,104,-35,]),'INTEIRO':([0,1,3,7,9,10,11,13,14,17,19,20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,73,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,101,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[2,-6,2,-18,-3,-5,-8,-4,-2,-17,2,-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,2,-78,-9,-48,-67,-46,-44,-50,-26,2,-13,-74,-27,-31,-33,-29,-19,-30,-32,-25,-28,-78,2,-78,-38,-39,2,-40,-36,-78,-34,2,-35,]),'MENOR_IGUAL':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,56,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,56,-50,-13,-74,]),'NUM_PONTO_FLUTUANTE':([18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[40,-12,40,-11,-10,-7,-70,-73,-45,40,-60,-43,-71,40,-11,-61,-69,-51,-64,-68,-72,-42,-41,40,-47,-49,40,-37,40,-14,-58,-57,-56,-55,-59,40,-54,-52,-68,40,-62,-63,40,-53,-66,40,-65,-78,-9,-48,-67,-46,-44,-50,-26,40,-13,40,-74,-27,-31,-33,-29,-30,40,-32,-25,-28,-78,40,40,40,-78,40,-38,-39,40,-40,-36,-78,-34,40,-35,]),'ENTAO':([20,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,79,80,81,85,86,92,94,113,],[-12,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-48,-67,-46,-44,-50,-13,-74,118,]),'NUM_INTEIRO':([18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[32,-12,32,-11,-10,-7,-70,-73,-45,32,-60,-43,-71,32,-11,-61,-69,-51,-64,-68,-72,-42,-41,32,-47,-49,32,-37,32,-14,-58,-57,-56,-55,-59,32,-54,-52,-68,32,-62,-63,32,-53,-66,32,-65,-78,-9,-48,-67,-46,-44,-50,-26,32,-13,32,-74,-27,-31,-33,-29,-30,32,-32,-25,-28,-78,32,32,32,-78,32,-38,-39,32,-40,-36,-78,-34,32,-35,]),'RETORNA':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,106,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,106,-78,-38,-39,106,-40,-36,-78,-34,106,-35,]),'MAIOR':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,59,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,59,-50,-13,-74,]),'FECHA_COLCHETE':([20,25,26,27,30,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,76,77,79,80,81,85,86,92,94,],[-12,-70,-73,-45,55,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,91,92,-48,-67,-46,-44,-50,-13,-74,]),'MENOR':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,62,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,62,-50,-13,-74,]),'ID':([0,1,2,3,4,7,8,9,10,11,13,14,16,17,18,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,101,103,104,105,107,108,109,111,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[5,-6,-15,5,15,-18,-16,-3,-5,-8,-4,-2,22,-17,34,-12,34,-11,-10,-7,-70,-73,-45,34,-60,-43,-71,34,-11,-61,-69,-51,-64,-68,-72,-42,-41,34,-47,-49,34,-37,22,34,-14,-58,-57,-56,-55,-59,34,-54,-52,-68,34,-62,-63,34,-53,-66,34,-65,-78,90,-9,-48,-67,-46,-44,-50,-26,34,-13,34,-74,-27,-31,-33,-29,-19,-30,34,-32,-25,-28,-78,22,34,34,34,-78,34,-38,-39,34,-40,-36,-78,-34,34,-35,]),'MENOS':([18,20,21,22,23,24,25,26,27,28,29,31,32,34,35,36,37,39,40,41,42,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[35,-12,35,-11,-10,-7,-70,-73,35,35,-60,-43,-71,-11,-61,-69,-51,-68,-72,-42,-41,-47,-49,35,-37,35,-14,-58,-57,-56,-55,-59,35,-54,-52,-68,35,-62,-63,35,-53,-66,35,-65,-78,-9,-48,-67,35,-44,-50,-26,35,-13,35,-74,-27,-31,-33,-29,-30,35,-32,-25,-28,-78,35,35,35,-78,35,-38,-39,35,-40,-36,-78,-34,35,-35,]),'FIM':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,101,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,-38,-39,127,-40,-36,-78,-34,129,-35,]),'DIVISAO':([20,25,26,32,34,36,37,39,40,44,45,55,63,64,69,79,80,86,92,94,],[-12,-70,-73,-71,-11,-69,-51,-68,-72,70,-49,-14,-52,-68,-53,70,-67,-50,-13,-74,]),'FLUTUANTE':([0,1,3,7,9,10,11,13,14,17,19,20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,73,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,101,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[8,-6,8,-18,-3,-5,-8,-4,-2,-17,8,-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,8,-78,-9,-48,-67,-46,-44,-50,-26,8,-13,-74,-27,-31,-33,-29,-19,-30,-32,-25,-28,-78,8,-78,-38,-39,8,-40,-36,-78,-34,8,-35,]),'ABRE_COLCHETE':([5,20,22,34,48,55,87,90,91,92,],[18,50,18,18,76,-14,76,-23,-24,-13,]),'DOIS_PONTOS':([2,4,8,47,102,],[-15,16,-16,75,16,]),'NEGACAO':([18,20,21,22,23,24,25,26,27,28,29,31,32,34,35,36,37,39,40,41,42,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[38,-12,38,-11,-10,-7,-70,-73,-45,38,-60,-43,-71,-11,-61,-69,-51,-68,-72,-42,-41,-47,-49,38,-37,38,-14,-58,-57,-56,-55,-59,38,-54,-52,-68,38,-62,-63,38,-53,-66,38,-65,-78,-9,-48,-67,-46,-44,-50,-26,38,-13,38,-74,-27,-31,-33,-29,-30,38,-32,-25,-28,-78,38,38,38,-78,38,-38,-39,38,-40,-36,-78,-34,38,-35,]),'OU_LOGICO':([20,25,26,27,31,32,34,36,37,39,40,42,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,67,-47,-49,-14,-52,-68,-53,-48,-67,-46,-44,-50,-13,-74,]),'FECHA_PARENTESE':([19,20,22,25,26,27,31,32,34,36,37,39,40,41,42,44,45,46,48,49,51,54,55,63,64,65,69,79,80,81,82,83,84,85,86,87,90,91,92,94,110,116,117,119,],[-78,-12,-11,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,74,-21,-22,-37,80,-14,-52,-68,-78,-53,-48,-67,-46,-76,94,-77,-44,-50,-20,-23,-24,-13,-74,-75,121,122,124,]),'MAIS':([18,20,21,22,23,24,25,26,27,28,29,31,32,34,35,36,37,39,40,41,42,44,45,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,78,79,80,81,85,86,88,89,92,93,94,95,96,97,98,103,104,105,107,108,109,112,114,115,118,120,121,122,123,124,125,126,127,128,129,],[29,-12,29,-11,-10,-7,-70,-73,29,29,-60,-43,-71,-11,-61,-69,-51,-68,-72,-42,-41,-47,-49,29,-37,29,-14,-58,-57,-56,-55,-59,29,-54,-52,-68,29,-62,-63,29,-53,-66,29,-65,-78,-9,-48,-67,29,-44,-50,-26,29,-13,29,-74,-27,-31,-33,-29,-30,29,-32,-25,-28,-78,29,29,29,-78,29,-38,-39,29,-40,-36,-78,-34,29,-35,]),'ATRIBUICAO':([5,12,20,34,39,55,92,],[-11,21,-12,-11,21,-14,-13,]),'SENAO':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,78,79,80,81,85,86,88,92,94,95,96,97,98,103,105,107,108,118,121,122,123,124,125,127,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-9,-48,-67,-46,-44,-50,-26,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,-38,-39,126,-40,-36,-34,-35,]),'DIFERENCA':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,57,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,57,-50,-13,-74,]),'MAIOR_IGUAL':([20,25,26,27,31,32,34,36,37,39,40,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,60,-71,-11,-69,-51,-68,-72,-47,-49,-14,-52,-68,-53,-48,-67,-46,60,-50,-13,-74,]),'E_LOGICO':([20,25,26,27,31,32,34,36,37,39,40,42,44,45,55,63,64,69,79,80,81,85,86,92,94,],[-12,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,66,-47,-49,-14,-52,-68,-53,-48,-67,-46,-44,-50,-13,-74,]),'LEIA':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,99,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,99,-78,-38,-39,99,-40,-36,-78,-34,99,-35,]),'REPITA':([20,22,23,24,25,26,27,31,32,34,36,37,39,40,41,42,44,45,51,55,63,64,69,74,78,79,80,81,85,86,88,89,92,94,95,96,97,98,103,105,107,108,109,115,118,121,122,123,124,125,126,127,128,129,],[-12,-11,-10,-7,-70,-73,-45,-43,-71,-11,-69,-51,-68,-72,-42,-41,-47,-49,-37,-14,-52,-68,-53,-78,-9,-48,-67,-46,-44,-50,-26,109,-13,-74,-27,-31,-33,-29,-30,-32,-25,-28,-78,109,-78,-38,-39,109,-40,-36,-78,-34,109,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressao_aditiva':([18,21,28,50,61,65,68,89,93,104,112,114,115,120,123,128,],[27,27,27,27,81,27,27,27,27,27,27,27,27,27,27,27,]),'operador_multiplicacao':([44,79,],[71,71,]),'declaracao_funcao':([0,3,],[1,1,]),'leia':([89,115,123,128,],[96,96,96,96,]),'operador_relacional':([31,85,],[61,61,]),'indice':([5,22,34,],[20,20,20,]),'retorna':([89,115,123,128,],[97,97,97,97,]),'escreva':([89,115,123,128,],[105,105,105,105,]),'lista_variaveis':([16,],[24,]),'expressao':([18,21,28,50,65,89,93,104,112,114,115,120,123,128,],[30,51,54,77,82,95,110,113,117,119,95,125,95,95,]),'numero':([18,21,28,33,43,50,53,61,65,68,71,89,93,104,112,114,115,120,123,128,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'lista_declaracoes':([0,],[3,]),'vazio':([19,65,74,109,118,126,],[49,84,88,88,88,88,]),'operador_soma':([18,21,27,28,50,53,61,65,68,71,81,89,93,104,112,114,115,120,123,128,],[33,33,53,33,33,33,33,33,33,33,53,33,33,33,33,33,33,33,33,33,]),'tipo':([0,3,19,73,89,115,123,128,],[4,4,47,47,102,102,102,102,]),'corpo':([74,109,118,126,],[89,115,123,128,]),'parametro':([19,73,],[48,87,]),'lista_argumentos':([65,],[83,]),'repita':([89,115,123,128,],[103,103,103,103,]),'operador_logico':([42,],[68,]),'se':([89,115,123,128,],[98,98,98,98,]),'programa':([0,],[6,]),'declaracao_variaveis':([0,3,89,115,123,128,],[13,13,108,108,108,108,]),'chamada_funcao':([18,21,28,33,43,50,53,61,65,68,71,89,93,104,112,114,115,120,123,128,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'fator':([18,21,28,33,43,50,53,61,65,68,71,89,93,104,112,114,115,120,123,128,],[37,37,37,63,69,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'var':([0,3,16,18,21,28,33,43,50,52,53,61,65,68,71,89,93,104,111,112,114,115,120,123,128,],[12,12,23,39,39,39,64,64,39,78,64,64,39,64,64,39,39,39,116,39,39,39,39,39,39,]),'declaracao':([0,3,],[9,14,]),'inicializacao_variaveis':([0,3,],[10,10,]),'expressao_simples':([18,21,28,50,65,68,89,93,104,112,114,115,120,123,128,],[31,31,31,31,31,85,31,31,31,31,31,31,31,31,31,]),'atribuicao':([0,3,18,21,28,50,65,89,93,104,112,114,115,120,123,128,],[11,11,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'expressao_logica':([18,21,28,50,65,89,93,104,112,114,115,120,123,128,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'lista_parametros':([19,],[46,]),'operador_negacao':([18,21,28,50,53,61,65,68,71,89,93,104,112,114,115,120,123,128,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'acao':([89,115,123,128,],[107,107,107,107,]),'cabecalho':([0,3,4,],[7,7,17,]),'expressao_multiplicativa':([18,21,28,50,53,61,65,68,89,93,104,112,114,115,120,123,128,],[44,44,44,44,79,44,44,44,44,44,44,44,44,44,44,44,44,]),'expressao_unaria':([18,21,28,50,53,61,65,68,71,89,93,104,112,114,115,120,123,128,],[45,45,45,45,45,45,45,45,86,45,45,45,45,45,45,45,45,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','parser.py',25),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','parser.py',39),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','parser.py',40),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','parser.py',57),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','parser.py',58),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','parser.py',59),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','parser.py',73),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','parser.py',92),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','parser.py',106),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','parser.py',107),
  ('var -> ID','var',1,'p_var','parser.py',127),
  ('var -> ID indice','var',2,'p_var','parser.py',128),
  ('indice -> indice ABRE_COLCHETE expressao FECHA_COLCHETE','indice',4,'p_indice','parser.py',147),
  ('indice -> ABRE_COLCHETE expressao FECHA_COLCHETE','indice',3,'p_indice','parser.py',148),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','parser.py',179),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','parser.py',180),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','parser.py',195),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','parser.py',196),
  ('cabecalho -> ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho','parser.py',211),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','parser.py',237),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','parser.py',238),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','parser.py',239),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','parser.py',257),
  ('parametro -> parametro ABRE_COLCHETE FECHA_COLCHETE','parametro',3,'p_parametro','parser.py',258),
  ('corpo -> corpo acao','corpo',2,'p_corpo','parser.py',276),
  ('corpo -> vazio','corpo',1,'p_corpo','parser.py',277),
  ('acao -> expressao','acao',1,'p_acao','parser.py',293),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','parser.py',294),
  ('acao -> se','acao',1,'p_acao','parser.py',295),
  ('acao -> repita','acao',1,'p_acao','parser.py',296),
  ('acao -> leia','acao',1,'p_acao','parser.py',297),
  ('acao -> escreva','acao',1,'p_acao','parser.py',298),
  ('acao -> retorna','acao',1,'p_acao','parser.py',299),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','parser.py',312),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','parser.py',313),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','parser.py',340),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','parser.py',359),
  ('leia -> LEIA ABRE_PARENTESE var FECHA_PARENTESE','leia',4,'p_leia','parser.py',376),
  ('escreva -> ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE','escreva',4,'p_escreva','parser.py',398),
  ('retorna -> RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE','retorna',4,'p_retorna','parser.py',420),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','parser.py',442),
  ('expressao -> atribuicao','expressao',1,'p_expressao','parser.py',443),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','parser.py',456),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','parser.py',457),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','parser.py',475),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','parser.py',476),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','parser.py',493),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','parser.py',494),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','parser.py',511),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','parser.py',512),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','parser.py',529),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','parser.py',530),
  ('expressao_unaria -> operador_negacao fator','expressao_unaria',2,'p_expressao_unaria','parser.py',531),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operator_relational','parser.py',553),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operator_relational','parser.py',554),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operator_relational','parser.py',555),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operator_relational','parser.py',556),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operator_relational','parser.py',557),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operator_relational','parser.py',558),
  ('operador_soma -> MAIS','operador_soma',1,'p_operador_soma','parser.py',573),
  ('operador_soma -> MENOS','operador_soma',1,'p_operador_soma','parser.py',574),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','parser.py',589),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','parser.py',590),
  ('operador_negacao -> NEGACAO','operador_negacao',1,'p_operador_negacao','parser.py',605),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',621),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',622),
  ('fator -> ABRE_PARENTESE expressao FECHA_PARENTESE','fator',3,'p_fator','parser.py',636),
  ('fator -> var','fator',1,'p_fator','parser.py',637),
  ('fator -> chamada_funcao','fator',1,'p_fator','parser.py',638),
  ('fator -> numero','fator',1,'p_fator','parser.py',639),
  ('numero -> NUM_INTEIRO','numero',1,'p_numero','parser.py',661),
  ('numero -> NUM_PONTO_FLUTUANTE','numero',1,'p_numero','parser.py',662),
  ('numero -> NUM_NOTACAO_CIENTIFICA','numero',1,'p_numero','parser.py',663),
  ('chamada_funcao -> ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE','chamada_funcao',4,'p_chamada_funcao','parser.py',677),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','parser.py',699),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','parser.py',700),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','parser.py',701),
  ('vazio -> <empty>','vazio',0,'p_vazio','parser.py',726),
]
