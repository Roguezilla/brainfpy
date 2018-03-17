exec("""import sys,re
a,c,d,e,f,g,h=[],[],{},0,0,[0 for i in range(999)],sys
for z in ''.join(filter(lambda x:x in'.,[]<>+-',re.sub('\\n','',open(h.argv[1],'r').read()))):a.append(z)
for p,m in enumerate(''.join(a)):A[':c.append(p)A]':s=c.pop();d[s]=p;d[p]=s
while e<len(a):
  m=a[e]A>':f+=1A<':f-=1A+':g[f]+=1A-':g[f]-=1A.':h.stdout.write(chr(g[f]))A,':g[f]=ord(h.stdin.read(1))A[' and g[f]==0:e=d[e]A]' and g[f]!=0:e=d[e]
  e+=1""".replace('A',"\n  if m=='"))