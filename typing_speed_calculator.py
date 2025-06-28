# Starter code for Typing Speed Calculator in Python
import time

def calculate_speed_and_accuracy(original_text, user_input, start_time, end_time):
    elapsed_time = end_time - start_time
    words = user_input.split()
    word_count = len(words)
    wpm = (word_count / elapsed_time) * 60

    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(original_text) and c == original_text[i])
    accuracy = (correct_chars / len(original_text)) * 100

    return wpm, accuracy

def main():
    test_text = "Python is an interpreted high-level programming language."
    print("Type the following text as quickly and accurately as you can:")
    print(f"\n{test_text}\n")
    input("Press Enter to start...\n")

    start = time.time()
    user_input = input("Start typing: ")
    end = time.time()

    wpm, accuracy = calculate_speed_and_accuracy(test_text, user_input, start, end)

    print(f"\nYour typing speed: {wpm:.2f} WPM")
    print(f"Your accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()



