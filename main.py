import time
import random


def typing_test(sentence):
    print("Type the following sentence:")
    print(sentence)

    input("Press Enter when you are ready to start...")

    print("\033[A\033[K", end="")  # Clear the previous line in the terminal

    start_time = time.time()

    user_input = input("Type the sentence and press Enter: ")

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    if user_input == sentence:
        print(f"Congratulations! You typed it correctly in {elapsed_time} seconds.")
    else:
        print("Sorry, there were mistakes in your typing. Here's where you went wrong:")
        display_mistakes(sentence, user_input)
        print(f"Total time taken: {elapsed_time} seconds.")


def display_mistakes(correct_sentence, user_input):
    for i in range(min(len(correct_sentence), len(user_input))):
        if correct_sentence[i] != user_input[i]:
            print(f"Error at position {i + 1}: You typed '{user_input[i]}' instead of '{correct_sentence[i]}'")


if __name__ == "__main__":
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and versatile programming language.",
        "Coding is fun and rewarding.",
        "Practice makes perfect.",
        "Hello, world! This is a typing test."
    ]

    selected_sentence = random.choice(sentences)
    typing_test(selected_sentence)



