def function(w): 
   l=[]
   tmp=[]
   for i in w:
      l.append(ord(i))
      tmp.append(i)
   l.reverse()    
   flag=0
   l.sort(reverse=True)
   l=[chr(i) for i in l]
   s=''

   w=s.join(l)
   if l!=tmp:
      tmp.reverse()
     
      un=[]
      for i in range(len(tmp)-1):
         if tmp[i]>tmp[i+1]:
            un = tmp[0:i+2]
            un.sort()
            # prv = un[un.index(tmp[i+1])+1]
            uniq_prv=[]
            
            for j in un:
               if j not in uniq_prv:
                  uniq_prv.append(j)
           
            prv = uniq_prv[uniq_prv.index(tmp[i+1])+1]
            # print(prv)
            un.pop(un.index(prv))
            un1=[]
            val=i+2
            un1=tmp[val:len(tmp)]
            un1.reverse()
           
            un1.append(prv)
           
            un=un1+un
            s=''
            word=s.join(un)
            return word
      # return w
   else:
      return 'no answer'
if __name__ == "__main__":
   w='zxvuutttrrrpoookiihhgggfdca'
   w='ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvlmcpapfbmzxmftrkkqvkpflxpezzapllerxyzlcf' 
   w='aba'
   print(function(w))
