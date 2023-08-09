#!/usr/bin/python3
import random

def sign(n):
  return {n > 0: "positive", n == 0: "zero", n < 0: "negative"}[True]

number = random.randint(-10, 10)
print(f"{number} is {sign(number)}")
