def frequencies(ciphertext):
    freq = [0] * 26
    for i in ciphertext:
        int_letter = ord(i) - ord('A')
        freq[int_letter] += 1
    return freq


def most_freq(my_str):
    freq = frequencies(my_str)
    print("letter frequencies")
    print(freq)
    sorted = []
    while (len(my_str) > 0):
        freq = frequencies(my_str)
        m = chr(freq.index(max(freq)) + 65)
        # m = chr(freq.index(freq) + 65)
        sorted.append(m)
        my_str = remove_all(my_str, m)
    return sorted


def remove_all(str, letter):
    my_list = list(str)
    while (letter in my_list):
        my_list.remove(letter)
    #	print(my_list)
    str = ''
    return str.join(my_list)


def separate(ciphertext, key_size):
    list_key = []
    l = len(ciphertext)
    list_key_str = []
    for j in range(key_size):
        key_str = ""
        key = []
        for i in range(0, l, key_size):
            if (i + j < l):
                key_str += ciphertext[j + i]
                key.append(ciphertext[j + i])
        list_key.append(key)
        list_key_str.append(key_str)

    return list_key, list_key_str


def main():
    key_size = int(input("enter key size "))
    ciphertextInput = input("input ciphertext ")
    ciphertextInput = ciphertextInput.replace(" ", "")
    ciphertextInput = ciphertextInput.replace("\t", "")
    ciphertextInput = ciphertextInput.replace(",", "")
    ciphertextInput = ciphertextInput.replace(";", "")
    ciphertextInput = ciphertextInput.replace("!", "")
    ciphertextInput = ciphertextInput.replace(":", "")
    ciphertextInputNoSpaces = ciphertextInput.replace(".", "")
    print("after removing all whitespaces and punctuations")
    print(ciphertextInputNoSpaces)
    list_key, list_key_str = separate(ciphertextInputNoSpaces, key_size)
    print(list_key)
    print(list_key_str)
    

    for i in range(key_size):
        m = most_freq(list_key_str[i])
        print("sorted for keyword letter", i + 1)
        print(m)
           # to delete


main()

