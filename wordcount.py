def count_words(text):
    # Split the text into words using whitespace as the separator
    words = text.split()
    # Return the number of words
    return len(words)

# Example usage
if __name__ == "__main__":
    sample_text = "This is a sample text to count the number of words."
    word_count = count_words(sample_text)
    print(f"The number of words in the given text is: {word_count}")

