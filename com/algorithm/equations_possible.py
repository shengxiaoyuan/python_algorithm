from com.algorithm.uf import UF
def equationsPossible(list1: [str]):
    uf = UF(26)
    for str1 in list1:
        if str1[1] == '=':
            uf.union(char2intBase(str1[0]), char2intBase(str1[3]))
    for str1 in list1:
        if str1[1] == '!':
            flag = uf.connected(char2intBase(str1[0]), char2intBase(str1[3]))
            if not flag:
                return False
    return True


def char2intBase(char: str):
    return ord(char) - ord('a')
if __name__ == '__main__':
    eq=['a==b','c==d','e!=f']
    print(equationsPossible(eq))
