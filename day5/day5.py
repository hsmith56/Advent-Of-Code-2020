f = open('day5.txt','r')
lines = f.read().split('\n')

p1=p2=0

def seat(string):
    row1 = [x for x in range(0,128)]
    clmns1 = [x for x in range(0,8)]
    row = string[0:7]
    column = string[7::]
    for x in row:
        if x =='F':
            row1 = row1[0:int((len(row1)-1)/2)+1]
        if x == 'B':
            row1 = row1[int((len(row1)-1)/2)+1::]

    for x in column:
        if x =='L':
            clmns1 = clmns1[0:int((len(clmns1)-1)/2)+1]
        if x == 'R':
            clmns1 = clmns1[int((len(clmns1)-1)/2)+1::]

    row1 = row1[0]
    column1 = clmns1[0]
    return row1,column1

seats = []
ids = []
for line in lines:
    x,y = seat(line)
    product = (x*8+y)
    ids.append(product)
    if product > p1:
        p1 = product
    seats.append([x,y])
    
ids.sort()
for id1 in range(84,900):
    if id1 not in ids:
        p2 = id1

print(p1,p2)