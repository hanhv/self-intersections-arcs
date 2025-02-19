# check cross pair final: after forward/ backward
def checkJrightI(wi, wj):
    # only check position if they have 1 common node

    if ((wi[0] in {wj[0], wj[1]} and wi[0] in {'1', '2', '3'}) 
        or (wi[1] in {wj[0], wj[1]} and wi[1] in {'1', '2', '3'}) 
        or (wj[0] in {wi[0], wi[1]} and wj[0] in {'1', '2', '3'})
        or (wj[1] in {wi[0], wi[1]} and wj[1] in {'1', '2', '3'})  
    ):
        return -1

    # same at start wi
    # start a
    if wi[0] == 'a':
        if (
            (wi[1] == 'A' and wj in {'a3', 'ab', 'a2', 'aB', 
                                        '3a', 'ba', '2a', 'Ba'}) or
            (wi[1] == '3' and wj in {'ab', 'a2', 'aB',
                                        'ba', '2a', 'Ba'}) or
            (wi[1] == 'b' and wj in {'a2', 'aB',
                                        '2a', 'Ba'}) or
            (wi[1] == '2' and wj[1] in {'aB', 'Ba'})
        ):
            return 1
    # start A
    elif wi[0] == 'A':
        if (
            (wi[1] == 'b' and wj in {'A2', 'AB', 'A3', 'Aa',
                                        '2A', 'BA', '3A', 'aA'}) or
            (wi[1] == '2' and wj in {'AB', 'A3', 'Aa',
                                        'BA', '3A', 'aA'}) or
            (wi[1] == 'B' and wj in {'A3', 'Aa',
                                        '3A', 'aA'}) or
            (wi[1] == '3' and wj in {'Aa', 'aA'})
        ): 
            return 1
    # start b
    elif wi[0] == 'b':
        if(
            (wi[1] == 'B' and wj in {'b3', 'ba', 'b1', 'bA',
                                        '3b', 'ab', '1b', 'Ab'}) or
            (wi[1] == '3' and wj in {'ba', 'b1', 'bA',
                                        'ab', '1b', 'Ab'}) or
            (wi[1] == 'a' and wj in {'b1', 'bA',
                                        '1b', 'Ab'}) or
            (wi[1] == '1' and wj in {'bA', 'Ab'})
        ):
            return 1
    # start B
    elif wi[0] == 'B':
        if(
            (wi[1] == 'a' and wj in {'B1', 'BA', 'B3', 'Bb',
                                        '1B', 'AB', '3B', 'bB'}) or
            (wi[1] == '1' and wj in {'BA', 'B3', 'Bb',
                                        'AB', '3B', 'bB'}) or
            (wi[1] == 'A' and wj in {'B3', 'Bb',
                                        '3B', 'bB'}) or
            (wi[1] == '3' and wj in {'Bb', 'bB'}) 
        ):
            return 1
    # same at end wi
    # end a
    if wi[1] == 'a':
        if(
            (wi[0] == 'B' and wj in {'2a', 'ba', '3a', 'Aa',
                                        'a2', 'ab', 'a3', 'aA'}) or
            (wi[0] == '2' and wj in {'ba', '3a', 'Aa',
                                        'ab', 'a3', 'aA'}) or
            (wi[0] == 'b' and wj in {'3a', 'Aa',
                                        'a3', 'aA'}) or
            (wi[0] == '3' and wj in {'Aa', 'aA'})
        ):
            return 1
    # end A
    elif wi[1] == 'A':
        if(
            (wi[0] == 'a' and wj in {'3A', 'BA', '2A', 'bA',
                                        'A3', 'AB', 'A2', 'Ab'}) or
            (wi[0] == '3' and wj in {'BA', '2A', 'bA',
                                        'AB', 'A2', 'Ab'}) or
            (wi[0] == 'B' and wj in {'2A', 'bA',
                                        'A2', 'Ab'}) or
            (wi[0] == '2' and wj in {'bA', 'Ab'})
        ):
            return 1
    # end B
    elif wi[1] == 'B':
        if(
            (wi[0] == 'b' and wj in {'3B', 'AB', '1B', 'aB',
                                        'B3', 'BA', 'B1', 'Ba'}) or
            (wi[0] == '3' and wj in {'AB', '1B', 'aB',
                                        'BA', 'B1', 'Ba'}) or
            (wi[0] == 'A' and wj in {'1B', 'aB',
                                        'B1', 'Ba'}) or
            (wi[0] == '1' and wj in {'aB', 'Ba'})
        ):
            return 1
    # end b
    elif wi[1] == 'b':
        if(
            (wi[0] == 'A' and wj in {'1b', 'ab', '3b', 'Bb',
                                        'b1', 'ba', 'b3', 'bB'}) or
            (wi[0] == '1' and wj in {'ab', '3b', 'Bb',
                                        'ba', 'b3', 'bB'}) or
            (wi[0] == 'a' and wj in {'3b', 'Bb',
                                        'b3', 'bB'}) or
            (wi[0] == '3' and wj in {'Bb', 'bB'})
        ):
            return 1

    return 0 

# # driver code 
# wi = 'b3'
# wj = 'bB'
# print(checkJrightI(wi, wj))

# wi = 'ab'
# wj = 'aB'
# print(checkJrightI(wi, wj))