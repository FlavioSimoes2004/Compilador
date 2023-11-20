ReservedWordList = ["int", "boolean", "String", "float", "double", "true", "false", "null", "if", "while", "for", "char", "void", "else", "scanf", "main", "return", "void", "println"]
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




#PLY
TIPOS = [
   'NUMBER_INT',
   'NUMBER_DEC', 
   'TYPE_BOOLEAN', 
   'TYPE_STRING', 
   'ID'
]

RESERVED_WORD_LIST = {
    'int': 'INT',
    'String': 'STRING',
    'boolean': 'BOOLEAN',
    'double': 'DOUBLE',
    'if': 'IF',
    'float': 'FLOAT',
    'while': 'WHILE',
    'for': 'FOR',
    'char':'CHAR',
    'void': 'VOID',
    'else': 'ELSE',
    'scanf': 'SCANF',
    'main': 'MAIN',
    'return': 'RETURN',
    'println': 'PRINTLN'
}