def LZ78_encode(dictionary, sequence):
    len_seq = len(sequence)
    index_dir = ['']
    encode_list = list()
    word = ''
    alphabet = list(dictionary.keys())
    codewords = list(dictionary.values())
    for i in sequence:
        word = word + i
        if not word in index_dir:
            index_dir.append(word)
            encode_list.append([index_dir.index(word[:-1]), word[-1]])
            word = ''
        elif i == len_seq:
            encode_list.append([index_dir.index(word), ''])
            word = ''
    for i in range(len(encode_list)):
        for j in range(len(alphabet)):
            if encode_list[i][1] == alphabet[j]:
                encode_list[i][1] = codewords[j]
    print("Index\tCodeword")
    print("------------------------------")
    for i in range(len(encode_list)):
        for j in range(2):
            print("  ", encode_list[i][j], end = "\t")
        print()
    print(index_dir)
    return [encode_list, dictionary, index_dir]


n = 0
dictionary = dict()
sequence = "DDCDDCDDCDDCDDCDDCDDCDDCX"
sequence = "ABBABBABBABBABBABBABBABBX"
master_directory = LZ78_encode(dictionary, sequence)
