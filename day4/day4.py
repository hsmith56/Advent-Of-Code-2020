f = open('day4.txt','r')
lines = f.read().split('\n\n')

class Passport:
    def __init__(self, iyr=None, hgt=None, byr=None, cid=None, pid=None, eyr=None, hcl=None, ecl=None):
        self.iyr = iyr
        self.hgt = hgt
        self.byr = byr
        self.cid = cid
        self.pid = pid
        self.eyr = eyr
        self.hcl = hcl
        self.ecl = ecl

good = 0
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
print(good)