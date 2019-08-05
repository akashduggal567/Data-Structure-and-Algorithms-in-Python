"""Brian Karnighan Algo"""

def count_set_bits(num):
    result = 0
    """change rightmost bit at each iteration to 0"""
    """
    5 -->101    101 100 000 
    """
    while(num>0):
        num = num&num-1  # num=101 num-1=100  num&num-1=100     num=100 num-1 = 011   num&num-1=000
        result+=1
    print(result)

count_set_bits(5)

""" Time complexity --> O(number of set bits) """


""" Look-up technique """
num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];


def count_set_bits_look(num):
    nibble = 0;
    if (0 == num):
        return num_to_bits[0];

    # Find last nibble
    nibble = num & 0xf;

    # Use pre-stored values to find count
    # in last nibble plus recursively add
    # remaining nibbles.

    return num_to_bits[nibble] + count_set_bits_look(num >> 4)



count_set_bits_look(5)