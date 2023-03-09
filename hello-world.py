class Hello:
    def say_hello(self, to: str):
        print(f"Hello, {to}!")

hello_obj = Hello()
hello_obj.say_hello("World")

if (__name__ == "__main__"):
    hello_obj.say_hello("Main")