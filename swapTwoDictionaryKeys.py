def swapTwoDictionaryKeys(mapping, keyA, keyB):
    if keyA in mapping and keyB in mapping:
        mapping[keyA],mapping[keyB]=mapping[keyB],mapping[keyA]
    return mapping   
