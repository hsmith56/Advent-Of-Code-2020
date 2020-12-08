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


for x in lines:
	rule = x[0:x.index(':')].strip()
	pswd = x[x.index(':')+1::].strip()
	pos1 = rule[0:rule.index('-')].strip()
	pos2 = rule[rule.index('-')+1:-2].strip()
	letter = rule[-1]
	if x[int(pos1)] == letter or x[int(pos2)]== letter and x[int(pos1)] != x[int(pos2)]:
		result1 += 1
		print(x[int(pos1)], x[int(pos2)],letter)
	else:
		pass

print(result1)