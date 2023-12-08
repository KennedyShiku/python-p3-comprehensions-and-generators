#!/usr/bin/env python3

def return_evens(num_list):
    returned_numbers = []
    for i in num_list:
        if i % 2 == 0:
             returned_numbers.append(i)
    return returned_numbers 

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]



