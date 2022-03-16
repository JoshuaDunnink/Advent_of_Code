"""find has starting with 5 zeros"""
from hashlib import md5


def determine_hash_five_leading_zeros(string):
    iterator = 1
    while True:
        hex_value = md5((string + str(iterator)).encode()).hexdigest()
        if hex_value[:5] == "00000":
            return iterator
        else:
            iterator += 1


print(determine_hash_five_leading_zeros("bgvyzdsv"))
