from itertools import permutations

def cryptarithmetic(left, right, letters):
    perm = permutations(range(10), len(letters))

    for p in perm:
        right_val = 0
        for i in right:
            right_val = right_val * 10 + p[letters.index(i)]

        left_val = 0
        for w in left:
            partial_left_val = 0
            for i in w:
                partial_left_val = partial_left_val * 10 + p[letters.index(i)]
            left_val += partial_left_val

        if left_val == right_val:
            print(f"{' + '.join(left)} = {right}")

            for word in left:
                for letter in word:
                    print(p[letters.index(letter)], end='')
                print(end='   ')

            for letter in right:
                print(p[letters.index(letter)], end='')

            print()

if __name__ == "__main__":
    statement = "SEND + MORE = MONEY"
    letters = list(filter(lambda a: a.isalpha(), set(statement)))

    left = list(map(lambda a: a.strip(), statement.split('=')[0].split('+')))
    right = statement.split('=')[1].strip()

    cryptarithmetic(left, right, letters)
