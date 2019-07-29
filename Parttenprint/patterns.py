#first
for j in range(4):
    for i in range(4-j):
        print("#",end=" ")
    print()

print()
#second
for j in range(4):
    for i in range(j+1):
        print("#",end=" ")
    print()

print()
#third
for j in range(4):
    for i in range(4):
        print("#",end=" ")
    print()

#first

# 1 2 3 4
# 2 3 4
# 3 4
# 4
for j in range(1,5):
    for i in range(4-j):
        print(i,end=" ")
    print()

# A P Q r
# A B A r
# A B C r
#A b c d
