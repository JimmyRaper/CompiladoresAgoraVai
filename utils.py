# -*- coding: utf-8 -*-
from anytree.exporter import DotExporter
from anytree import RenderTree

# Reading Tpp File
def read_file_Tpp(path):
    try:
        file = open(path, 'r')
        return file.read()
    except:
        print('A noble mistake struck amid reading the file')
        return None

# Print Tokens
def print_tokens(tokens_list):
    for token in tokens_list:
        print(token.type)

# Save Tokens in file
def save_tokens(tokens_list, name_file):
    
    try:
        token_file = open(name_file, 'w')
        for token in tokens_list:
            token_file.write(token.type + "\n")
        token_file.close()       
        return True
    
    except:
        print('A noble mistake struck amid reading the file')
        return False


def export_tree(tree, fileName):
    print('Exportando arvore...')
    if(fileName):
        DotExporter(tree, nodeattrfunc=lambda node: 'label="{}"'.format(node.value)).to_dotfile(fileName + ".dot")
        DotExporter(tree, nodeattrfunc=lambda node: 'label="{}"'.format(node.value)).to_picture(fileName + ".png")
    else:
        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.value))
 