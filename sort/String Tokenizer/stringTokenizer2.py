string = "1+2*(3 -4)"

#숫자와 괄호를 분리 해주는 식

def stringTokenzier(string,deli):
    result = []
    accu = ""
    for char in string:

        if char in deli: #"+-*/()"

            result.append(char)
        else:
            accu = accu+char
            if accu != " ":
                result.append(accu)
                accu =""


    return result

result = stringTokenzier(string,"+-*/()")
print("result=>",result)
