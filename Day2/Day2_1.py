import re
l = []
for line in open('input','r'):
    m = [int(x) for x in re.split(r'\D+',line.replace("\n",""))]
    l.append(max(m)-min(m))
print(sum(l))
