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
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'

t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_IS_EQUALS = r'=='
t_IS_DIFFERENT = r'!='
t_LESS_THAN_OR_EQUALS = r'<='
t_GREATER_THAN_OR_EQUALS = r'>='

t_PONTO_VIRGULA = r';'
t_DOIS_PONTOS = r':'
t_PAREN_ABERTO = r'\('
t_PAREN_FECHADO = r'\)'
t_CHAVE_ABERTA = r'\['
t_CHAVE_FECHADA = r'\]'
t_COLCHETE_ABERTO = r'{'
t_COLCHETE_FECHADO = r'}'
t_VIRGULA = r','
t_DOT = r'\.'


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
    global lexer
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
    '''declaracao : declaracao declaracao
    | declaracao_variavel
    | declaracao_funcao
    | declaracao_estrutura
    | estrutura_de_controle
    | print
    | COMMENT
    | 
    
    declaracao_variavel : ID EQUAL expressao PONTO_VIRGULA
    | tipo ID PONTO_VIRGULA
    | tipo ID EQUAL expressao PONTO_VIRGULA
    | tipo array EQUAL expressao PONTO_VIRGULA
    | ID PLUS PLUS PONTO_VIRGULA
    | ID MINUS MINUS PONTO_VIRGULA
    | declaracao_variavel declaracao_variavel
    
    declaracao_funcao : tipo ID PAREN_ABERTO parametros PAREN_FECHADO bloco
    | VOID ID PAREN_ABERTO parametros PAREN_FECHADO bloco
    | tipo MAIN PAREN_ABERTO parametros PAREN_FECHADO bloco
    | VOID MAIN PAREN_ABERTO parametros PAREN_FECHADO bloco
    
    declaracao_estrutura : STRUCT ID COLCHETE_ABERTO declaracao_variavel COLCHETE_FECHADO
    
    declaracao_ou_coisas : declaracao_ou_coisas declaracao_ou_coisas
    | retorno
    | declaracao_variavel
    | estrutura_de_controle
    | print
    | COMMENT
    | 
    
    estrutura_de_controle : if
    | while
    | for
    | switch
    
    print : PRINTLN PAREN_ABERTO expressao PAREN_FECHADO PONTO_VIRGULA
    | 
    
    print_statement : atribuicao operador
    | atribuicao operador print_statement
    | atribuicao'''

def p_operador(p):
    '''operador : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | REST'''

def p_tipo(p):
    '''tipo : INT
    | STRING
    | BOOLEAN
    | DOUBLE
    | CHAR
    | FLOAT'''

def p_expressao(p):
    '''expressao : atribuicao
    
    atribuicao : NUMBER_DEC
    | NUMBER_INT
    | TYPE_FLOAT
    | TYPE_STRING
    | TYPE_BOOLEAN
    | TYPE_CHAR
    | ID
    | ID operador expressao
    | ID EQUAL expressao
    | ID PLUS_EQUAL expressao
    | ID MINUS_EQUAL expressao
    | ID TIMES_EQUAL expressao
    | ID DIVIDE_EQUAL expressao
    | ID REST_EQUAL expressao
    | ID AND EQUAL expressao
    | ID OR EQUAL expressao
    | ID comparador expressao
    | variavel_ou_valor PLUS_PLUS
    | variavel_ou_valor MINUS_MINUS
    | expressao_logica
    
    expressao_logica : expressao_relacional
    | expressao_logica AND expressao_relacional
    | expressao_logica OR expressao_relacional
    | NOT expressao_relacional
    
    expressao_relacional : expressao_aritmetica
    | expressao_aritmetica comparador expressao_aritmetica
    
    expressao_aritmetica : expressao_multiplicativa
    | expressao_aritmetica PLUS expressao_multiplicativa
    | expressao_aritmetica MINUS expressao_multiplicativa
    
    expressao_multiplicativa : expressao_unaria
    | expressao_multiplicativa TIMES expressao_unaria
    | expressao_multiplicativa DIVIDE expressao_unaria
    | expressao_multiplicativa REST expressao_unaria
    
    expressao_unaria : expressao_postfix
    | MINUS expressao_unaria
    | PLUS_PLUS expressao_postfix
    | MINUS_MINUS expressao_postfix
    
    expressao_postfix : primaria
    | primaria CHAVE_ABERTA expressao CHAVE_FECHADA
    | primaria PAREN_ABERTO argumentos PAREN_FECHADO
    | primaria DOT ID
    
    argumentos : expressao_lista
    | 

    expressao_lista : 
    
    primaria : variavel_ou_valor
    | PAREN_ABERTO expressao PAREN_FECHADO'''

def p_parametros(p):
    '''parametros : parametro
    | parametro VIRGULA parametros
    | 
    
    parametro : tipo ID
    | tipo ID CHAVE_ABERTA CHAVE_FECHADA'''

def p_bloco(p):
    '''bloco : COLCHETE_ABERTO declaracao_ou_coisas COLCHETE_FECHADO'''

def p_retorno(p):
    '''retorno : RETURN PONTO_VIRGULA
    | RETURN ID PONTO_VIRGULA
    | RETURN expressao PONTO_VIRGULA
    | RETURN ID PAREN_ABERTO parametros_dado PAREN_FECHADO PONTO_VIRGULA
    
    parametros_dado : variavel_ou_valor VIRGULA parametros_dado
    | variavel_ou_valor'''

def p_if_switch(p):
    '''if : IF PAREN_ABERTO statement PAREN_FECHADO bloco
    | IF PAREN_ABERTO statement PAREN_FECHADO bloco ELSE bloco
    | IF PAREN_ABERTO statement PAREN_FECHADO bloco elseif ELSE bloco

    elseif : ELSEIF PAREN_ABERTO statement PAREN_FECHADO bloco elseif
    | 
    
    statement : variavel_ou_valor comparador variavel_ou_valor operador_logico
    
    variavel_ou_valor : ID
    | NUMBER_DEC
    | NUMBER_INT
    | TYPE_STRING
    | TYPE_BOOLEAN
    | TYPE_CHAR
    | TYPE_FLOAT
    
    switch : SWITCH PAREN_ABERTO ID PAREN_FECHADO bloco_switch
    
    bloco_switch : COLCHETE_ABERTO cases COLCHETE_FECHADO
    
    cases : cases cases
    | CASE expressao DOIS_PONTOS declaracao_ou_coisas BREAK PONTO_VIRGULA
    | DEFAULT DOIS_PONTOS declaracao_ou_coisas BREAK PONTO_VIRGULA
    | '''

def p_loop(p):
    '''while : WHILE PAREN_ABERTO statement PAREN_FECHADO bloco
    
    for : FOR PAREN_ABERTO tipo ID EQUAL variavel_ou_valor PONTO_VIRGULA variavel_ou_valor comparador variavel_ou_valor PONTO_VIRGULA expressao PAREN_FECHADO bloco
    | FOR PAREN_ABERTO ID EQUAL variavel_ou_valor PONTO_VIRGULA variavel_ou_valor comparador variavel_ou_valor PONTO_VIRGULA expressao PAREN_FECHADO bloco'''

def p_comparador(p):
    '''comparador : LESS_THAN
    | IS_EQUALS
    | LESS_THAN_OR_EQUALS
    | GREATER_THAN
    | GREATER_THAN_OR_EQUALS
    | IS_DIFFERENT'''

def p_operador_logico(p):
    '''operador_logico : AND statement
    | OR statement
    | '''

def p_array(p):
    '''array : ID chaves_array
    | array_inicializacao
    
    array_inicializacao : COLCHETE_ABERTO expressao COLCHETE_FECHADO
    
    chaves_array : CHAVE_ABERTA expressao CHAVE_FECHADA
    | CHAVE_ABERTA CHAVE_FECHADA'''

def p_error(p):
    if p == None:
        raise Exception('Algum simbolo pode estar faltando ser inserido')

    cont = 1
    prev = p.lexer.lexdata[p.lexpos - cont]
    while prev == '' or prev == ' ' or prev == '\n':
        cont+=1
        prev = p.lexer.lexdata[p.lexpos - cont]

    errorTxt = '\nERRO SINTAXE\nPOSICAO DO ERRO EM RELACAO AO ARQUIVO: {}\nULTIMO TOKEN LIDO: {}\nTOKEN ANTERIOR AO LIDO: {}\n'.format(p.lexpos, p.value, prev)
    raise Exception(errorTxt)

def sintatico():
    lexico()

    parser = yacc.yacc()
    #while True:
    #    try:
    #        s = input('sintatico > ')
    #    except EOFError:
    #        break
    #    if not s: continue
    #    result = parser.parse(s)
    #    print(result)
    s = Complemento.getCode()
    result = parser.parse(s)
    #print(result)
    print('\nSINTATICO APROVADO!')


#lexico()
sintatico()
print("----------- FIM ---------------")