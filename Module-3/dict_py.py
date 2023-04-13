l=["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
a1=input('enter a word from above list')
c = {}
for i in l:
  count = 0
  for j in i.split():
    if j == a1:
      count = count+1
  c[count]=i

d = []
for s in sorted(c):
  d.append(c[s])
d.reverse()
print (d)
