f = open('day4.txt','r')
lines = f.read().split('\n\n')

class Passport:
    def __init__(self, iyr=None, hgt=None, byr=None, pid=None, eyr=None, hcl=None, ecl=None):
        try:
            self.iyr = int(iyr)
            self.hgt = hgt
            self.byr = int(byr)
            self.pid = pid
            self.eyr = int(eyr)
            self.hcl = hcl
            self.ecl = ecl
        except:
            pass

    def isValid(self) -> bool:
        try:
            if self.byr < 1920 or self.byr > 2002:
                return False

            if self.iyr < 2010 or self.iyr > 2020:
                return False

            if self.eyr < 2020 or self.eyr > 2030:
                return False

            if self.hgt[-2::] == 'cm':
                height= int(self.hgt[:-2])
                if height < 150 or height > 193:
                    return False

            else:
                height= int(self.hgt[:-2])
                if height < 59 or height > 76:
                    return False

            if self.hcl[0] != '#':
                return False

            if len(self.hcl) != 7:
                return False

            if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

            if len(self.pid) != 9:
                return False
        except:
            return False
        return True

    def print(self):
        return (self.iyr, self.hgt, self.byr,  self.pid, self.eyr, self.hcl, self.ecl)

good = 0
valid = []
for x in lines:
    x = x.replace('\n',' ')
    if x.find('iyr') < 0:
        continue
    if x.find('hgt') < 0:
        continue
    if x.find('byr') < 0:
        continue
    if x.find('pid') < 0:
        continue
    if x.find('eyr') < 0:
        continue
    if x.find('hcl') < 0:
        continue
    if x.find('ecl') < 0:
        continue
    good += 1
    valid.append(x)

part2 = 0

for pp in valid:
    test = pp.replace(' ', ':').split(':')
    k = [test[x] for x in range(0,len(test),2)]
    v = [test[x] for x in range(1,len(test),2)]
    d = {}
    for x in range(len(k)):
        d[k[x]] = v[x]

    # for k,v in d.items():
    #     print(k,v)
    tempP = Passport(d['iyr'],d['hgt'],d['byr'],d['pid'],d['eyr'],d['hcl'],d['ecl'])
    if tempP.isValid():
        part2 += 1

print(part2)