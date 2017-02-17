def label(stringOfWords): 
  
    open_file = open('depressedwords.txt', 'r')
    depressed_words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         if contents[i].strip('\n') in stringOfWords:
                open_file.close()
                return 1
    open_file.close()  
    return 0
