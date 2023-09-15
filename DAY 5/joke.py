import pyjokes

def generate_joke():
    joke = pyjokes.get_joke()
    return joke

if __name__ == "__main__":
    while True:
        input("Press Enter to get a random joke...")
        joke = generate_joke()
        print(joke)
