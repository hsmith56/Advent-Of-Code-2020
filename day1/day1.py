target,result = 2020,0

with open('input.txt','r') as f:
    lines = f.read().splitlines()

for x in range(0,len(lines)-2):
	for y in range(x+1,len(lines)-1):
		for z in range(x+2,len(lines)):
			if int(lines[x]) + int(lines[y]) + int(lines[z]) == target:
				result = int(lines[x])*int(lines[y])*int(lines[z])
				print(int(lines[x]),int(lines[y]),int(lines[z]))
print(result)