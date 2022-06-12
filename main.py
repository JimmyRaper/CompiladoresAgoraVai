# -*- coding: utf-8 -*-
from sys import argv
import lexical
import parser
import utils
import prune_tree
import semantics


def main(argv):
    # Reading Tpp file from terminal
    data_file = utils.read_file_Tpp(argv[1])
    if(not data_file):
        print("Arquivo não existente")
        return
    
    # === Lexical Process === #
    tokens = lexical.analyzer(data_file)
    
    # Print Tokens List
    # utils.print_tokens(tokens)
    
    # Save Token List
    utils.save_tokens(tokens,'Tokens.txt')

    # === Syntactic Process === #
    print('Processo sintático em andamento.')
    parse_tree, has_success = parser.parse(data_file)

    if (not has_success):
        print('Processo sintático falhou.')
        return
    
    utils.export_tree(parse_tree, "parse_tree")
    
    # === Prune Tree Process === #
    
    prune_tree.prune_tree(parse_tree)
    
    print('\nPodando a árvore... \n')
    
    utils.export_tree(parse_tree, "prune_tree")
    
    # === Semantic Process === #
    print('\nProcesso semantico em andamento. \n')
    
    semantic_success = semantics.semantic_analyze(parse_tree)
    
    if (not semantic_success):
        print('Processo semantico falhou.')
        return

main(argv)