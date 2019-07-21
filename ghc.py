import os
d={12:["1",0],23:["2",0],34:["3",0]}
vote=[0]*10
while(True):
	print(vote)
	a=str(input())
	b=str(input())
	count=0
	for k in d.keys():
		if(str(k)==a):
			if(d[k][0]==b and d[k][1]==0):	
				c=int(input())
				vote[c]=vote[c]+1		
				print("Voted Successfully")
				os.system("espeak 'Voted Successfully'")
				d[k][1]=1
				break
			elif(d[k][0]==b and d[k][1]==1):
				print("Voted already!")
				os.system("espeak 'Voted already'")
				break	
			else:	
				count=0
				while(count<3):
					print("Secret code mismatch!!!!")
					b=str(input())
					if(d[k][0]!=b):
						count=count+1
					else:
						c=str(input())
						vote[c]=vote[c]+1	
						print("Voted Successfully")
						os.system("espeak 'Voted Successfully'")
						break
				if(count==3):
					print("Invalid voter")
				break
	else:
		print("Voter doesn't exist!!")