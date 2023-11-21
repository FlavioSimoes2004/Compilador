import ply.lex as lex
import ply.yacc as yacc
import Complemento
import re

ordemTokens = []

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
        Complemento.reserved_word_table.append(t.value)
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
    #t.value = int(t.value)
    return t

def t_OPERATOR(t):
    r'.|..'
    if t.value == '.' or t.value == '..':
        raise Exception("LEXICO: Illegal character '%s'" % t.value[0])
    if t.value in Complemento.COMPARE_OP_LIST:
        t.type = 'COMPARE_OPERATOR'
        Complemento.compare_operators_table.append(t.value)
    elif t.value in Complemento.SPECIAL_SYMBOLS_LIST:
        t.type = 'SPECIAL_SYMBOL'
        Complemento.special_symbol_table.append(t.value)
    else: #is normal operator
        Complemento.operators_table.append(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise Exception("LEXICO: Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def lexico():
    global tokens
    tokens = Complemento.TIPOS + list(Complemento.RESERVED_WORD_LIST.values()) + list(Complemento.OP_LIST.values()) + list(Complemento.COMPARE_OP_LIST.values()) + list(Complemento.SPECIAL_SYMBOLS_LIST.values())
    lexer = lex.lex()

    data = Complemento.getCode()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        elif tok.type == 'ID':
            if tok.value not in Complemento.id_table:
                Complemento.id_table.append(tok.value)
            print('(ID, ' , (Complemento.id_table.index(tok.value) + 1) , ',' , tok.value, ')')
        else:
            print(tok.type, tok.value)
        ordemTokens.append(tok)
    print('LEXICO APROVADO!')





def p_expression_plus(p):
    '''expression : term OPERATOR term SPECIAL_SYMBOL'''
    if p[4] == ';':
        p[0] = p[1] + p[3]

def p_term(p):
    '''term : ID
    | NUMBER_INT
    | NUMBER_DEC'''
    p[0] = p[1]

def p_error(p):
    raise Exception("Syntax error")

def sintatico():
    lexico()

    parser = yacc.yacc()
    while True:
        try:
            s = input('Sintaxe > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)


sintatico()
print("----------- FIM ---------------")