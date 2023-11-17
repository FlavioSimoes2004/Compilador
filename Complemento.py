TokenList = ["int", "boolean", "String", "float", "double", "true", "false", "null", "if", "while", "for", "char", "void", "else", "scanf", "main", "return", "void", "println"]
opList = ["=", "<", ">", "&&", "||", "!", "%", "+", "/", "-", "*"]
compareOpList = ["<", "==", "<=", ">", ">=", "!="]
specialSymbolList = [";", "(", ")", "[", "]", "{", "}", ","]

Tokens = []
opSymbol = []
compareOpSymbol = []
specialOpSymbol = []
IdTable = []


def getCode():
    code = ""
    with open('arquivoAqui/arquivo.txt', 'r') as arquivo:
        for line in arquivo:
            code += line
    return code