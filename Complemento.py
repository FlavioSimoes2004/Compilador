ReservedWordList = ["int", "boolean", "String", "float", "double", "true", "false", "null", "if", "while", "for", "char", "void", "else", "scanf", "main", "return", "void", "println"]
opList = ["=", "<", ">", "&&", "||", "!", "%", "+", "/", "-", "*"]
compareOpList = ["<", "==", "<=", ">", ">=", "!="]
specialSymbolList = [";", "(", ")", "[", "]", "{", "}", ","]


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
   'TYPE_FLOAT',
   'TYPE_BOOLEAN',
   'TYPE_STRING',
   'TYPE_CHAR',
   'ID',
   'OPERATOR',
   'COMPARE_OPERATOR',
   'SPECIAL_SYMBOL',
   'COMMENT'
]

RESERVED_WORD_LIST = {
    'int': 'INT',
    'String': 'STRING',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'double': 'DOUBLE',
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'float': 'FLOAT',
    'while': 'WHILE',
    'for': 'FOR',
    'char':'CHAR',
    'void': 'VOID',
    'else': 'ELSE',
    'scanf': 'SCANF',
    'main': 'MAIN',
    'return': 'RETURN',
    'println': 'PRINTLN',
    'struct' : 'STRUCT',
    'switch' : 'SWITCH',
    'case' : 'CASE',
    'default' : 'DEFAULT',
    'break' : 'BREAK',
    'continue': 'CONTINUE'
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
    '%': 'REST',
    '+=': 'PLUS_EQUAL',
    '-=': 'MINUS_EQUAL',
    '*=': 'TIMES_EQUAL',
    '/=': 'DIVIDE_EQUAL',
    '%=': 'REST_EQUAL',
    '++': 'PLUS_PLUS',
    '--': 'MINUS_MINUS'
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
    ':': 'DOIS_PONTOS',
    '(': 'PAREN_ABERTO',
    ')': 'PAREN_FECHADO',
    '[': 'CHAVE_ABERTA',
    ']': 'CHAVE_FECHADA',
    '{': 'COLCHETE_ABERTO',
    '}': 'COLCHETE_FECHADO',
    ',': 'VIRGULA',
    '.' : 'DOT'
}

reserved_word_table = []
operators_table = []
compare_operators_table = []
special_symbol_table = []
id_table = []