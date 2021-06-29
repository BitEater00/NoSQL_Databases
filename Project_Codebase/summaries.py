import re

file = open('testsum.txt', 'r').read()
for i in range(2):
    x = re.search("^[0-9]*\s/m/.*", file)

    index = x.group().find('. ')
    summary = x.group()[index+2:]

    print(summary)
    print("\n\n")
