import ply.lex as lex
import Complemento
import re

tokens = []

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = Complemento.RESERVED_WORD_LIST.get(t.value,'ID')    # Check for reserved words
    return t

def t_TYPE_BOOLEAN(t):
    r'false|true'
    t.value = bool(t.value)
    return t

def t_TYPE_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

def t_NUMBER_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_NUMBER_DEC(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_COMMENT(t):
    r'^//'
    pass

def t_error(t):
    raise Exception("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def lexico():
    tokens = Complemento.TIPOS + list(Complemento.RESERVED_WORD_LIST.values())
    lexer = lex.lex()

    data = Complemento.getCode()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.type, tok.value)


def sintatico():
    lexico()


sintatico()