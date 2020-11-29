z=a=x=0
c,m=input(),[0]*999
while z<len(c):exec("a+=1|a-=1|m[a]+=1|m[a]-=1|print(chr(m[a]))|m[a]=ord(input())|x=z|if m[a]:z=x".split("|")["><+-.,[]".find(c[z])]);z+=1
