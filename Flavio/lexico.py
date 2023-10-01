import re
from Complemento import getCode, TokenList, opList, compareOpList, specialSymbolList, Tokens, IdTable, opSymbol, compareOpSymbol, specialOpSymbol

patternID = re.compile(r'[_a-zA-Z][_a-zA-Z0-9]+')
patternInt = re.compile(r'^-?\b\d+\b')
patternBool = re.compile(r'false|true')
patternString = re.compile(r'"[^"]*"')
patternDouble = re.compile(r'\d+.\d+')

def identify(table, lexema):
    print(lexema)
    if lexema in TokenList:
        table.append(lexema)
        Tokens.append(lexema)
    elif bool(re.match(patternID, lexema)):
        table.append("ID")
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
            if lexema != "" and lexema != "/":
                identify(table, lexema)
                lexema = ""
            
            if c in specialSymbolList:
                table.append(c)
                specialOpSymbol.append(c)
            else: #opSymbol
                if count + 1 < code.__len__():
                    nextChar = code[count + 1]
                    c += nextChar
                    if c in compareOpList:
                        table.append(c)
                        compareOpSymbol.append(c)
                        count += 1
                    elif c == "//":
                        comment = True
                        count += 1
                    else:
                        table.append(c)
                        opSymbol.append(c)
                else:
                    table.append(c)
                    opSymbol.append(c)
        else:
            if c != '\n':
                if c == ' ':
                    if openStr:
                        lexema += c
                elif not comment:
                    lexema += c
            else:
                comment = False
        general = openStr or comment
        count += 1
                
    if lexema != "":
        identify(table, lexema)
    print(table)




main()
print("")