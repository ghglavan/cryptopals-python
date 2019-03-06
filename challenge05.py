import itertools
import challenge02 as c2

def encrypt(message, key):
    key = key * (int(len(message)/len(key)) + 1)
    key = key[:len(message)]
    return c2.fixed_xor(message.encode("utf-8"), key.encode("utf-8"))

if __name__ == "__main__":
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    enc = encrypt(message, key)

    assert expected == encrypt(message, key)