def label(stringOfWords): 
  
    #open file containing list of depressed phrases, and read lines
    open_file = open('depressedwords.txt', 'r')
    contents = open_file.readlines()
    
    #label depending on whether it contains a phrase from the file 
    for i in range(len(contents)):
         if contents[i].strip('\n') in stringOfWords:
                open_file.close()
                return 1
    open_file.close()  
    return 0
