import re
re.purge()
print('regular expression')
re.compile()
re.findall()

string = "some digits: 888"
pattern = re.compile(r"\d")     # \d 是任何數字的表達
re.findall(pattern, string)