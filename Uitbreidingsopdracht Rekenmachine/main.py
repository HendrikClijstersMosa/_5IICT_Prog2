# Gebruik deze file om de functie rekenmachine te testen!
from rekenmachine import rekenmachine

"""
Gebruik deze functies om te testen of het rekenmachine
functioneert zoals verwacht. 
Gebruik "ctrl+/" om regels uit/in commentaar te halen/zetten.
"""

print(rekenmachine(['3801 - 2', '123 + 49']))

"""
Expected output
'  3801      123'
'-    2    +  49'
'------    -----',
"""

# print(rekenmachine(['3801 - 2', '123 + 49']))

"""
Expected output
'  1         1'
'+ 2    - 9380'
'---    ------',
"""

# print(rekenmachine(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))

"""
Expected output
'  11      3801      1      123         1'
'+  4    - 2999    + 2    +  49    - 9380'
'----    ------    ---    -----    ------',
"""

# print(rekenmachine(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))

"""
Expected output
"Error: Operator must be '+' or '-'.",
"""

# print(rekenmachine(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))

"""
Expected output
"Error: Numbers cannot be more than four digits.",
"""

# print(rekenmachine(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))

"""
Expected output
"Error: Numbers must only contain digits.",
"""

# print(rekenmachine(['3 + 855', '988 + 40'], True))

"""
Expected output
'    3      988'
'+ 855    +  40'
'-----    -----'
'  858     1028',
"""

# print(rekenmachine(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

"""
Expected output
'   32         1      45      123      988'
'- 698    - 3801    + 43    +  49    +  40'
'-----    ------    ----    -----    -----'
' -666     -3800      88      172     1028',
"""