exec("""import sys,re
a,c,d,e,f,g,h=[],[],{},0,0,[0 for i in range(999)],sys
for z in ''.join(filter(lambda x:x in '.,[]<>+-',re.sub('\\n','',open(h.argv[1],'r').read()))):a.append(z)
for p,m in enumerate(''.join(a)):
Y[':c.append(p)
Y]':s=c.pop();d[s]=p;d[p]=s
while e<len(a):
  m=a[e]
Y>':f+=1
Y<':f-=1
Y+':K+=1
Y-':K-=1
Y.':h.stdout.write(chr(K))
Y,':K=ord(h.stdin.read(1))
Y[' and K==0:e=d[e]
Y]' and K!=0:e=d[e]
  e+=1""".replace('Y',"  if m=='").replace('K','g[f]'))
