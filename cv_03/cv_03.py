import re


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
    file = open(path, "r", encoding="utf-8")
    letterCounts = {}
    wordsCounts = {}
    letters = file.read()
    words = letters.split()
    for letter in letters:
        if letter.isalpha():
            if letter.lower() in letterCounts:
                letterCounts[letter.lower()] += 1
            else:
                letterCounts[letter.lower()] = 1
    for word in words:
        word = re.sub(r'\W+', '', word)
        word = word.lower()
        if word in wordsCounts:
            wordsCounts[word] += 1
        else:
            wordsCounts[word] = 1
    file.close()
    return wordsCounts, letterCounts


def get_words(n, m, wordsStructure):
    words = {}
    sortedWords = {k: v for k, v in sorted(
        wordsStructure.items(), key=lambda item: item[1], reverse=True)}
    number = n
    for word in sortedWords:
        if number == 0:
            break
        if len(word) >= m:
            words[word] = wordsStructure[word]
            number -= 1
    return words


def cypher(pathIn, pathOut):
    fileIn = open(pathIn, "r")
    fileOut = open(pathOut, "w")
    result = ""
    key = "VINEA"
    for i, word in enumerate(fileIn.read()):
        if word.isalpha():
            posun = ord(key[i % len(key)]) - ord("A")
            if word.isupper():
                result += chr((ord(word) - ord('A') + posun) % 26 + ord('A'))
            else:
                result += chr((ord(word) - ord('a') + posun) % 26 + ord('a'))
        else:
            result += word
    fileOut.write(result)


def decypher(pathIn, pathOut):
    fileIn = open(pathIn, "r")
    fileOut = open(pathOut, "w")
    result = ""
    key = "VINEA"
    for i, word in enumerate(fileIn.read()):
        if word.isalpha():
            posun = ord(key[i % len(key)]) - ord("A")
            if word.isupper():
                result += chr((ord(word) - ord('A') - posun) % 26 + ord('A'))
            else:
                result += chr((ord(word) - ord('a') - posun) % 26 + ord('a'))
        else:
            result += word
    fileOut.write(result)


if __name__ == "__main__":
    print(factorize(15))
    print(factorize(10))
    print()
    #print(factorize(45))
    #print(factorize(123))
    #print(factorize(14))
    queen(10, 10, 7, 5)
    print()
    #queen(8, 8, 3, 4)
    #censor_number(13, 2)
    words, letters = text_analysis("cv_03/book.txt")
    print(letters)
    
    print(get_words(5, 5, words))
    cypher("cv_03/testSifraIn.txt", "cv_03/testSifraOut.txt")
    decypher("cv_03/testSifraOut.txt", "cv_03/testDesifraOut.txt")
