# -*- coding: utf-8 -*-
import ply.yacc as yacc
from lexical import tokens
from anytree import Node
import logging

logging.basicConfig(
     level = logging.DEBUG,
     filename = "log-parser.txt",
     filemode = "w",
     format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

index_node = 0
has_success = True

precedence = (
    ("nonassoc", "ID"),
    ("nonassoc", "ABRE_PARENTESE"),
)

def p_programa(p):
    '''
    programa : lista_declaracoes
    '''

    global index_node
    
    root = Node(str(index_node), value='programa')
    index_node += 1

    p[1].parent = root
    p[0] = root


def p_lista_declaracoes(p):
    '''
    lista_declaracoes : lista_declaracoes declaracao
                     | declaracao
    '''

    global index_node
    
    pai = Node(str(index_node), value='lista_declaracoes')
    index_node += 1
    
    p[1].parent = pai
    
    if (len(p) == 3):
        p[2].parent = pai

    p[0] = pai

def p_declaracao(p):
    '''
    declaracao : declaracao_variaveis
                | inicializacao_variaveis
                | declaracao_funcao
    '''

    global index_node
    
    pai = Node(str(index_node), value='declaracao')
    index_node += 1

    p[1].parent = pai
    p[0] = pai


def p_declaracao_variaveis(p):
    '''
    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    '''

    global index_node
    
    pai = Node(str(index_node), value='declaracao_variaveis')
    index_node += 1

    p[1].parent = pai

    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    
    p[3].parent = pai

    p[0] = pai

def p_inicializacao_variaveis(p):
    '''
    inicializacao_variaveis : atribuicao
    '''

    global index_node
    
    pai = Node(str(index_node), value='inicializacao_variaveis')
    index_node += 1
    
    p[1].parent = pai

    p[0] = pai

def p_lista_variaveis(p):
    '''
    lista_variaveis : lista_variaveis VIRGULA var
                            | var
    '''

    global index_node

    pai = Node(str(index_node), value='lista_variaveis')
    index_node += 1

    if(len(p) == 4):
        p[1].parent = pai
        Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
        index_node += 1
        p[3].parent = pai
    else:
        p[1].parent = pai

    p[0] = pai
    
    
def p_var(p):
    '''
    var : ID
        | ID indice
    '''

    global index_node
    
    pai = Node(str(index_node), value='var', line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    if(len(p) == 3):
        p[2].parent = pai

    p[0] = pai

def p_indice(p):
    '''
    indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
            | ABRE_COLCHETE expressao FECHA_COLCHETE
    '''

    global index_node
    
    pai = Node(str(index_node), value='indice')
    index_node += 1
    
    if(len(p) == 5):
        p[1].parent = pai
        Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
        index_node += 1
        
        p[3].parent = pai
        Node(str(index_node), pai, value=str(p[4]), line=p.lineno(4), pos=p.lexpos(4))
        index_node += 1 
    else:
        Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
        index_node += 1
        
        p[2].parent = pai
        Node(str(index_node), pai, value=str(p[3]), line=p.lineno(3), pos=p.lexpos(3))
        index_node += 1

    p[0] = pai


def p_tipo(p):
    '''
    tipo : INTEIRO
        | FLUTUANTE
    '''

    global index_node

    pai = Node(str(index_node), value="tipo")
    index_node += 1
    
    
    Node(str(index_node), value=str(p[1]), parent=pai, line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai
    

def p_declaracao_funcao(p):
    '''
    declaracao_funcao : tipo cabecalho 
                    | cabecalho 
    '''

    global index_node
    pai = Node(str(index_node), value="declaracao_funcao")
    index_node += 1

    p[1].parent = pai

    if(len(p) == 3):
        p[2].parent = pai

    p[0] = pai
    

def p_cabecalho(p):
    '''
    cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM
    '''

    global index_node
    pai = Node(str(index_node), value="cabecalho")
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai
    
    Node(str(index_node), pai, value=str(p[4]), line=p.lineno(4), pos=p.lexpos(4))
    index_node += 1
    p[5].parent = pai
    
    Node(str(index_node), pai, value=str(p[6]), line=p.lineno(6), pos=p.lexpos(6))
    index_node += 1

    p[0] = pai

def p_lista_parametros(p):
    '''
    lista_parametros : lista_parametros VIRGULA parametro
                | parametro
                | vazio
    '''

    global index_node
    pai = Node(str(index_node), value="lista_parametros")
    index_node += 1

    if(len(p) == 4):
        p[1].parent = pai
        Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
        index_node += 1
        p[3].parent = pai
    elif(p[1] is not None):
        p[1].parent = pai
    else:
        Node(str(index_node), pai, value="")
        index_node += 1

    p[0] = pai

def p_parametro(p):
    '''
    parametro : tipo DOIS_PONTOS ID
            | parametro ABRE_COLCHETE FECHA_COLCHETE
    '''

    global index_node
    pai = Node(str(index_node), value="parametro")
    index_node += 1

    p[1].parent = pai
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[3]), line=p.lineno(3), pos=p.lexpos(3))
    index_node += 1

    p[0] = pai

def p_corpo(p):
    '''
    corpo : corpo acao
        | vazio
    '''

    global index_node
    pai = Node(str(index_node), value="corpo")
    index_node += 1
    
    
    if(len(p) == 3):
        p[1].parent = pai
        p[2].parent = pai
    else:
        Node(str(index_node), pai, value="")
        index_node += 1

    p[0] = pai

def p_acao(p):
    '''
    acao : expressao
        | declaracao_variaveis
        | se
        | repita
        | leia
        | escreva
        | retorna
    '''

    global index_node
    pai = Node(str(index_node), value="acao")
    index_node += 1

    p[1].parent = pai
    p[0] = pai


def p_se(p):
    '''
    se : SE expressao ENTAO corpo FIM
          | SE expressao ENTAO corpo SENAO corpo FIM
    '''

    global index_node
    pai = Node(str(index_node), value="se")
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    p[2].parent = pai
    
    Node(str(index_node), pai, value=str(p[3]), line=p.lineno(3), pos=p.lexpos(3))
    index_node += 1
    p[4].parent = pai
    
    Node(str(index_node), pai, value=str(p[5]), line=p.lineno(5), pos=p.lexpos(5))
    index_node += 1
    
    if(len(p) == 8):
        p[6].parent = pai
        Node(str(index_node), pai, value=str(p[7]), line=p.lineno(7), pos=p.lexpos(7))
        index_node += 1

    p[0] = pai

def p_repita(p):
    '''
    repita : REPITA corpo ATE expressao
    '''
    global index_node
    pai = Node(str(index_node), value="repita")
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    p[2].parent = pai
    
    Node(str(index_node), pai, value=str(p[3]), line=p.lineno(3), pos=p.lexpos(3))
    index_node += 1
    p[4].parent = pai

    p[0] = pai

def p_atribuicao(p):
    '''
    atribuicao : var ATRIBUICAO expressao
    '''
    
    global index_node
    pai = Node(str(index_node), value="atribuicao", line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    
    p[1].parent = pai
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai

    p[0] = pai

def p_leia(p):
    '''
    leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE
    '''

    global index_node
    pai = Node(str(index_node), value="leia")
    index_node += 1
    
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai
    
    Node(str(index_node), pai, value=str(p[4]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_escreva(p):
    '''
    escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE
    '''

    global index_node
    pai = Node(str(index_node), value="escreva")
    index_node += 1

    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai
    
    Node(str(index_node), pai, value=str(p[4]), line=p.lineno(4), pos=p.lexpos(4))
    index_node += 1

    p[0] = pai

def p_retorna(p):
    '''
    retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE
    '''

    global index_node
    pai = Node(str(index_node), value="retorna", line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai
    
    Node(str(index_node), pai, value=str(p[4]), line=p.lineno(4), pos=p.lexpos(4))
    index_node += 1

    p[0] = pai

def p_expressao(p):
    '''
    expressao : expressao_logica
                | atribuicao
    '''

    global index_node
    pai = Node(str(index_node), value="expressao")
    index_node += 1
    
    p[1].parent = pai

    p[0] = pai

def p_expressao_logica(p):
    '''
    expressao_logica : expressao_simples
                    | expressao_logica operador_logico expressao_simples
    '''

    global index_node
    pai = Node(str(index_node), value="expressao_logica")
    index_node += 1
    
    p[1].parent = pai

    if(len(p) == 4):
        p[2].parent = pai
        p[3].parent = pai
        
    p[0] = pai

def p_expressao_simples(p):
    '''
    expressao_simples : expressao_aditiva
                    | expressao_simples operador_relacional expressao_aditiva
    '''

    global index_node
    pai = Node(str(index_node), value="expressao_simples")
    index_node += 1
    
    p[1].parent = pai
    
    if(len(p) == 4):
        p[2].parent = pai
        p[3].parent = pai

    p[0] = pai

def p_expressao_aditiva(p):
    '''
    expressao_aditiva : expressao_multiplicativa
                    | expressao_aditiva operador_soma expressao_multiplicativa
    '''

    global index_node
    pai = Node(str(index_node), value="expressao_aditiva")
    index_node += 1
    
    p[1].parent = pai
    
    if(len(p) == 4):
        p[2].parent = pai
        p[3].parent = pai

    p[0] = pai

def p_expressao_multiplicativa(p):
    '''
    expressao_multiplicativa : expressao_unaria
                            | expressao_multiplicativa operador_multiplicacao expressao_unaria
    '''

    global index_node
    pai = Node(str(index_node), value="expressao_multiplicativa")
    index_node += 1
    
    p[1].parent = pai
    
    if(len(p) == 4):
        p[2].parent = pai
        p[3].parent = pai

    p[0] = pai

def p_expressao_unaria(p):
    '''
    expressao_unaria : fator
                    | operador_soma fator
                    | operador_negacao fator
    '''

    global index_node
    pai = Node(str(index_node), value="expressao_unaria")
    index_node += 1
    
    
    if(len(p) == 3):
        if(p[1] == '!'):
            Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
            index_node += 1
        else:
            p[1].parent = pai

        p[2].parent = pai
    else:  
        p[1].parent = pai

    p[0] = pai

def p_operator_relacional(p):
    '''
    operador_relacional : MENOR
                        | MAIOR
                        | IGUAL
                        | DIFERENCA
                        | MENOR_IGUAL
                        | MAIOR_IGUAL
    '''

    global index_node
    pai = Node(str(index_node), value='operador_relacional')
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_operador_soma(p):
    '''
    operador_soma : MAIS
                | MENOS
    '''

    global index_node
    pai = Node(str(index_node), value='operador_soma')
    index_node += 1
    
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_operador_logico(p):
    '''
    operador_logico : E_LOGICO
                | OU_LOGICO
    '''

    global index_node
    pai = Node(str(index_node), value='operador_logico')
    index_node += 1
    
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_operador_negacao(p):

    '''
    operador_negacao : NEGACAO
    '''

    global index_node
    pai = Node(str(index_node), value='operador_negacao')
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai


def p_operador_multiplicacao(p):
    '''
    operador_multiplicacao : MULTIPLICACAO
                            | DIVISAO
    '''

    global index_node
    pai = Node(str(index_node), value='operador_multiplicacao')
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_fator(p):
    '''
        fator : ABRE_PARENTESE expressao FECHA_PARENTESE
            | chamada_funcao
            | var
            | numero
    '''

    global index_node
    pai = Node(str(index_node), value='fator')
    index_node += 1
    
    
    if(len(p) == 4):
        Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
        index_node += 1
        p[2].parent = pai
        
        Node(str(index_node), pai, value=str(p[3]), line=p.lineno(3), pos=p.lexpos(3))
        index_node += 1
    else:
        p[1].parent = pai

    p[0] = pai

def p_numero(p):
    '''
    numero : NUM_INTEIRO
        | NUM_PONTO_FLUTUANTE
        | NUM_NOTACAO_CIENTIFICA
    '''

    global index_node
    pai = Node(str(index_node), value='numero')
    index_node += 1
    
    Node(str(index_node), pai, value=p[1], line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1

    p[0] = pai

def p_chamada_funcao(p):
    '''
    chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE
    '''

    global index_node
    pai = Node(str(index_node), value='chamada_funcao', line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
    
    Node(str(index_node), pai, value=str(p[1]), line=p.lineno(1), pos=p.lexpos(1))
    index_node += 1
        
    Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
    index_node += 1
    p[3].parent = pai
        
    Node(str(index_node), pai, value=str(p[4]), line=p.lineno(4), pos=p.lexpos(4))
    index_node += 1

    p[0] = pai


def p_lista_argumentos(p):
    '''
    lista_argumentos : lista_argumentos VIRGULA expressao
                    | expressao
                    | vazio
    '''

    global index_node
    pai = Node(str(index_node), value='lista_argumentos')
    index_node += 1
    
    if(len(p) == 4):
        p[1].parent = pai
        Node(str(index_node), pai, value=str(p[2]), line=p.lineno(2), pos=p.lexpos(2))
        index_node += 1
        
        p[3].parent = pai
    
    elif(p[1] is not None):
        p[1].parent = pai
    else:
        Node(str(index_node), pai, value="")
        index_node += 1

    p[0] = pai

def p_vazio(p):
    '''
        vazio :
    '''
    pass


def p_error(p):
    global has_success
    has_success = False
    
    if(not p):
        return
    
    token = p
    print("Erro:[{line},{column}]: Erro próximo ao token '{token}'".format(
        line=token.lineno, column=token.lineno, token=token.value))

    parser.errok()


parser = yacc.yacc()

def parse(data):
    result_parse = parser.parse(data)

    global has_success
    return result_parse, has_success