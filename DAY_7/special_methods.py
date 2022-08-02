class CD:

    def __init__(self,author,title,songs):
        self.author = author
        self.title = title
        self.songs = songs
    
    def __str__(self):                                          # __str__ defines how I want the string to work
        return f"Albun: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.songs

    def __del__(self):
        print("CD deleted")

myCD = CD("Pink Floyd","The Wall",24)


print(myCD)
print(len(myCD))

del myCD                                                        # Deletes something