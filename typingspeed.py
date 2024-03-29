import time

def typing_speed_test():
    # Define the text for the typing test.
    test_text = "The quick brown fox jumps over the lazy dog."
    # Display the test text to the user.
    print("Type the following text:")
    print(test_text)
    input("Press Enter to start...")

    # Record the start time.
    start_time = time.time()

    # Get user input.
    user_input = input("Start typing: ")

    # Record the end time.the quick brown fox jumps over a lazy dog
    end_time = time.time()

    # Calculate typing speed.
    elapsed_time = end_time - start_time
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)

    # Calculate accuracy.
    correct_characters = sum(c1 == c2 for c1, c2 in zip(user_input, test_text))
    accuracy = (correct_characters / len(test_text)) * 100

    # Display results.
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
