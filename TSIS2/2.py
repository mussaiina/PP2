s = input()

def interpret(s):
    x = s.replace("()", "o")
    y = x.replace("(al)", "al")
    return y

print(interpret(s))