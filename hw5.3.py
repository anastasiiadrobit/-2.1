import string

text = input("Enter your text: ")

clean_text = ''.join(char for char in text if char not in string.punctuation and not char.isspace())

words = text.split()
capitalized_words = [word.capitalize() for word in words]

hashtag = '#' + ''.join(capitalized_words)

hashtag = hashtag[:140]

print(hashtag)
