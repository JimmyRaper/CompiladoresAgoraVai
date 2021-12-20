from sys import argv
import lexical
import parser
import utils
import prune_tree


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

    parse_tree, has_success = parser.parse(data_file)

    if (not has_success):
        print('Processo sintático falhou.')
        return
    
    utils.export_tree(parse_tree, "parse_tree")
    
    # === Prune Tree Process === #
    
    prune_tree.prune_tree(parse_tree)
    
    print('Podando a árvore...')
    
    utils.export_tree(parse_tree, "prune_tree")

main(argv)