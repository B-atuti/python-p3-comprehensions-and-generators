#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n%2 == 0]

def make_exclamation(sentence_list):
    return [n + '!' for n in sentence_list]

numbers = [1,3,5,7,8,9]
even_numbers = return_evens(numbers)
print("Even numbers:", even_numbers)

sentences = ["Hello", "I'm doing great", "Python is fun"]
exclamations = make_exclamation(sentences)
print("Exclamations:", exclamations)