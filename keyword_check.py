from collections import defaultdict
import re

def keyword_check(ans,path_file1,path_file2):
    file1=open(path_file1,"r")
    file2=open(path_file2,"r")
    include_words = defaultdict(lambda:0)
    result = defaultdict(lambda:0) 
      
    i = 0
    lines_with_words=[]  
    # create map of banned words
    for line in file2: 
        # reading each word 
        res = re.findall(r'\w+',line)
        n=len(res)
        i=0      
        while i<n:
            s=res[i].lower()
            include_words[s]=1
            i+=1
        
    for line in file1: 
        # reading each word 
        for line1 in line.split('.'):
            if(line1=='\n'):
                continue
            res = re.findall(r'\w+',line1)
            #print(res)
            n=len(res)
            i=0  
            flag=0    
            while i<n:
                s=res[i].lower()
                if(include_words[s]==1):
                    flag=1
                i+=1
            if(flag==1):
                lines_with_words.append(line1)
                
    ans.append(lines_with_words)

    
    
            
