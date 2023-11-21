import ply.lex as lex
import Complemento
import re

tokens = []

t_ignore  = ' \t'

def t_COMMENT(t):
    r'//.*'
    pass

def t_TYPE_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    if t.value in Complemento.RESERVED_WORD_LIST:
        t.type = Complemento.RESERVED_WORD_LIST.get(t.value)
    return t

def t_TYPE_BOOLEAN(t):
    r'false|true'
    t.value = bool(t.value)
    return t

def t_NUMBER_DEC(t):
    r'-?\d+\.\d+'
    #t.value = float(t.value)
    return t

def t_NUMBER_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_OPERATOR(t):
    r'.|..'
    if t.value == '.' or t.value == '..':
        raise Exception("LEXICO: Illegal character '%s'" % t.value[0])
    if t.value in Complemento.COMPARE_OP_LIST:
        t.type = 'COMPARE_OPERATOR'
    elif t.value in Complemento.SPECIAL_SYMBOLS_LIST:
        t.type = 'SPECIAL_SYMBOL'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise Exception("LEXICO: Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def lexico():
    tokens = Complemento.TIPOS + list(Complemento.RESERVED_WORD_LIST.values()) + list(Complemento.OP_LIST.values()) + list(Complemento.COMPARE_OP_LIST.values()) + list(Complemento.SPECIAL_SYMBOLS_LIST.values())
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