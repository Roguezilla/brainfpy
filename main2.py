import sys,re
c,f,_,b,d,p,e=[],open(sys.argv[1],'r'),[],{},0,0,[0 for i in range(9999)]
for z in ''.join(filter(lambda x:x in '.,[]<>+-',re.sub('\n','',f.read()))):c.append(z)
for p,m in enumerate(''.join(c)):
  if m=='[':_.append(p)
  if m==']':s=_.pop();b[s]=p;b[p]=s
while d < len(c):
  m=c[d]
  if m=='>':p+=1
  if m=='<':p-=1
  if m=='+':e[p]+=1
  if m=='-':e[p]-=1
  if m=='.':sys.stdout.write(chr(e[p]))
  if m==',':e[p]=ord(sys.stdin.read(1))
  if m=='[' and e[p]==0:d=b[d]
  if m==']' and e[p]!=0:d=b[d]
  d+=1