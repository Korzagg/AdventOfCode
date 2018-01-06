import requests
# https://oeis.org/A141481/b141481.txt
val = 347991  # 349975
for line in requests.get("https://oeis.org/A141481/b141481.txt").text.split("\n"):
    if line.startswith("#"):
        continue
    a = int(line.split(" ")[1])
    if a >= val:
        print(a)
        break
