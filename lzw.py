def LZW_encode(init_dict, sequence):
    encode_table = []
    encode_list = []
    for i in init_dict.items():
        encode_table.append([i[0], i[1]])
    init_char = ''
    init_char = init_char + sequence[0]
    index_encode_table = len(encode_table)
    next_char = ''
    for i in range(len(sequence)):
        flag = 0
        if i != len(sequence) - 1:
            next_char = next_char + sequence[i + 1]
        for j  in range(len(encode_table)):
            if str(init_char + next_char) == str(encode_table[j][0]):
                flag = 1
        if flag == 1:
            init_char = str(init_char + next_char)
        else:
            for k in range(len(encode_table)):
                if init_char == encode_table[k][0]:
                    encode_list.append(encode_table[k][1])
            index_encode_table = index_encode_table + 1
            encode_table.append([str(init_char + next_char), index_encode_table])
            init_char = next_char
        next_char = ''
    for i in range(len(encode_table)):
        if sequence[-1] == encode_table[i][0]:
            encode_list.append(encode_table[i][1])
    print("Alphabet", end = "\t")
    print("Index")
    print("-------------------------------")
    for i in range(len(encode_table)):
        for j in range(2):
            print("  ", encode_table[i][j], end = "\t\t")
        print()
    encoded_sequence = ''
    for i in range(len(encode_list)):
        encoded_sequence = encoded_sequence + str(encode_list[i]) + ' '
    print("Encoded output sequence for the sequence " + sequence + " is: " + encoded_sequence)
    return [init_dict, encode_list]
    


dictionary = {chr(i): i for i in range(127)}
sequence = "DDCDDCDDCDDCDDCDDCDDCDDCX"
master_directory = LZW_encode(dictionary, sequence)
