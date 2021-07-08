colors = ["black", "orange", "red", "blue", "purple", "yellow"]
with open("colors.txt", "w") as f:
    for clr in colors:
        f.write(clr + '\n')
    
x = open('colors.txt')
print(x.read().strip())