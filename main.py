import pandas

# Read the CSV file with Pandas module

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# It creates a dictionary in this format

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# It lists of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
