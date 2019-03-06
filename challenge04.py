import challenge03 as c3

def find_enc(content):
    scores = []
    for line in content:
        if line[-1] == '\n':
            line = line[:-1]
        scores.append(c3.decode(line))

    return max(scores)


if __name__ == "__main__":
    with open('data04.txt', 'r') as f:
        content = f.readlines()
        print(find_enc(content))