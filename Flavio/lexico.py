import re
from Complemento import getCode, TokenList, opList, compareOpList, specialSymbolList, Tokens, IdTable, opSymbol, compareOpSymbol, specialOpSymbol

patternID = re.compile(r'[_a-zA-Z][_a-zA-Z0-9]+')
patternInt = re.compile(r'^-?\b\d+\b$')
patternBool = re.compile(r'false|true')
patternString = re.compile(r'"[^"]*"')
patternDouble = re.compile(r'^-?\b\d+\.\d+\b$')

def identify(table, lexema):
    print(lexema)
    if lexema != "":
        if lexema in TokenList:
            table.append(lexema)
            Tokens.append(lexema)
        elif bool(re.match(patternID, lexema)):
            table.append("ID")
            if lexema not in IdTable:
                IdTable.append(lexema)
        else: #comparar para ver se é um valor
            if bool(re.match(patternInt, lexema)):
                table.append('NUM_INT_' + lexema)
            elif bool(re.match(patternString, lexema)):
                table.append("TEXTO")
            elif bool(re.match(patternDouble, lexema)):
                table.append("NUM_DOUBLE_" + lexema)
            else:
                table.append("ERRO")

def main():
    lexema = ""
    table = []
    openStr = False
    comment = False
    general = openStr or comment
    
    code = getCode()
    count = 0
    while count < code.__len__():
        c = code[count]
        if c == ' ' and not general and lexema != "":
            identify(table, lexema)
            lexema = ""
        elif c == '"' and not comment:
            openStr = not openStr
            lexema += '"'
        elif (c in opList or c in specialSymbolList) and not general:
            #if lexema != "" and lexema != "/":
                #identify(table, lexema)
                #lexema = ""
            
            if c in specialSymbolList:
                identify(table, lexema)
                table.append(c)
                specialOpSymbol.append(c)
                lexema = ""
            else: #opSymbol
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
                    elif c == '-':
                        if newC[1].isnumeric():
                            identify(table, lexema)
                            lexema = newC
                            count += 1
                    else:
                        if c != '&' and c != '|':
                            identify(table, lexema)
                            table.append(c)
                            opSymbol.append(c)
                            lexema = ""
                else:
                    if c != '&' and c != '|':
                        identify(table, lexema)
                        table.append(c)
                        opSymbol.append(c)
                        lexema = ""
        else:
            if c != '\n':
                if c == ' ':
                    if openStr:
                        lexema += c
                elif not comment:
                    lexema += c
            else:
                if lexema != "":
                    identify(table, lexema)
                comment = False
                lexema = ""
        general = openStr or comment
        count += 1
                
    if lexema != "":
        identify(table, lexema)
    print(table)




main()
print("")