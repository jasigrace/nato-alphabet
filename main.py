import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(nato_dictionary)

user_name = input("Enter a word: ").upper()
nato = [nato_dictionary[letter] for letter in user_name]
print(nato)
