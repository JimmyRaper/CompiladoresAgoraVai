# -*- coding: UTF-8 -*-
import logging
logging.basicConfig(
     level = logging.DEBUG,
     filename = "log.txt",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

import ply.lex as lex
from ply.lex import TOKEN
import re


#Reserved
reserved_words = {
    'se': 'SE',
    'então': 'ENTAO',
    'senão': 'SENAO',
    'fim': 'FIM',
    'repita': 'REPITA',
    'flutuante': 'FLUTUANTE',
    'inteiro': 'INTEIRO',
    'até': 'ATE',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'retorna': 'RETORNA',
}

#Tokens
tokens = [
    "ID",  # identificador
    # numerais
    "NUM_NOTACAO_CIENTIFICA",  # ponto flutuante em notaçao científica
    "NUM_PONTO_FLUTUANTE",  # ponto flutuate
    "NUM_INTEIRO",  # inteiro
    # operadores binarios
    "MAIS",  # +
    "MENOS",  # -
    "MULTIPLICACAO",  # *
    "DIVISAO",  # /
    "E_LOGICO",  # &&
    "OU_LOGICO",  # ||
    "DIFERENCA",  # <>
    "MENOR_IGUAL",  # <=
    "MAIOR_IGUAL",  # >=
    "MENOR",  # <
    "MAIOR",  # >
    "IGUAL",  # =
    # operadores unarios
    "NEGACAO",  # !
    # simbolos
    "ABRE_PARENTESE",  # (
    "FECHA_PARENTESE",  # )
    "ABRE_COLCHETE",  # [
    "FECHA_COLCHETE",  # ]
    "VIRGULA",  # ,
    "DOIS_PONTOS",  # :
    "ATRIBUICAO",  # :=
    "COMENTARIO", # {***}
] + list(reserved_words.values())

#Regular expressions

digito = r"([0-9])"
letra = r"([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])"
sinal = r"([\-\+]?)"

""" 
    id deve começar com uma letra
"""
id = (
    r"(" + letra + r"(" + digito + r"+|_|" + letra + r")*)"
)  # o mesmo que '((letra)(letra|_|([0-9]))*)'

# inteiro = r"(" + sinal + digito + r"+)"
# inteiro = r"(" + digito + r"+)"
inteiro = r"\d+"

flutuante = (
    # r"(" + digito + r"+\." + digito + r"+?)"
    # (([-\+]?)([0-9]+)\.([0-9]+))'
    r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d*)([eE][-+]?\d+)?'
    # r'[-+]?[0-9]+(\.([0-9]+)?)'
    #r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    #r"(([-\+]?)([0-9]+)\.([0-9]+))"
    )

notacao_cientifica = (
    r"(" + sinal + r"([1-9])\." + digito + r"+[eE]" + sinal + digito + r"+)"
)  # o mesmo que '(([-\+]?)([1-9])\.([0-9])+[eE]([-\+]?)([0-9]+))'

# Expressões Regulaes para tokens simples.
# Símbolos.
t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_VIRGULA = r','
t_ATRIBUICAO = r':='
t_DOIS_PONTOS = r':'

# Operadores Lógicos.
t_E_LOGICO = r'&&'
t_OU_LOGICO = r'\|\|'
t_NEGACAO = r'!'

# Operadores Relacionais.
t_DIFERENCA = r'<>'
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'='

@TOKEN(id)
def t_ID(token):
    token.type = reserved_words.get(
        token.value, "ID"
    )  # não é necessário fazer regras/regex para cada palavra reservada
    # se o token não for uma palavra reservada automaticamente é um id
    # As palavras reservadas têm precedências sobre os ids

    return token

@TOKEN(notacao_cientifica)
def t_NUM_NOTACAO_CIENTIFICA(token):
    return token

@TOKEN(flutuante)
def t_NUM_PONTO_FLUTUANTE(token):
    return token

@TOKEN(inteiro)
def t_NUM_INTEIRO(token):
    return token

t_ignore = " \t"

# Comments
def t_COMENTARIO(token):
    r"(\{((.|\n)*?)\})"
    token.lexer.lineno += token.value.count("\n")
    return token

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def define_column(input, lexpos):
    begin_line = input.rfind("\n", 0, lexpos) + 1
    return (lexpos - begin_line) + 1


def t_error(t):

    # file = token.lexer.filename
    line = t.lineno
    # column = define_column(token.lexer.backup_data, token.lexpos)
    message = "Caracter ilegal '%s'" % t.value[0]

    # print(f"[{file}]:[{line},{column}]: {message}.") 
    print(message)

    t.lexer.skip(1)

    # token.lexer.has_error = Trueb

lexer = lex.lex()

def analyzer(data_file):
    global lexer

    lexer.input(data_file)

    tokens_list = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens_list.append(token)
    
    lexer = lex.lex()
    return tokens_list

if __name__ == '__main__':
    pass