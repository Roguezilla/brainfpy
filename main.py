exec('''import sys
d=e=z=0
a,f=input(),[0]*999
while d<len(a):
	m=a[d]A'>':e+=1A'<':e-=1A'+':f[e]+=1A'-':f[e]-=1A'.':sys.stdout.write(chr(f[e]))A',':f[e]=ord(sys.stdin.read(1))A'[':z=dA']' and f[e]!=0:d=z
	d+=1'''.replace('A','\n	if m=='))