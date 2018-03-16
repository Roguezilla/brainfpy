import sys,re
a,c,d,e,f,g,h=[],[],{},0,0,[0 for i in range(50)],sys
for z in ''.join(filter(lambda x:x in '.,[]<>+-',re.sub('\n','',open(h.argv[1],'r').read()))):a.append(z)
for p,m in enumerate(''.join(a)):
  if m=='[':c.append(p)
  if m==']':s=c.pop();d[s]=p;d[p]=s
while e<len(a):
  m=a[e]
  if m=='>':f+=1
  if m=='<':f-=1
  if m=='+':g[f]+=1
  if m=='-':g[f]-=1
  if m=='.':h.stdout.write(chr(g[f]))
  if m==',':g[f]=ord(h.stdin.read(1))
  if m=='[' and g[f]==0:e=d[e]
  if m==']' and g[f]!=0:e=d[e]
  e+=1