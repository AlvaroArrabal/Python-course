text = input("Introduce a text: ")
a = input("Introduce one letter: ")
b = input("Introduce one letter: ")
c = input("Introduce one letter: ")

miList = (a,b,c)

text = text.lower()

na = text.count(miList[0])
nb = text.count(miList[1])
nc = text.count(miList[2])

print(f"The letter {miList[0]} appears {na} times")
print(f"The letter {miList[1]} appears {nb} times")
print(f"The letter {miList[2]} appears {nc} times")

totalWords = text.split()

print(f"The text have {len(totalWords)} words")

print(f"The first letter of the text is {totalWords[0][0]} and the last letter is {totalWords[-1][-1]}")

totalWords.reverse()

reverseText = " ".join(totalWords)

print(reverseText)

res = "python" in text

print(f"Is the word 'python' in your text? {res}")