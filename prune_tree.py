# -*- coding: utf-8 -*-

nodes_read = []


def examine_tree(tree):
    if (tree.value == 'programa'):
        program = tree
        children = list(program.children)
        
        while (len(children) > 0):
            if (children[0].value != 'declaracao'):
                node = children[0]
                node.parent = None
                
                children = children[1:]
                children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                
                node.parent = None
                node.children[0].parent = program

        return program
    elif(tree.value == 'cabecalho'):
        for child in tree.children:
            tree.parent.children = list(tree.parent.children) + [child]

        cabecalho = tree.parent
        tree.parent = None

        return cabecalho
    elif(tree.value == 'corpo'):
        body = tree
        children = list(body.children)
        
        while (len(children) > 0):
            if (children[0].value != 'acao'):
                node = children[0]
                node.parent = None
                children = children[1:]
                
                if len(node.children) > 0:
                    children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                
                node.parent = None
                node.children[0].parent = body

        return body
    elif(tree.value == 'tipo' or tree.value == ',' or tree.value == ':' or tree.value == ':=' or tree.value == '(' or tree.value == ')' or tree.value == 'fim'):
        for child in tree.children:
            tree.parent.children = [child] + list(tree.parent.children)
        tree.parent = None

        return None
    elif(tree.value == 'lista_variaveis'):
        parent = tree.parent
        children = list(tree.children)
        
        while (len(children) > 0):
            if (children[0].value != 'var'):
                node = children[0]
                node.parent = None
                children = children[1:]
                children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                node.parent = parent
        tree.parent = None

        return parent
    elif(tree.value == 'inicializacao_variaveis'):
        node = tree
        node.value = 'atribuicao'
        aux = node.children[0]
        aux.parent = None
        
        for child in aux.children:
            child.parent = node

        return node
    elif(tree.value == 'lista_parametros'):
        first_params_list = tree
        children = list(first_params_list.children)
        
        while (len(children) > 0):
            if (children[0].value != 'parametro'):
                node = children[0]
                node.parent = None
                children = children[1:]
                
                if len(node.children) > 0:
                    children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                
                if(node.parent != first_params_list):
                    node.parent = None
                    first_params_list.children = [node] + list(first_params_list.children)

        return first_params_list
    elif(tree.value == 'lista_argumentos'):
        first_argument_list = tree
        children = list(first_argument_list.children)
        
        while (len(children) > 0):
            if (children[0].value != 'expressao'):
                node = children[0]
                node.parent = None
                children = children[1:]
               
                if len(node.children) > 0:
                    children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                
                if(node.parent != first_argument_list):
                    node.parent = None
                    first_argument_list.children = [node] + list(first_argument_list.children)

        return first_argument_list
    elif(tree.value == 'parametro'):
        first_param = tree
        children = list(first_param.children)
        
        while (len(children) > 0):
            if (children[0].value == 'parametro'):
                node = children[0]
                node.parent = None
                children = children[1:]
                
                if len(node.children) > 0:
                    children = list(node.children) + children
            else:
                node = children[0]
                children = children[1:]
                
                if (node.parent != first_param):
                    first_param.children = [node] + list(first_param.children)

        return first_param
    elif(tree.value == 'indice'):
        index = tree
        children = list(index.children)
        while (len(children) > 0):
            if (children[0].value == 'indice'):
                node = children[0]
                children = children[1:]
                node.parent = None
                new_children = []
                
                for child in node.children:
                    child.parent = None
                    new_children.append(child)
                children = new_children + children
                index.children = new_children + list(index.children)
                
            else:
                children = children[1:]

        return index
    elif(tree.value == 'retorna' or tree.value == 'leia' or tree.value == 'escreva' or tree.value == 'então' or tree.value == 'repita' or tree.value == 'até'):
        action = tree
        children = list(action.children)

        while(len(children) > 0):
            if(children[0].value == 'então' or children[0].value == 'até' or children[0].value == 'leia' or children[0].value == 'repita' or children[0].value == 'escreva' or children[0].value == 'retorna'):
                children[0].parent = None

            children = children[1:]

        return action
    elif(tree.value == 'condicional'):
        conditional = tree
        children = conditional.children
        children_if = children[0]
        children_expression = children[1]
        children_body = children[3]

        children_if.parent = None
        children_expression.parent = None
        children[2].parent = None
        children_body.parent = None

        children_expression.parent = conditional
        children_if.parent = conditional
        children_body.parent = children_if

        if(len(children) > 5):
            children_than = children[4]
            body_senao = children[5]

            children_than.parent = None

            children[6].parent = None

            children_than.parent = conditional
            body_senao.parent = children_than
        else:
            children[4].parent = None

        return conditional
    elif(tree.value == 'expressao_logica' or tree.value == 'expressao_simples' or tree.value == 'expressao_multiplicativa' or tree.value == 'expressao_aditiva'):
        expression = tree
        children = list(expression.children)

        if(len(children) == 3):
            expression.value = children[1].children[0].value
            expression.line = children[1].children[0].line
            expression.pos = children[1].children[0].pos

            new_children = list(expression.children)
            new_children.pop(1)
            expression.children = new_children
        
        elif(len(children) == 1):
            expression.value = children[0].value
            children[0].parent = None

            for child in children[0].children:
                child.parent = expression

            expression = expression.parent

        return expression
    elif(tree.value == 'operador_logico' or tree.value == 'operador_soma' or tree.value == 'operador_multiplicacao' or tree.value == 'operador_relacional' or tree.value == 'operador_negacao'):
        root = tree
        child = root.children[0]

        child.parent = None
        root.value = child.value

        return root
    elif(tree.value == 'expressao'):
        expression = tree
        child = list(expression.children)[0]

        if(child.value == 'atribuicao'):
            child.parent = None
            expression.value = child.value
            expression.children = child.children
        return expression

    return tree


def prune_tree(big_tree):
    global nodes_read
    nodes_read.append(big_tree)

    tree = examine_tree(big_tree)

    if(not tree and tree not in nodes_read):
        return
    for child in tree.children:
        prune_tree(child)
