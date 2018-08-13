import re
s = input()
k = len(s) - len( re.findall('[\w]', s) )
print(k)
