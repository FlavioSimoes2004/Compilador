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
   'ID',
   'OPERATOR',
   'COMPARE_OPERATOR',
   'SPECIAL_SYMBOL'
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

OP_LIST = {
    '=': 'EQUAL',
    '&&': 'AND',
    '||': 'OR',
    '!': 'NOT',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'TIMES',
    '/': 'DIVIDE',
    '%': 'REST'
}

COMPARE_OP_LIST = {
    '<' : 'LESS_THAN',
    '==' : 'IS_EQUALS',
    '<=' : 'LESS_THAN_OR_EQUALS',
    '>' : 'GREATER_THAN',
    '>=': 'GREATER_THAN_OR_EQUALS',
    '!=': 'IS_DIFFERENT'
}

SPECIAL_SYMBOLS_LIST = {
    ';': 'PONTO_VIRGULA',
    '(': 'PAREN_ABERTO',
    ')': 'PAREN_FECHADO',
    '[': 'CHAVE_ABERTA',
    ']': 'CHAVE_FECHADA',
    '{': 'COLCHETE_ABERTO',
    '}': 'COLCHETE_FECHADO',
    ',': 'VIRGULA'
}