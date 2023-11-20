import ply.lex as lex
import re
import Complemento

tokens = ['NUMBER_INT', 'NUMBER_DEC', 'BOOLEAN_', 'STRING_', 'ID']
reserved = {
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
tokens += list(reserved.values())


t_ignore  = ' \t'

def t_ID(t):
    r'(^[a-zA-Z]+$)|([_a-zA-Z][_a-zA-Z0-9]+$)'
    if t.value in reserved:
        t.type = reserved.get(t.value)
    return t

def t_BOOLEAN_(t):
    r'false|true'
    t.value = bool(t.value)
    return t

def t_STRING_(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

def t_NUMBER_INT(t):
    r'^-?\b\d+\b$'
    t.value = int(t.value)
    return t

def t_NUMBER_DEC(t):
    r'^-?\b\d+\.\d+\b$'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'^//'
    pass
    # No return value. Token discarded

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def lexico():
    data = 'int ok'

    lexer = lex.lex()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)



def sintatico():
    lexico()



sintatico()