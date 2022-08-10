from hashtable.hashtable import *
import re


def repeated_word(string):
    words_map = HashTable()
    words = string.replace(",", "").split(" ")
    # words = map(str.strip, string.split(','))
    # words = [x.strip() for x in string.split(",")]
    # pattern = re.compile("^\s+|\s*,\s*|\s+$")
    # words = [x for x in pattern.split(string) if x]
    # words = re.sub(r'\s', '', string).split(',')
    # print(words)

    for i in words:
        i = i.lower()
        words_map.set(i, "1")
        count = len(words_map.get(i))
        if count > 1:
            return i
    return "No Repetition"


if __name__ == '__main__':
    str1 = "Once upon a time, there was a brave princess who..."
    str2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    str3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    r = repeated_word(str1)
    r2 = repeated_word(str2)
    r3 = repeated_word(str3)
    print(r)
    print(r2)
    print(r3)