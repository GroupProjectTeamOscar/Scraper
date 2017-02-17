def depressedWords(): 
  
    open_file = open('depressedwords.txt', 'r')
    depressed_words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         depressed_words_list.append(contents[i].strip('\n'))   
    open_file.close()  
    return depressed_words_list 

def firstlabel(stringOfWords): 
    
    #takes a string and returns true if keyphase is in the string 
    
    depressedWordsList = depressedWords()
    
    for w in depressedWordsList:
        if w in stringOfWords: 
            return 1
    return 0
   
