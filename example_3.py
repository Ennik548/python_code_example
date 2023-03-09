'''
Написать свою реализацию функции isalpha()
Написать свою реализацию функции islower()
Написать свою реализацию функции istitle()
Написать свою реализацию функции upper()
Написать свою реализацию функции endswith()
Написать свою реализацию функции count()
Написать свою реализацию функции strip()
Написать свою реализацию функции replace()
'''


def k_isalpha(s: str) -> bool:
    i = 0
    while i < len(s):
        if not ("A" <= s[i] <= "Z" or "a" <= s[i] <= "z"):
            return False
        i += 1
    return True


def k_islower(s: str) -> bool:
    i = 0
    if s.isdigit() is True:
        return False
    while i < len(s):
        if "A" <= s[i] <= "Z":
            return False
        i += 1
    return True


def k_istitle(s: str) -> bool:
    i = 0
    j = 0
    while i < len(s.split()):
        if "A" <= s.split()[i][0] <= "Z":
            big_letter = 0
            while j < len(s.split()[i]):
                if "A" <= s.split()[i][j] <= "Z":
                    big_letter += 1
                j += 1
            if big_letter == 1:
                return True
        i += 1
    return False


def k_upper(s: str) -> str:
    i = 0
    res = ""
    while i < len(s):
        if "a" <= s[i] <= "z":
            res += chr(ord(s[i]) - 32)
            i += 1
        else:
            res += s[i]
            i += 1
    return res


def k_endswith(s: str, substring: str) -> bool:
    i = -1
    while i >= - len(substring):
        print(substring[i])
        print(s[i])
        if substring[i] != s[i]:
            return False
        i -= 1
    return True


def k_count(s: str, substring: str) -> int:
    i = 0
    j = 0
    counter = 0
    if len(substring) == 0:
        return len(s) + 1
    while i < len(s):
        if s[i] == substring[0]:
            while j < len(substring):
                if s[i] == substring[j]:
                    i += 1
                    j += 1
                    counter += 1
                else:
                    break
            j = 0
        else:
            i += 1
    return counter // len(substring)


def k_strip(s: str) -> str:
    i = 0
    j = -1
    while i < len(s):
        if s[i] == " " or s[i] == "\n" or s[i] == "\t":
            i += 1
        else:
            while -j >= - len(s):
                if s[j] == " " or s[j] == "\n" or s[j] == "\t":
                    j -= 1
                else:
                    return s[i:len(s) + j + 1]


def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
    i = 0
    j = 1
    res = ""
    k = 0
    if s == "" and oldvalue == "":
        return newvalue
    else:
        while i < len(s):
            if s[i] == oldvalue[0] and k < count:
                i += 1
                while j < len(oldvalue) and i < len(s):
                    if oldvalue[j] == s[i]:
                        j += 1
                        i += 1
                    else:
                        break
                if j == len(oldvalue):
                    res += newvalue
                    j = 1
                    k += 1
                else:
                    res += oldvalue[:j]
                    j = 1
            else:
                res += s[i]
                i += 1
        return res
