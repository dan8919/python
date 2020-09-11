#가장 많이 등장하는 문자 체크

word = "testk"
def highFrequencyLetterCount(word):

    map = {}
    for alphabet in word:


        if map.get(alphabet) == None:
            map[alphabet] = 1

        else:
            map[alphabet] += 1


        print("2map=>", map)
    return -1

print(highFrequencyLetterCount(word))