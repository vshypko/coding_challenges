# Note that we can reuse the result from this function after calling it once by saving the data.
# So, there is no need to compute the hashmap each time we call get_capitalized_anagrams.
def get_hashmap(dictionary):
    # create a hashmap for each word in dictionary
    hashmap = {}

    for w in dictionary:
        # key is the lowercase sorted word (so that we can assign anagrams to the same bucket)
        key = ''.join(sorted(w.lower()))
        if key not in hashmap.keys():
            hashmap[key] = list()
        hashmap[key].append(w.lower())

    return hashmap


def get_capitalized_anagrams(word):
    # word is a randomly selected word from the English dictionary
    # (function written by the colleague)
    sorted_word = ''.join(sorted(word.lower()))
    capitalized_indices = set()

    for i in range(len(word)):
        if word[i].isupper():
            capitalized_indices.add(i)

    # See note above. After the first call to get_hashmap, we can access the saved data
    # instead of recomputing every time.

    dictionary = list()
    # assuming dictionary is English dictionary
    # dictionary = EnglishDictionary
    # to make sure there are no repetitions (which should not normally happen anyway)
    anagrams = list(set(get_hashmap(dictionary)[sorted_word]))

    if capitalized_indices:
        for i in range(len(anagrams)):
            word_list = list(anagrams[i])
            for index in capitalized_indices:
                word_list[index] = word_list[index].upper()
            anagrams[i] = ''.join(word_list)

    return anagrams
