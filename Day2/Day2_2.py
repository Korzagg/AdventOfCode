import re
l = []
for line in open('input','r'):
    m = [int(x) for x in re.split(r'\D+',line.replace("\n",""))]
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if m[i]%m[j] == 0:
                l.append(m[i]/m[j])
            elif m[j]%m[i] == 0:
                l.append(m[j]/m[i])
print(sum(l)) # 191