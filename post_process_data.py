import re
textfile = open('./ictst/data/tools.csv', 'r')
filetext = textfile.read()
textfile.close()
filetext = re.sub(r'"[^"]*(?:""[^"]*)*"', lambda m: m.group(0).replace("\n", "||"), filetext)
filetext = re.sub(r'"[^"]*(?:""[^"]*)*"', lambda m: m.group(0).replace("\r\n", "||"), filetext)
textfile = open('./ictst/data/tools.csv', 'w')
textfile.write(filetext)
textfile.close()
