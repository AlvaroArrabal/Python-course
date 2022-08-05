def say_hello(function):
    def another_function(word):
        print("Hello")
        function(word)
        print("Bye")
    return another_function

@say_hello
def text_upper(text):
    print(text.upper())

def text_lower(text):
    print(text.lower())



text_upper("i am alvaro")

text_lower_hello = say_hello(text_lower)

text_lower_hello("I AM ALVARO")

text_lower("I AM ALVARO")