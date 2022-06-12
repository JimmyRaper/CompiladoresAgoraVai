from symbol_table import Symbol_table

RELATION_OPERATION = ["=", "<>", ">", "<", ">=", "<=", "&&", "||"]
TYPE = ["inteiro", "flutuante"]

class Semantic_analyzer():
    def __init__(self):
        self.symbol__table = Symbol_table()
        self.has_success = True
        
    def verify_tree(self, node):
        currentStatus = self.__analyze(node)
        
        if (not currentStatus["keepingGoing"]):
            return
        
        for child in node.children:
            self.verify_tree(child)
            
        if (currentStatus["newContext"]):
            self.symbol__table.finalize_current_context()
        
        if (currentStatus["isFunction"]):
            line = self.symbol__table.get_last_line_global_scope()
            
            if (line['tipo'] != '' and not self.symbol__table.has_return()):
                self.has_success = True
                print("Função" + line["nome"] + "não possui retorno, verifique a função")

    def verify_table_line(self, node_type, used = True, initialized = False):
        aux = node_type.children[0].value
        line = self.symbol__table.search_line(aux, used = used, initialized = initialized)
        node_type.table_pointer = line

        if (not line):
            self.has_success = False    
            print('A' + ('variável ' if(node_type.value == 'var') else 'função ') + aux + ' não foi declarada em ' + str(node_type.children[0].line) + ':' + str(node_type.children[0].pos))
        
        return line if line else None
    
    def __create_variable_to_table(self, variable, _type):
        dimension = self.__analyze_variable(variable)
        line_table = {
            "nome": variable.children[0].value,
            "tipo": _type,
            "usada": False,
            "tipo_simbolo": "var",
            "inicializada": False,
            "dimensao": dimension,
            "linha": variable.children[0].line,
            "posicao": variable.children[0].pos,
            "valor": None
        }
        
        insert_status = self.symbol__table.insert_table(line_table)
        
        line = self.symbol__table.search_line(variable.children[0].value)
        variable.children[0].table_pointer = line
        
        if (not insert_status):
            self.has_success = False
   
    def __analyze_declaration_variables(self, node):
        children = node.children
        _type = children[0].value
        
        for variable in children[1:]:
            self.__create_variable_to_table(variable, _type)

    def __analyze_params_list(self, node): 
        params = node.children
        for param in params:
            par_name = param.children[1].value
            dimension = int(len(param.children[2:])/2)
            line_table = {
            "nome": param.children[1].value,
            "tipo": param.children[0].value,
            "usada": False,
            "tipo_simbolo": "parametros",
            "inicializada": True,
            "dimensao": dimension,
            "linha": param.children[0].line,
            "posicao": param.children[0].pos,
            }
            self.symbol__table.insert_table(line_table)
           
            line = self.symbol__table.search_line(par_name)
            param.children[1].table_pointer = line

    def __analyze_function_call(self, node):
        function = self.verify_table_line(node, False)
        node.table_pointer = function
        
        if (function):
            list_args = node.children[-1]
            params = function['parametros']
            args = []
            
            for expression in list_args.children:
                arg = {}
                expression_type = self.__analyze_expression(expression).split(' ')

                arg['tipo'] = expression_type[0]
                arg['vet'] = int(expression_type[1]) if len(expression_type) == 2 else 0
                args.append(arg)

            if (function['nome'] == 'principal'):
                
                if (self.symbol__table.get_current_context().scope == 'principal'):
                    print('--- Chamada recursiva para a função principal ---')
                
                else:
                    self.has_success = False
                    print('Não foi permitida a chamada para a função principal')
                    
                if (len(params) != len(args)):
                    self.has_success = False
                    print('A função \'' + function['nome'] + '\' foi declarada com o número de parâmetros diferentes da assinatura original da função. Era esperado ' + str(len(params)) + ', mas foi passado ' + str(len(args)) + ', na linha ' + str(function['line']) + ':' + str(function['pos']))
                    
                elif (params != args):
                    self.has_success = False
                    print('Conversão Implícita em função \'' + function['nome'] + '\' em ' + str(function['line']) + ':' + str(function['pos']))
        
    def __analyze_variable(self, variable):
        dimension = 0
        
        if (len(variable.children) > 1):
            list_index = variable.children[1]
            
            for child in list_index.children:
                
                if (child.value != "[" and child.value != "]"):
                    _type = self.__analyze_expression(child)
                    
                    if(_type and _type != "inteiro"):
                        self.success = False
                        print("O indice deve ser do tipo inteiro na linha" + str(variable.children[0].line) + "." + str(variable.children[0].pos))
                    
                    dimension += 1
        
        return dimension
    
    def __analyze_single_expression(self, node):
        children = node.children
        
        if (len(children) == 1):
            expression_type = children[0].children[0]
        else:
            operation = children[0].value
            expression_type = children[1].children[0]
            
            if (operation == "!"):
                if (expression_type.value == "expressao"):
                    self.__analyze_expression(expression_type)
                return 'invalid_type'

        if (expression_type.value == "numero"):
            number = expression_type.children[0].value
            return "inteiro" if (type(number) is int) else "flutuante"
        
        elif (expression_type.value == "expressao"):
            return self.__analyze_expression(expression_type)
        
        else:
            line = self.verify_table_line(expression_type)
            
            if (line and (line['tipo_simbolo'] == 'var' or line['tipo_simbolo'] == 'parametros')):
                dimension = line['dimensao']
            
                if (dimension != 0):
                    real_dimension = len(expression_type.children) - 1
            
                    if (dimension - real_dimension != 0):
                        return line['tipo']

            if (expression_type.value == 'chamada_funcao'):
                self.__analyze_function_call(expression_type)
        
            return line['tipo'] if line else None
    
    def __analyze_expression(self, node):
        if (node.value == "expressao"):
            return self.__analyze_expression(node.children[0])
        
        if (node.value == "expressao_unaria"):
            return self.__analyze_single_expression(node)
        
        type1 = self.__analyze_expression(node.children[0])
        type2 = self.__analyze_expression(node.children[1])
            
            
        if (node.value in RELATION_OPERATION):
            if (not type1 or not type2 or (len(type1.split(" ")) == 2 or len(type2.split(" ")) == 2)):
                self.has_success = False
                print("Tipo Inválido encontrado na linha" + str(node.line) + ":" + str(node.pos))
            
            return "invalid_type"
            
        if (type1 == type2):
            return type1
            
        elif (type1 in TYPE and type2 in TYPE):
            return "flutuante"
            
        return None
                     
    def __analyze_assignment(self, node):
        variable = node.children[0]
        expression = node.children[1]
        self.__analyze_variable(variable)
        line = self.verify_table_line(variable, initialized=True, used=False)
        variable_type = "inteiro"
        
        if (line):
           variable_type = line["tipo"]

        expression_type = self.__analyze_expression(expression)
        
        if (expression_type == "invalid_type"):
            print("Tipo inválido associado a linha " + str(variable.line) + "." + str(variable.pos))
            self.has_success = False
        elif (variable_type != expression_type):
            print("Conversão de tipo implícita na linha " + str(variable.line) + "." + str(variable.pos))
            self.has_success = False
    
    def __analyze_body(self, node):
        for child in node.children:
            if (child.value == "expressao"):
                self.__analyze_expression(child)
     
    def __analyze_return(self, node):
        expression_type = self.__analyze_expression(node.children[0])
        self.symbol__table.set_return()
        
        line = self.symbol__table.get_last_line_global_scope()
        
        if (expression_type not in TYPE or line['tipo'] not in TYPE):
            self.has_success = False
            print('Retorno inválido na linha ' + str(node.line) + ':' + str(node.pos))
        
        elif (expression_type != line['tipo']):
            print('Conversão Implícita de tipos na linha ' + str(node.line) + ':' + str(node.pos))
            
    def __analyze_function_declaration(self, node):
        params = []
        function_type = None
        
        if (len(node.children) == 4):
            function_type = node.children[0].value
            function_name = node.children[1].value
            params_list = node.children[2]
        else:
            function_name = node.children[0].value
            params_list = node.children[1]

        for param in params_list.children:
            params.append({
                "tipo_simbolo": param.children[0].value,
                "vet": 0 if len(param.children) == 2 else int((len(param.children) - 2)/2)
            })
            
        type = function_type if function_type else ''
        
        line_table = {
            "nome": function_name,
            "tipo": type,
            "usada": False,
            "tipo_simbolo": "funcao",
            "inicializada": True,
            "dimensao": 0,
            "linha": node.children[0].line,
            "posicao": node.children[0].pos,
            "parametros": params
        }
            
        insert_status = self.symbol__table.insert_table(line_table)
            
        line = self.symbol__table.search_line(function_name, used=False)
        
        if (len(node.children) == 4):
            node.children[1].table_pointer = line
        else:
            node.children[0].table_pointer = line
        if (not insert_status):
            self.has_success = False

        self.symbol__table.add_context(function_name)
        
    def __analyze_add_new_contex(self, node):
        self.symbol__table.add_context(node.value)
    
    def __analyze_read(self, node):
        var = node.children[0]
        var.children[0].table_pointer = self.verify_table_line(var, initialized = True)

    def __analyze(self, node):
        if (node.value == "declaracao_variaveis"):
            self.__analyze_declaration_variables(node)
            return {
                "keepingGoing": False,
                "isFunction": False,
                "newContext": False,
            }
        elif (node.value == "lista_parametros"):
            self.__analyze_params_list(node)
            return {
                "keepingGoing": False,
                "isFunction": False,
                "newContext": False,
            }
        elif (node.value == "atribuicao"):
            self.__analyze_assignment(node)
            return {
                "keepingGoing": True,
                "isFunction": False,
                "newContext": False,
            }
        elif (node.value == "corpo"):
            self.__analyze_body(node)
            return {
                "keepingGoing": True,
                "isFunction": False,
                "newContext": False,
            }
        elif (node.value == "retorna"):
            self.__analyze_return(node)
            return {
                "keepingGoing": False,
                "isFunction": False,
                "newContext": False,
            }
        elif (node.value == "declaracao_funcao"):
            self.__analyze_function_declaration(node)
            return {
                "keepingGoing": True,
                "isFunction": True,
                "newContext": True,
            }
        elif (node.value == 'repita' or node.value == 'se' or node.value == 'senão'):
            self.__analyze_add_new_contex(node)
            
            if (node.value == "repita"):
                for child in node.children:
                    if(child.value == "expression"):
                        self.__analyze_expression(child)
                        
            return {
                "keepingGoing": True,
                "isFunction": False,
                "newContext": True,
            }
        elif (node.value == 'condicional'):
            for child in node.children:
                if(child.value == 'expressao'):
                    self.verify_expression(child)
                    
            return {
                'keepingGoing': True,
                'isFunction': False,
                'newContext': False,
            }
        elif (node.value == "leia"):
            self.__analyze_read(node)
            
            return {
                'keepingGoing': True,
                'isFunction': False,
                'newContext': False,
            }
        elif(node.value == 'chamada_funcao'):
            self.__analyze_function_call(node)

            return {
                'keepingGoing': True,
                'isFunction': False,
                'newContext': False,
            }
        elif(node.value == 'escreva'):
            self.__analyze_expression(node.children[0])

            return {
                'keepingGoing': False,
                'isFunction': False,
                'newContext': False,
            }
        else:
            return {
                'keepingGoing': True,
                'isFunction': False,
                'newContext': False,
            }

    def check_principal_function(self):
        line = self.symbol__table.has_principal()
        
        if (line and line["usada"]):
            print('Chamada para a função principal não pode ser executada.')
            self.has_success = False
        elif(not line):
            print('Função principal não foi declarada.')
            self.has_success = False

    def check_unused_and_uninitialized_variable(self):
        for line in self.symbol__table.get_unused_lines('inicializada'):
            print('A variável \'' + line['nome'] + '\' foi declarada, e não foi utilizada em ' + str(line['line']) + ':' + str(line['pos']))

        for line in self.symbol__table.get_unused_lines('usada'):
            if (line['nome'] == 'principal'):
                continue
            print('A função \'' + line['nome'] + '\' foi declarada, mas não utilizada em ' + str(line['line']) + ':' + str(line['pos']))

def semantic_analyze(tree):
    analyzer = Semantic_analyzer()
    analyzer.verify_tree(tree)
    analyzer.check_principal_function()
    analyzer.check_unused_and_uninitialized_variable()
    
    
    return analyzer.has_success