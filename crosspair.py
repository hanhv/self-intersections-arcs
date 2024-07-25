### check if wi and wj intersect in the current domain
def checkcross(wi, wj):
    if ((wi in {'aA', 'Aa'} and wj in {'1b', 'b1', '1B', 'B1'}) or 
        (wi in {'ab', 'ba'} and wj in {'AB', 'BA', '2A', 'A2', '3A', 'A3', '1B', 'B1', '3B', 'B3'}) or 
        (wi in {'aB', 'Ba'} and wj in {'3A', 'A3', '3b', 'b3'}) or 
        (wi in {'2a', 'a2'} and wj in {'AB', 'BA', '3A', 'A3','bB', 'Bb', '3b', 'b3', '1B','B1', '3B', 'B3'}) or 
        (wi in {'3a', 'a3'} and wj in {'Ab', 'bA', 'AB', 'BA', '2A', 'A2', '3A', 'A3', '1b', 'b1', '1B', 'B1'}) or 
        (wi in {'Ab', 'bA'} and wj in {'3B', 'B3'}) or 
        (wi in {'AB', 'BA'} and wj in {'ab', 'ba', '2a', 'a2', '3a', 'a3', '1b', 'b1', '3b', 'b3'}) or 
        (wi in {'2A', 'A2'} and wj in {'ab', 'ba', '3a', 'a3', 'bB', 'Bb', '1b', 'b1', '3b', 'b3', '3B', 'B3'}) or 
        (wi in {'3A', 'A3'} and wj in {'ab', 'ba', 'aB', 'Ba', 'a2', '2a', 'a3', '3a', 'b1', '1b', 'B1', '1B'}) or 
        (wi in {'bB', 'Bb'} and wj in {'a2', '2a', 'A2', '2A'}) or 
        (wi in {'1b', 'b1'} and wj in {'aA', 'Aa', 'a3', '3a', 'AB', 'BA', 'A2', '2A', 'A3', '3A', 'B3', '3B'}) or 
        (wi in {'3b', 'b3'} and wj in {'aB', 'Ba', 'a2', '2a', 'AB', 'BA', 'A2', '2A', 'B1', '1B', 'B3', '3B'}) or 
        (wi in {'1B', 'B1'} and wj in {'aA', 'Aa', 'ab', 'ba', 'a2', '2a', 'a3', '3a', 'A3', '3A', 'b3', '3b'}) or 
        (wi in {'3B', 'B3'} and wj in {'ab', 'ba', 'a2', '2a', 'Ab', 'bA', 'A2', '2A', 'b1', '1b', 'b3', '3b'})
    ):  
        return 1
    elif ((wi in {'aA', 'Aa'} and wj in {'bB', 'Bb', 'b3', '3b', 'B3', '3B'}) or 
        (wi in {'aB', 'Ba'} and wj in {'Ab', 'bA', 'A2', '2A', 'b1', '1b'}) or 
        (wi in {'a2', '2a'} and wj in {'Ab', 'bA', 'A2', '2A', 'b1', '1b'}) or 
        (wi in {'a3', '3a'} and wj in {'bB', 'Bb', 'b3', '3b', 'B3', '3B'}) or 
        (wi in {'Ab', 'bA'} and wj in {'aB', 'Ba', 'a2', '2a', 'B1', '1B'}) or 
        (wi in {'A2', '2A'} and wj in {'aB', 'Ba', 'a2', '2a', 'B1', '1B'}) or 
        (wi in {'bB', 'Bb'} and wj in {'aA', 'Aa', 'a3', '3a', 'A3', '3A'}) or 
        (wi in {'b1', '1b'} and wj in {'aB', 'Ba', 'a2', '2a', 'B1', '1B'}) or 
        (wi in {'b3', '3b'} and wj in {'aA', 'Aa', 'a3', '3a', 'A3', '3A'}) or 
        (wi in {'B1', '1B'} and wj in {'Ab', 'bA', 'A2', '2A', 'b1', '1b'}) or 
        (wi in {'B3', '3B'} and wj in {'aA', 'Aa', 'a3', '3a', 'A3', '3A'})
    ):
        return 0
    else:
        return -1

# # driver code
# # 1b a2 0
# wi = '1b'
# wj = 'a2'

# # AB a2 1
# wi = 'AB'
# wj = 'a2'

# # ab b3 -1
# wi = 'ab'
# wj = 'b3'

# print("check cross ", wi, wj, " : ", checkcross(wi, wj))