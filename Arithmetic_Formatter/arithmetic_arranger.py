def check(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def arithmetic_arranger(problems,disp=False):
  first=[]
  second=[]
  operator=[]
  output=[]
  diffs=[]
  diffs1=[]
  diffs2=[]
  diffs3=[]
  b=''
  d=''
    
  #check for errors    
  #its easy to observe the possible errors by taking a look at the following return statements
  if(len(problems)>5):
    return("Error: Too many problems.")
  
  for i in problems:
    fail=0
    temp=[]
    temp=i.split()
    
    if (len(temp[1])==1 and (("+" in temp[1]) or ("-" in temp[1]))):
      fail=1
    else:
      return("Error: Operator must be '+' or '-'.")
    
    if (check(temp[0]) and check(temp[2])): 
      fail=2
    else:  
      return('Error: Numbers must only contain digits.')
    
    if (len(temp[0])<=4 and len(temp[2])<=4):
      fail=1
    else:
      return("Error: Numbers cannot be more than four digits.")
    
    first.append(temp[0])
    operator.append(temp[1])
    second.append(temp[2])
  
  #after collecting the input data and separate them accordingly
  #we have to return the final outcome depending on the disp argument
  for i in range(len(first)):
    d=''
    ap=''
    alen=len(first[i])
    blen=len(second[i])
      
    if(operator[i]=='+'):
      ap=str(int(first[i])+int(second[i]))
  
    else:
      ap=str(int(first[i])-int(second[i]))
    
    if(alen>blen):
      diff=alen-blen
      b=first[i].rjust(2+alen)
      c=operator[i]+' '+second[i].rjust(alen)
      e=ap.rjust(2+alen)

      for i in range(2+alen):
        d=d+'-'
        
    else:
      diff=blen-alen
      b=first[i].rjust(2+blen)
      c=operator[i]+' '+second[i].rjust(blen)
      e=ap.rjust(2+blen)
      
      for i in range(blen+2):
        d=d+'-'
        
    diffs.append(b)
    diffs1.append(c)
    diffs2.append(d)
    diffs3.append(e)
    
  diffs='    '.join(diffs)
  diffs=diffs+'\n'
  diffs1='    '.join(diffs1)
  diffs1=diffs1+'\n'
  if(disp==False):
    diffs2='    '.join(diffs2)
    return diffs+diffs1+diffs2

  if(disp==True):
    diffs2='    '.join(diffs2)
    diffs2=diffs2+'\n'
    diffs3='    '.join(diffs3)
    return diffs+diffs1+diffs2+diffs3

    
