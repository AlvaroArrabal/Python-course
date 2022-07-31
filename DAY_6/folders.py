# Input / Output

text = open('test.txt')         # We open the txt

one_line = text.readline()      # Read one line
print(one_line)

# readlines() makes a list with each line

print(text.read())              # Now we read de txt


text.close()                    # we have to close the txt at the end of the program
