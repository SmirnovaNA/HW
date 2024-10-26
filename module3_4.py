def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word in other_words:
            same_words.append(other_words)
            return(same_words)
    print(same_words)
single_root_words('low', 'lower')
