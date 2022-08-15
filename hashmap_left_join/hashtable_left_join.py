def left_join(h1, h2):
    output = []
    for key in h1:
        output.append([key, h1[key], h2.get(key)])
    return output
    # return [[key, h1[key], h2.get(key)] for key in h1]


if __name__ == '__main__':
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }

    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    print(left_join(synonyms, antonyms))
