import random
import time

def generate_random_sentence(words, length):
    sentence = " ".join(random.choices(words, k=length))
    return sentence

def calculate_typing_speed(sentence, elapsed_time):
    words = sentence.split()
    num_words = len(words)
    words_per_minute = (num_words / elapsed_time) * 60
    return words_per_minute

def main():
    words = ["hello", "world", "python", "programming", "speed", "typing", "test", "challenge", "practice", "coding"]
    sentence_length = 5  # You can change the number of words in the sentence
    sentence = generate_random_sentence(words, sentence_length)

    print("Type the following sentence as fast as you can:")
    print(sentence)

    input("Press Enter to start the timer...")
    start_time = time.time()

    user_input = input("Type the sentence: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    if user_input.strip() == sentence:
        words_per_minute = calculate_typing_speed(sentence, elapsed_time)
        print(f"Congratulations! You typed the sentence correctly.")
        print(f"Your typing speed: {words_per_minute:.2f} words per minute.")
    else:
        print("Oops! Your input does not match the given sentence.")

if __name__ == "__main__":
    main()

