import sys, re
o=sys
c=[]
f=open(o.argv[1],'r')
for e in ''.join(filter(lambda x:x in '.,[]<>+-',re.sub('\n','', f.read()))):
  c.append(e)
_,b=[],{}
for p,m in enumerate(''.join(c)):
  if m=="[":_.append(p)
  if m=="]":
    s=_.pop()
    b[s]=p
    b[p]=s
e,d,p= [0 for i in range(9999)],0,0
while d<len(c):
  m=c[d]
  if m=='>':
    p+=1
  if m=='<':
    p-=1
  if m=='+':
    e[p]=e[p]+1
  ifm=='-':
    e[p]=e[p]-1
  if m=='.':
    o.stdout.write(chr(e[p]))
  if m==',':
    e[p]=ord(o.stdin.read(1))
  if m=='[' and e[p]==0:
    d=b[d]
  if m==']' and e[p]!=0:
    d=b[d]
  d+=1
