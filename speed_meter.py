import time

def calculate_wpm(start_time, end_time, sentence):
    words = sentence.split()
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = len(words) / minutes
    return wpm

def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    print("Type the following sentence as fast as you can:")
    print(sentence)
    input("Press Enter to start...")

    start_time = time.time()

    user_input = input("Type the sentence: ")

    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, sentence)

    print(f"You typed at a speed of {wpm:.2f} words per minute.")

if __name__ == "__main__":
    main()
