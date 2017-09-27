def wordfreq(str):
    wordlist = {}
    count = 0
    for word in str:
        if word in wordlist:
            count = count+1
        else:
            wordlist.append(word)
        
wordfreq("hello there good morning there")
