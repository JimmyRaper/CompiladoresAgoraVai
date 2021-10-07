from sys import argv
import lexical
import utils


def main(argv):

    # Reading Tpp file from terminal
    data_file = utils.read_file_Tpp(argv[1])
    if(not data_file):
        print("File not exists")
        return
    
    ############### LEX ###############

    tokens = lexical.analyzer(data_file)
    
    # Print Tokens List
    utils.print_tokens(tokens)
    
    # Save Token List
    utils.save_tokens(tokens,'Tokens.txt')

main(argv)