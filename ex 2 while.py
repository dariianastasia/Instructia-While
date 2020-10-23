temp=0
i=0
p=0
n=0
sumpos=0
sumneg=0
while temp<12:
    temp=eval(input("Introduceti temperatura intr-o luna"))
if temp>=0:
    sumeng+=temp
    n+=1
    i=i+1
if p>0:
    media.pos= float(sumpos/p)
    print(media.pos)
if n>0:
    media.neg=float(sumneg/n)
    print(media.neg)