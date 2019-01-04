exec('''d=e=z=0
a,f=input(),[0]*999
while d<len(a):
	m=a[d]A'>':e+=1A'<':e-=1A'+':f[e]+=1A'-':f[e]-=1A'.':print(chr(f[e]),end='')A',':f[e]=ord(input())A'[':z=dA']' and f[e]!=0:d=z
	d+=1'''.replace('A','\n	if m=='))