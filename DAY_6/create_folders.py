# operation modes
# "r" -> only for read the txt
# "w" -> rewrite the txt, important: the previous text is lost
# "a" -> appends the new text at the end of the text (very useful)



text = open("test.txt","w")

text.write("I am the new text\nByeee!")

# writelines() introduce a list of strings in the txt
text.close()

text = open("test.txt","a")

text.write("\nnow we append the new text")

text.close()