# -*- coding: utf-8 -*-
from anytree import Node, PreOrderIter


class Symbol_table():
    def __initialize__(self):
        self.id = 1
        self.root = Node(0, scope='global', table=[])
        self.current_context = self.root

    def get_current_context(self):
        return self.current_context.context

    def add_context(self, context):
        self.current_context = Node(self.id, self.current_context, scope=context, table=[], isReturn=False)
        self.id += 1

    def finalize_current_context(self):
        self.current_context.context = self.current_context.parent

    def set_return(self):
        self.current_context.isReturn = True

    def has_principal(self):
        for line in self.root.table:
            if(line['nome' == 'principal']):
                return line

        return False

    def search_by_name(self, name, node):
        for line in node.table:
            if(line['nome'] == name):
                return line

        if(node.parent):
            return self.searchByName(name, node.parent)
        else:
            return False

    def search_line(self, name, usada=True, inicializada=False):
        line = self.searchByName(name, self.current_context)

        if(line and usada):
            line['usada'] = True

        if(line and inicializada):
            line['inicializada'] = True

        return line

    def insert_table(self, item):
        item['contexto'] = self.current_context.context
        line = self.search_line(item["nome"], False)

        if(item['contexto'] != 'global' and item['nome'] == 'principal' and item['tipo_simbolo'] != 'funcao'):
            print('ERRO: Principal deve ser uma função')
            return False

        if(line and line['contexto'] == self.contexto.scope):
            print('ERRO: ' + ('A variável ' if(item['tipo_simbolo'] == 'var') else 'Função ') + '\'' +
                  item['name'] + '\' já foi declarada na ' + str(item['line']) + ':' + str(item['column']))
            return False

        self.current_context.table.append(item)

        return True
     
    def get_unused_lines(self):
        response = []

        for contex in PreOrderIter(self.root):
            for line in contex.table:
                if(not line['usado']):
                    response.append(line)

        return response
    
    def get_uninitialized_lines(self):
        response = []

        for contex in PreOrderIter(self.root):
            for line in contex.table:
                if(not line['inicializado']):
                    response.append(line)

        return response

    def search_return(self, context):
        flag_return = False
        has_return = False

        for inner in context.children:
            response_return = inner.hasReturn

            if(not inner.hasReturn):
                response_return = self.search_return(inner)

            if(inner.scope == 'se'):
                flag_return = response_return
            elif(flag_return and inner.scope == 'senão' and response_return):
                has_return = True
        return has_return
    
    def get_last_line_global_scope(self):
        return self.root.table[-1]

    def has_return(self):
        return_function = self.root.children[-1].isReturn
        
        if(return_function):
            return return_function
        
        return self.search_return(self.root.children[-1])