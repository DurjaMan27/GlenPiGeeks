#DesignerDoorMat.py

n = 7
m = 21

for i in range(0, (n//2)*2, 2):
    design = ".|."
    multiple = design * i
    print(((design)+multiple).center(m, '-'))
print(("WELCOME").center(m, '-'))
for i in range(((n//2)*2)-2, -1, -2):
    design = ".|."
    multiple = design * i
    print(((design)+multiple).center(m, '-'))    