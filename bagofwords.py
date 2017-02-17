import re 

def bagOfWords(input): 
    
    #split text input into a string of lower case words
    text = re.sub("[^a-zA-Z]", " ", input).lower().split()
    
    #open file containing words for bag of words
    open_file = open('english.txt', 'r')
    
    #initialise outputs
    formattedOutput = ""
    
    #read file 
    contents = open_file.readlines()
    
    #count occurances of each word in the bag of words, and add this to the output 
    for i in range(len(contents)):
         j=0
         w = contents[i].strip('\n')
         j = text.count(w)
         formattedOutput+=str(j)
         formattedOutput+='.'
    
    open_file.close()  
    
    return formattedOutput

