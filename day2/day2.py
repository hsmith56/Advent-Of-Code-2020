target,result,result1 = 2020,0,0

with open('input.txt','r') as f:
    lines = f.read().splitlines()

for x in lines:
	rule = x[0:x.index(':')].strip()
	pswd = x[x.index(':')+1::].strip()
	min1 = rule[0:rule.index('-')].strip()
	max1 = rule[rule.index('-')+1:-2].strip()
	letter = rule[-1]
	tot = pswd.count(letter)
	if tot < int(min1) or tot > int(max1):
		pass
	else:
		result += 1

result = 0
for x in lines:
	rule = x[0:x.index(':')].strip()
	pswd = x[x.index(':')+1::].strip()
	pos1 = rule[0:rule.index('-')].strip()
	pos2 = rule[rule.index('-')+1:-2].strip()
	letter = rule[-1]
	#print(pos1,pos2,pswd)
	if pswd[int(pos1)-1] != pswd[int(pos2)-1]:
		if pswd[int(pos1)-1] == letter or pswd[int(pos2)-1] == letter:
			result1 += 1
			print(pswd[int(pos1)-1], pswd[int(pos2)-1],letter)
		else:
			pass

print(result1)