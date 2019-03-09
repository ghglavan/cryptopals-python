import challenge02 as c2
import challenge03 as c3
import itertools
from textwrap import wrap
from base64 import b64decode
from binascii import unhexlify, hexlify


def edit_distance(s1, s2):
    x = unhexlify(c2.fixed_xor(s1.encode("utf-8"), s2.encode("utf-8")))
    bit_sum = 0
    for c in x:
        bit_sum += bin(c).count("1")

    return bit_sum

def do_break_lens(contents):
    n_edit_distance = []
    for key_size in range(2,41):
        cts = [contents[i:i+key_size] for i in range(0, len(contents), key_size)][:4]
        pairs = list(itertools.combinations(cts,2))

        edits = [edit_distance(p1, p2)/ key_size for p1,p2 in pairs]

        e_sum = 0
        for edit in edits:
            e_sum += edit

        n_edit_distance.append((e_sum / len(pairs), key_size))

    return sorted(n_edit_distance)[0]


def do_break_key(key_l, contents):
    _, k_l = key_l
    blocks = [contents[i:i+k_l] for i in range(0, len(contents), k_l)]
    key = []
    a = []
    for i in range(k_l):
        s = hexlify("".join([c[i] for c in blocks if i < len(c)]).encode("utf-8"))
        a.append(s)
        _,_,_,k = c3.decode(s)
        key.append(k[0])

    return "".join(key)

if __name__ == "__main__":
    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    assert edit_distance(s1, s2) == 37

    with open('data06.txt', 'r') as f:
        content = b64decode(f.read()).decode("utf-8")
    
    key_l = do_break_lens(content)
    key = do_break_key(key_l, content)
    print("found key: {}".format(key))
