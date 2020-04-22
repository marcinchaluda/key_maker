import string


def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    shift_word = ""
    for letter in word:
        letter_index = string.ascii_lowercase.index(letter) + shift
        if letter_index > len(string.ascii_lowercase):
            letter_index = letter_index - len(string.ascii_lowercase)
        elif letter_index < 0:
            letter_index = letter_index + len(string.ascii_lowercase)
        shift_word += string.ascii_lowercase[letter_index]
    return shift_word


def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    if len(word) >= n:
        return word[:n]
    else:
        extended_word = word
        while(len(extended_word) <= n):
            word = shift_characters(word, shift)
            extended_word += word
        return extended_word[:n]


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    mirror_word = ""
    for letter in word:
        mirror_word += string.ascii_lowercase[(len(string.ascii_lowercase) -1) - string.ascii_lowercase.index(letter)]
    return mirror_word


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    word_matrix = []
    for letter in word2:
        word_matrix.append(shift_characters(word1, string.ascii_lowercase.index(letter)))
    return word_matrix


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    concatenated_string = ""
    for letter_index in range(len(matrix[0])):
        letter_sequence = ""
        for word in matrix:
            letter_sequence += word[letter_index]
        if letter_index % 2 != 0:
            letter_sequence = get_reversed_string(letter_sequence)
        concatenated_string += letter_sequence
    return concatenated_string


def get_reversed_string(word):
    letters = []
    for letter in word:
        letters.append(letter)
    reverse_letters = reversed(letters)
    return "".join(reverse_letters)


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    letters = [""] * len(word)
    for index, letter in enumerate(word):
        letter_input_index = index + n
        if n >= 0:
            while letter_input_index >= len(word):
                letter_input_index -= len(word)
        else:
            while letter_input_index <= -len(word):
                letter_input_index += len(word)
        letters[letter_input_index] = letter
    return "".join(letters)


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    square_index_word = ""
    for index, letter in enumerate(word):
        square_index = index ** 2
        if square_index <= len(word):
            square_index_word += word[square_index]
    return square_index_word


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    blocks = []
    block_start = 0
    for letter_index, letter in enumerate(word):
        if block_start <= len(word):
            blocks.append(word[block_start: block_start + block_length])
            block_start += block_length
    even_blocks_word = [block for index, block in enumerate(blocks) if index % 2 == 0]
    return "".join(even_blocks_word)


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    reduced_word = [""] * len(word[:n])
    letter_index = 0
    for index, letter in enumerate(word[:n]):
        letter_index = index - (n // 3)
        if letter_index < 0:
            letter_index = n + letter_index
        reduced_word[letter_index] = letter
    return get_reversed_string("".join(reduced_word))


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
