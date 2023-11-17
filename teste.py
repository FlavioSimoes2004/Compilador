import re

patternID = re.compile(r'(^[a-zA-Z]+$)|([_a-zA-Z][_a-zA-Z0-9]+$)')
texto = "e"
print(bool(re.match(patternID, texto)))