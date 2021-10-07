# -*- coding: UTF-8 -*-
import ply.lex as lex
import re


#Reserved
reserved = {
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
    'ID',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'IGUALDADE',
    'VIRGULA',
    'ATRIBUICAO',
    'MENOR',
    'MAIOR',
    'MENOR_IGUAL',
    'MAIOR_IGUAL',
    'ABRE_PAR',
    'FECHA_PAR',
    'DOIS_PONTOS',
    'ABRE_COL',
    'FECHA_COL',
    'E_LOGICO',
    'OU_LOGICO',
    'NEGACAO',
    'DIFERENTE',
    'NUM_INTEIRO',
    'NUM_PONTO_FLUTUANTE',
    'NUM_NOTACAO_CIENTIFICA',
    'COMENTARIO',
] + list(reserved.values())

#Regular expressions
t_ignore = ' \t'

def t_ID(t):
    r'[a-zà-úA-ZÀ-Ú_][a-zà-úA-ZÀ-Ú0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


def t_SOMA(t):
    r'\+'
    return t


def t_SUBTRACAO(t):
    r'\-'
    return t


def t_MULTIPLICACAO(t):
    r'\*'
    return t


def t_DIVISAO(t):
    r'/'
    return t


def t_IGUALDADE(t):
    r'\='
    return t


def t_VIRGULA(t):
    r','
    return t


def t_ATRIBUICAO(t):
    r':='
    return t


def t_MENOR(t):
    r'<'
    return t


def t_MAIOR(t):
    r'>'
    return t


def t_MENOR_IGUAL(t):
    r'<='
    return t


def t_MAIOR_IGUAL(t):
    r'>='
    return t


def t_ABRE_PAR(t):
    r'\('
    return t


def t_FECHA_PAR(t):
    r'\)'
    return t


def t_DOIS_PONTOS(t):
    r':'
    return t


def t_ABRE_COL(t):
    r'\['
    return t


def t_FECHA_COL(t):
    r'\]'
    return t


def t_E_LOGICO(t):
    r'\&\&'
    return t


def t_OU_LOGICO(t):
    r'\|\|'
    return t


def t_NEGACAO(t):
    r'!'
    return t


def t_DIFERENTE(t):
    r'<>'
    return t


def t_NUM_INTEIRO(t):
    r'[0-9]+'
    return t

def t_NUM_PONTO_FLUTUANTE(t):
    r'([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)'
    return t


def t_NUM_NOTACAO_CIENTIFICA(t):
    r'([0-9]+(\.[0-9]+)?|\.[0-9]+|\.|[0-9]+)([eE][-+]? [0-9]+)'
    return t

# Comments
def t_COMENTARIO(t):
    r'{[^(})]*}'
    lineCount = re.findall('\n', t.value)
    t.lexer.lineno += len(lineCount)
    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise Exception("Illegal character '{}' (linha {})".format(t.value[0], t.lineno))

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