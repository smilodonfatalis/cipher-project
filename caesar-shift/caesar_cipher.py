import numpy as np
import pandas as pd


def create_dictionary(filename):
    """Import dictionary of words
    Input: list of words in target language
    Output: list of words
    """
    # import dictionary
    dictionary = []
    with open(filename) as file:
        for line in file:
            dictionary.append(line)

    # remove newline
    dictionary = [w.rstrip() for w in dictionary]
    dictionary.pop(len(dictionary)-1)

    return dictionary


def caesar_shift(enc_input, shift, alphabet):
    """Shift text according to key file
    Input: dictionary of keys (created with create_enc_key or decipher key mapping)
    Output: shifted text
    """
    # convert enciphered input to lowercase
    enc_input.lower()
    shifted_text = ''

    for word in enc_input:
        if word in alphabet:
            shifted_text += alphabet[(alphabet.index(word) + shift) % 26]
        else:
            shifted_text += word

    return shifted_text

# create dictionary and set alphabet
eng_dict = create_dictionary('english_dictionary.txt')
alphabet = "abcdefghijklmnopqrstuvwxyz"

# get enciphered input
try:
    enciphered = input('Enter the enciphered text: ')
except Exception:
    print('Input error.')
    exit(1)

# shift text
zero_data = np.zeros(shape=(len(alphabet), 4))
shifted_text = pd.DataFrame(zero_data, columns=['Shifted Text','Total Words','Total Real Words','Word Percentage'])

for i in range(0,len(alphabet)):
    shifted_text.loc[i, 'Shifted Text'] = caesar_shift(enciphered, i, alphabet)
    shifted_text.loc[i, 'Total Words'] = len(enciphered.split(' '))

    # count total real words
    shifted_words = shifted_text.loc[i, 'Shifted Text'].split(' ')
    for word in shifted_words:
        if word in eng_dict:
            shifted_text.loc[i, 'Total Real Words'] += 1

shifted_text['Word Percentage'] = shifted_text['Total Real Words'] / shifted_text['Total Words']

print(shifted_text.iloc[shifted_text['Word Percentage'].idxmax()])
print(shifted_text)
