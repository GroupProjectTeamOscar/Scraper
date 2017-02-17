import re 

def bagOfWords(input): 
    text = re.sub("[^a-zA-Z]", " ", input).lower().split()
    open_file = open('wordlist.txt', 'r')
    outputlist = []
    output = ""
    contents = open_file.readlines()
    for i in range(len(contents)):
         j=0
         w = contents[i].strip('\n')
         if w in text:
            j = text.count(w)
         outputlist.append(j)  
         j=0
    open_file.close()  
    for i in outputlist:
        output+=str(i)
        output+='.'
    return output
