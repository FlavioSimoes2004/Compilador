import ply.lex as lex
import ply.yacc as yacc
import Complemento
import re

ordemTokens = []

t_ignore  = ' \t'

t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_REST = r'%'
t_NOT = '!'
t_AND = r'&&'
t_OR = r'\|\|'
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_TIMES_EQUAL = r'\*='
t_DIVIDE_EQUAL = '/='
t_REST_EQUAL = '%='

t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_IS_EQUALS = r'=='
t_IS_DIFFERENT = r'!='
t_LESS_THAN_OR_EQUALS = r'<='
t_GREATER_THAN_OR_EQUALS = r'>='

t_PONTO_VIRGULA = r';'
t_PAREN_ABERTO = r'\('
t_PAREN_FECHADO = r'\)'
t_CHAVE_ABERTA = r'\['
t_CHAVE_FECHADA = r'\]'
t_COLCHETE_ABERTO = r'{'
t_COLCHETE_FECHADO = r'}'
t_VIRGULA = r','


def t_COMMENT(t):
    r'//.*'
    return t

def t_TYPE_STRING(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

def t_TYPE_BOOLEAN(t):
    r'false|true'
    t.value = bool(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    if t.value in Complemento.RESERVED_WORD_LIST:
        t.type = Complemento.RESERVED_WORD_LIST.get(t.value)
        Complemento.reserved_word_table.append(t.value)
    return t

def t_NUMBER_DEC(t):
    r'-?\d+\.\d+'
    #t.value = float(t.value)
    return t

def t_NUMBER_INT(t):
    r'-?\d+'
    #t.value = int(t.value)
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





def p_programa(p):
    '''programa : declaracao'''

def p_declaracao(p):
    '''declaracao : declaracao_variavel
    
    declaracao_variavel : tipo ID PONTO_VIRGULA
    | tipo ID EQUAL expressao PONTO_VIRGULA'''

def p_tipo(p):
    '''tipo : INT
    | STRING
    | BOOLEAN
    | DOUBLE
    | CHAR
    | FLOAT'''

def p_expressao(p):
    '''expressao : atribuicao'''

def p_atribuicao(p):
    '''atribuicao : NUMBER_DEC
    | NUMBER_INT
    | TYPE_STRING
    | TYPE_BOOLEAN
    | ID
    | ID EQUAL expressao
    | ID PLUS_EQUAL expressao
    | ID MINUS_EQUAL expressao
    | ID TIMES_EQUAL expressao
    | ID DIVIDE_EQUAL expressao
    | ID REST_EQUAL expressao
    | ID AND EQUAL expressao
    | ID OR EQUAL expressao'''

def p_error(p):
    raise Exception("Syntax error")

def sintatico():
    lexico()

    parser = yacc.yacc()
    while True:
        try:
            s = input('sintatico > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)


#lexico()
sintatico()
print("----------- FIM ---------------")