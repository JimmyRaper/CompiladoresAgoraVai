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
        print("<" + str(token.type) + ", '" + str(token.value) + "'>")
    print("\n")

# Save Tokens in file
def save_tokens(tokens_list, name_file):
    
    try:
        token_file = open(name_file, 'w')
        for token in tokens_list:
            token_file.write("<" + str(token.type) + ", '" + str(token.value) + "'>" + "\n")
        token_file.close()       
        return True
    
    except:
        print('A noble mistake struck amid reading the file')
        return False