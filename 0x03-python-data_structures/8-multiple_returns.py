#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first = ""

    if sentence == "":
        first = None
    if sentence != "":
        first = sentence[0]
        for item in range(len(sentence)):
            length += 1
    return length, first
