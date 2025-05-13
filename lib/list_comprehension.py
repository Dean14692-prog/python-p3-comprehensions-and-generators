#!/usr/bin/env python3

def return_evens(num_list):
    even_list=[n for n in num_list if n % 2 == 0]
    return even_list
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    result = []
    for sentence in sentence_list:
        result.append(sentence + '!')
    return result
    
    pass