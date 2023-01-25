txt: str = "I am a teacher and I love to inspire and teach people"
t = txt.split()  # split is used to separate the text
y = set(t)  # the list which we split is push into set values to get unique words
print("the unique words are:", y)
print("the length of unique words is", len(y))  # len is function which is used to print length of string
