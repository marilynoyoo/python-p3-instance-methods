#!/usr/bin/env python3

class Person:
    def talk(self):
        print("Hello World!")
        # prints "Hello World!"

    def walk(self):
        print("The person is walking.")
        # prints "The person is walking."
fido = Person()

fido.talk()
# prints "Hello World!"

fido.walk()
# prints "The person is walking."