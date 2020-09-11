string = "1+2*(3-4)"

#숫자와 괄호를 분리 해주는 식

def stringTokenzier(string):
    result = []
    for char in string:
        if char in ["+","-","*","/","(",")"]:
            result.append(char)
        result.append(char)

    return result

result = stringTokenzier(string)
print("result=>",result)
