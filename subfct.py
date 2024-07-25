### subfunctions
# find wStart and wEnd for wi: wi = wstart[i] + wend[i]

def wStartwEnd(myword):
    wend = myword[1:]
    wordLength = len(wend)
    wstart = myword[0]
    for i in range(0, wordLength):
        if wend[i]== 'a':
            wstart += 'A'

        if wend[i]== 'b':
            wstart += 'B'

        if wend[i]== 'A':
            wstart += 'a'

        if wend[i]== 'B':
            wstart += 'b'
        
    return [wstart, wend]

# # driver code
# myword = '1baBA2'
# print("wStart, wEnd of ", myword, wStartwEnd(myword))