#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("приведенный список является: ")
print(my_list)
list_length = len(my_list)
sumOfElements = 0
for i in range(list_length):
    dumOfElements = sumOfElements + my_list[i]

print("Sum of all the elements in the is:", sumOfElements)


