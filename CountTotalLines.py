"""
Counts total lines, as in lines of iambic pentameter,
for all important characters in Romeo & Juliet.
"""

from collections import defaultdict

# Find start of play (skip title and character list)
def FindPlayStart(lines):
    for i in range (0, len(lines)):
        if lines[i][:5] == "SCENE":
            return i
    return -1

# Read in list of characters
charsource = open(snakemake.input[1], 'r')
chars = charsource.readlines()
charsource.close()

# Remove newlines
for i in range (0, len(chars)):
    chars[i] = chars[i].rstrip('\n')

# Count each character's lines
chars_dict = defaultdict(int)
playsource = open(snakemake.input[0], 'r')
lines = playsource.readlines()
i = FindPlayStart(lines)
while i < len(lines):
    # Get line and strip to compare with chars list 
    line = lines[i].rstrip('\n').rstrip('.').lstrip()
    if line in chars:
        # If char name found, count how many lines follow
        i += 1
        if i >= len(lines):
            break
        nextline = lines[i]
        while nextline != "\n":
            chars_dict[line] += 1
            i += 1
            if i >= len(lines):
                break
            nextline = lines[i]
    else:
        i += 1

# Output to file
output = open(snakemake.output[0], 'w')
for c, f in chars_dict.items():
    output.write(c + "\t" + str(f) + '\n')
