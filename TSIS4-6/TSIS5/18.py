with open('input.txt') as f:
    words = f.read()
    x = words.replace(",", " ")
    
print(len(x.split()))