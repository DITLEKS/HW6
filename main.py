import requests
from collections import Counter


def get_text(url):
    response = requests.get(url)
    return response.text


def count_word_frequencies(text, words):
    word_counts = Counter(text.split())
    return {word: word_counts.get(word, 0) for word in words}


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    text = get_text(url)

    with open(words_file, "r") as file:
        unique_words = {line.strip() for line in file if line.strip()}

    frequencies = count_word_frequencies(text, unique_words)

    print(frequencies)


if __name__ == "__main__":
    main()