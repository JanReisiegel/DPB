def factorize(n):
    '''Vrací rozklad na prvočísla čísla n.'''
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


def queen(n, m, x, y):
    '''
    Vygeneruje hrací pole o velkisti n×m a na pozici x, y umistí dámu.
    Dámu značí písmeno D a místa ohrožená dámou značí *. Zbylá
    neohrožená místa jsou označena '.'.
    '''
    chessboard = []
    for i in range(n+1):
        row = []
        for j in range(m+1):
            if i == x and j == y:
                row.append("D")
            elif i == x or j == y or abs(i - x) == abs(j - y):
                row.append("*")
            else:
                row.append(".")
        chessboard.append(row)
    for row in chessboard:
        print(row.__str__().replace(", ", "").replace("'", "")
              .replace("[", "").replace("]", ""))


def censor_number(n, m):
    for i in range(1, n + 1):
        if str(m) in str(i):
            print("*")
        else:
            print(i)


def text_analysis(path):
    file = open(path, "r")
    letterCounts = {}
    wordsCounts = {}
    letters = list(file.read().lower())
    words = list(file.read().lower().split(' '))
    for letter in letters:
        if letter in letterCounts:
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1
    for word in words:
        if word in wordsCounts:
            wordsCounts[word] += 1
        else:
            wordsCounts[word] = 1
    file.close()
    return letterCounts, wordsCounts


if __name__ == "__main__":
    """print(factorize(15))
    print(factorize(10))
    print(factorize(45))
    print(factorize(123))
    print(factorize(14))
    queen(8, 8, 3, 4)
    censor_number(13, 2)"""
    print(text_analysis("cv_03/book.txt"))
