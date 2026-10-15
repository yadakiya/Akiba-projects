
def clean_text(text):
    punctuation = ".,!?;:()[]{}\"'"
    cleaned = ""

    for char in text.lower():
        if char in punctuation:
            cleaned += " "
        else:
            cleaned += char

    return cleaned


def count_words(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return len(words)


def count_characters(text):
    total = 0

    for char in text:
        if not char.isspace():
            total += 1

    return total


def count_vowels_and_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def find_longest_word(text):
    words = clean_text(text).split()

    if len(words) == 0:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def count_word_frequencies(text):
    words = clean_text(text).split()
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def find_repeated_words(text):
    frequencies = count_word_frequencies(text)
    repeated = []

    for word in frequencies:
        if frequencies[word] > 1:
            repeated.append(word)

    return repeated


def find_top_five_words(text):
    frequencies = count_word_frequencies(text)
    top_words = []

    for word, frequency in frequencies.items():
        top_words.append((word, frequency))

    # Sort by frequency, highest first, without external libraries
    for i in range(len(top_words)):
        for j in range(i + 1, len(top_words)):
            if top_words[j][1] > top_words[i][1]:
                top_words[i], top_words[j] = (
                    top_words[j], top_words[i]
                )

    return top_words[:5]


def analyze_text(text):
    vowels, consonants = count_vowels_and_consonants(text)

    return {
        "word_count": count_words(text),
        "character_count": count_characters(text),
        "vowels": vowels,
        "consonants": consonants,
        "longest_word": find_longest_word(text),
        "word_frequencies": count_word_frequencies(text),
        "repeated_words": find_repeated_words(text),
        "top_five_words": find_top_five_words(text)
    }


# Main program
paragraph = input("Enter a paragraph: ")

result = analyze_text(paragraph)

print("\n===== TEXT ANALYSIS =====")
print(f"Words: {result['word_count']}")
print(f"Characters (excluding spaces): {result['character_count']}")
print(f"Vowels: {result['vowels']}")
print(f"Consonants: {result['consonants']}")
print(f"Longest word: {result['longest_word']}")
print(f"Repeated words: {result['repeated_words']}")

print("\nWord frequencies:")
for word, frequency in result["word_frequencies"].items():
    print(f"{word}: {frequency}")

print("\nTop five most frequent words:")
for word, frequency in result["top_five_words"]:
    print(f"{word}: {frequency}")
