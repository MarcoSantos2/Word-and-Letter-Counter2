#Create a program that can open, read, and count the words and letters in a .CSV, .docx, and .TXT file

import csv
import docx

def word_letter_counter():
    user_input = input("Please write the full name of the file, including its extension. Make sure the file is in the "
                       "same folder as this program. Files are limited to the following extensions: "
                       ".txt, .csv, and .docx\n")
    try:
        if user_input.endswith('.txt'):
            with open('TextFile.txt') as text:
                lines = text.readlines()
                word_counter = 0
                letter_counter = 0
                for line in lines:
                    list_words = line.split()
                    for word in list_words:
                        word_counter += 1
                        for letter in word:
                            letter_counter += 1

                print(f'This file has {word_counter} words and {letter_counter} letters.')
        if user_input.endswith('.csv'):
            with open('TextCSV.csv', newline='') as csvfile:
                line_reader = csv.reader(csvfile)
                word_list = []
                letter_list = []
                for row in line_reader:
                    for word in row:
                        if word.isalpha():
                            word_list.append(word)
                for letters in word_list:
                    for letter in letters:
                        letter_list.append(letter)
                print(f'This file has {len(word_list)} words and {len(letter_list)} letters.')
        if user_input.endswith('.docx'):
            def getText(filename):
                doc = docx.Document(filename)
                fullText = []
                for para in doc.paragraphs:
                    fullText.append(para.text)
                word_counter = 0
                letter_counter = 0
                for line in fullText:
                    list_words = line.split()
                    for word in list_words:
                        word_counter += 1
                        for letter in word:
                            letter_counter += 1
                print(f'This file has {word_counter} words and {letter_counter} letters.')
            getText('A Silence of Three Parts.docx')
    except:
        print("The file's name is incorrect, please try again.")



word_letter_counter()