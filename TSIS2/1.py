def IPaddress(s):
    return s.replace(".", "[.]")
    

s = input()
print(IPaddress(s))