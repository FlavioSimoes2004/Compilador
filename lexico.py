import re
from Complemento import getCode, TokenList, opList, compareOpList, specialSymbolList#, Tokens, IdTable, opSymbol, compareOpSymbol, specialOpSymbol

reserved_word = []
IdTable = []
opSymbol = []
compareOpSymbol = []
specialOpSymbol = []

patternID = re.compile(r'(^[a-zA-Z]+$)|([_a-zA-Z][_a-zA-Z0-9]+$)')
patternInt = re.compile(r'^-?\b\d+\b$')
patternBool = re.compile(r'false|true')
patternString = re.compile(r'"[^"]*"')
patternDouble = re.compile(r'^-?\b\d+\.\d+\b$')

def identify(table, lexema):
    if lexema != "":
        print(lexema)
        if lexema in TokenList:
            table.append(lexema)
            reserved_word.append(lexema)
        elif bool(re.match(patternID, lexema)):
            if lexema not in IdTable:
                IdTable.append(lexema)
            table.append("(ID, "+ str(IdTable.index(lexema) + 1) + ")")
        else: #comparar para ver se é um valor
            if bool(re.match(patternInt, lexema)):
                table.append('NUM_INT_' + lexema)
            elif bool(re.match(patternString, lexema)):
                table.append("TEXTO: " + lexema)
            elif bool(re.match(patternDouble, lexema)):
                table.append("NUM_DEC_" + lexema)
            else:
                raise Exception("//---------------ERRO------------------\\")

def main():
    lexema = ""
    table = []
    openStr = False
    comment = False
    multiComment = False
    general = openStr or comment or multiComment
    
    code = getCode()
    count = 0
    while count < code.__len__():
        c = code[count]
        if c == ' ' and not general and lexema != "":
            identify(table, lexema)
            lexema = ""
        elif c == '"' and not comment and not multiComment:
            openStr = not openStr
            lexema += '"'
        elif (c in opList or c in specialSymbolList or c == '&' or c == '|') and (not general or (c == '*' and not comment and not openStr)):
            #if lexema != "" and lexema != "/":
                #identify(table, lexema)
                #lexema = ""
            
            if c in specialSymbolList:
                identify(table, lexema)
                table.append(c)
                specialOpSymbol.append(c)
                lexema = ""
            elif c in opList:
                if count + 1 < code.__len__():
                    newC = c + code[count + 1]
                    if newC in compareOpList:
                        identify(table, lexema)
                        table.append(newC)
                        compareOpSymbol.append(newC)
                        lexema = ""
                        count += 1
                    elif newC in opList:
                        identify(table, lexema)
                        table.append(newC)
                        opSymbol.append(newC)
                        lexema = ""
                    elif newC == "//":
                        identify(table, lexema)
                        lexema = ""
                        comment = True
                        count += 1
                    elif newC == "/*":
                        multiComment = True
                        identify(table, lexema)
                        lexema = ""
                        count += 1
                    elif newC == "*/":
                        multiComment = False
                        count += 1
                    elif c == '-':
                        if newC[1].isnumeric():
                            identify(table, lexema)
                            lexema = newC
                            count += 1
                    else:
                        identify(table, lexema)
                        table.append(c)
                        opSymbol.append(c)
                        lexema = ""
                else:
                    identify(table, lexema)
                    table.append(c)
                    opSymbol.append(c)
                    lexema = ""
            elif c == '&':
                    if count + 1 < code.__len__():
                        newC = c + code[count + 1]
                        if newC == "&&":
                            identify(table, lexema)
                            table.append(newC)
                            opSymbol.append(newC)
                            lexema = ""
                            count += 1
                        else:
                            lexema += c
            else: #c == '|'
                    if count + 1 < code.__len__():
                        newC = c + code[count + 1]
                        if newC == "||":
                            identify(table, lexema)
                            table.append(newC)
                            opSymbol.append(newC)
                            lexema = ""
                            count += 1
                        else:
                            lexema += c
        else:
            if c != '\n':
                if c == ' ':
                    if openStr:
                        lexema += c
                elif not comment and not multiComment:
                    lexema += c
            else:
                if not openStr and not multiComment: #para cancelar um comentario normal
                    if lexema != "":
                        identify(table, lexema)
                    comment = False
                    lexema = ""
                else:
                    if openStr: #se for string ele adiciona
                        lexema += c
        general = openStr or comment or multiComment
        count += 1
                
    identify(table, lexema)
    if openStr or multiComment:
        raise Exception("ERRO")
    print(table)




main()
print("")