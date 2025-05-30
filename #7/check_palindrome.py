Str1 = "A manhello, a plan, a canal: Panama"


def isPalidrome(Str1, s: str) -> bool:
    if s:
        result = []
        for c in s.lower():
            result.append(c)
        if result == result[::-1]:
            print("done")
            return result
        else:
            print("no")

    else:
        return True
