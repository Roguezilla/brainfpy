import sys, re
def B(c): 
  _,b=[],{}
  for p,i in enumerate(c):
    if i=="[": _.append(p)
    if i=="]":
      s= _.pop()
      b[s]=p
      b[p]=s
  return b
def r(F):
  C=[]
  with open(F,'r') as f:
    for e in ''.join(filter(lambda x:x in '.,[]<>+-', re.sub('\n','', f.read()))):
      C.append(e)
  b=B(''.join(C))
  c,p,q=[0 for i in range(9999)],0,0
  while p<len(C):
    g=C[p]
    if g=='>':
      q+=1
    elif g=='<':
      q-=1
    elif g=='+':
      c[q]+=1
    elif g=='-':
      c[q]-=1
    elif g=='.':
      sys.stdout.write(chr(c[q]))
    elif g==',':
      c[cellptr]=ord(sys.stdin.read(1))
    elif g=='[' and c[q]==0:
      p=b[p]
    elif g==']' and c[q]!=0:
      p=b[p]
    p+=1
r(sys.argv[1])
