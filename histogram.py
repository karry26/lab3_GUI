from collections import defaultdict
import re
import matplotlib.pyplot as plt

def hist(ans,file_path):
	file = open(file_path, "r")
	banned = defaultdict(lambda:0)
	result = defaultdict(lambda:0) 
	  
	i = 0
	  
	# create map of banned words
	S2="a an the and was aboard about above across after against along amid among around at before behind below beneath beside between beyond by down during except for from in into like near of off on onto out over past since through throughout to toward under underneath until unto up upon with within without"  
	while i < len(S2):  
	  
	    s = ""  
	    while i < len(S2) and S2[i] != ' ':  
	        s += S2[i] 
	        i += 1
	          
	    i += 1
	    banned[s] += 1
	    
	numlines=0
	   
	for line in file: 
	    
	    for li in line.split('.'):
	    #print(line.rstrip('\n'))
		    if(li=='\n'):continue
		    numlines+=1
		    res = re.findall(r'\w+',li)
		    n=len(res)
		    i=0      
		    while i<n:
		        s=res[i].lower()
		        if(banned[s]==0):
		            result[s]+=1
		        i+=1
	
	
	maxfrequent = max(result, key=result.get) 
	minfrequent = min(result, key=result.get)
	
	histlist=[]
	for i in result.values():
	    histlist.append(i)

	plt.xlabel('frequency range')
	plt.ylabel('total no of words')
	plt.title('freq vs words')
	
	#plt.bar(result.keys(), result.values(), width=.5, color='g')
	plt.hist(histlist,bins=5,rwidth=.70,color='g')
	plt.savefig('histogram.png')
	ans.append([maxfrequent,minfrequent,numlines])
        
