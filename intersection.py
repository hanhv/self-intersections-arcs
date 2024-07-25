### 
from subfct import wStartwEnd
from crosspair import checkcross
from crossfinal import checkJrightI


def intersection(myword):
    numberOfIntersection = 0
    [wstart, wend] = wStartwEnd(myword)
    wsize = len(wstart)
    matrix = [[0 for x in range(wsize)] for y in range(wsize)]

    # test
    # for i in {0}: 
    for i in range(wsize):
        wi = wstart[i] + wend[i]
        for j in range(i + 1, wsize):
            # for j in {3}:
            wj = wstart[j] + wend[j]
            # print('check pair ', i, j, wi , wj, checkcross(wi, wj))
            if matrix[i][j] == 0:  # not checked yet
                if matrix[j][i] != 0:  # already checked by forward/ backward
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 1  # marked as checked

                    # case 1: intersect immediately in the current domain
                    if checkcross(wi, wj) == 1:
                        numberOfIntersection += 1
                        # print('found at', i, j)
                    # end case 1

                    # case 2: never intersect: checkcross(wi,wj)=0

                    # case 3: start and end at the same letters
                    # forward wi, forward wj
                    # backward wi, backward wj
                    if (
                            wi[0] == wj[0] and wi[1] == wj[1] and
                            wi[0] in {'a', 'A', 'b', 'B'} and
                            wi[1] in {'a', 'A', 'b', 'B'}
                    ):
                        # START FORWARD: forward until end different
                        indexiforward = i + 1
                        indexjforward = j + 1
                        while (
                                wend[indexiforward] in {'a', 'A', 'b', 'B'} and
                                wend[indexiforward] == wend[indexjforward]
                        ):
                            matrix[indexiforward][indexjforward] = 1  # mark as checked
                            indexiforward += 1  # continue forward
                            indexjforward += 1

                        matrix[indexiforward][indexjforward] = 1  # mark as checked
                        wifinal1 = wstart[indexiforward] + wend[indexiforward]
                        wjfinal1 = wstart[indexjforward] + wend[indexjforward]
                        jrighti1 = checkJrightI(wifinal1, wjfinal1)

                        # START BACKWARD 
                        indexibackward = i - 1
                        indexjbackward = j - 1
                        while (
                                wstart[indexibackward] in {'a', 'A', 'b', 'B'} and
                                wstart[indexibackward] == wstart[indexjbackward]
                        ):
                            matrix[indexibackward][indexjbackward] = 1  # mark as checked
                            indexibackward -= 1  # continue backward
                            indexjbackward -= 1

                        wifinal2 = wstart[indexibackward] + wend[indexibackward + 1]
                        wjfinal2 = wstart[indexjbackward] + wend[indexjbackward + 1]
                        jrighti2 = checkJrightI(wifinal2, wjfinal2)

                        if (jrighti1 != -1 and jrighti2 != -1 and
                                jrighti1 != jrighti2
                        ):
                            numberOfIntersection += 1
                            # print('found at', i, j)
                    # end case 3

                    # case 4: same start, different end
                    # backward i j until start different
                    if (
                            wi[0] == wj[0] and wi[1] != wj[1] and
                            wi[0] in {'a', 'A', 'b', 'B'}
                    ):
                        jrighti1 = checkJrightI(wi, wj)

                        # START BACKWARD 
                        indexibackward = i - 1
                        indexjbackward = j - 1
                        while (
                                wstart[indexibackward] in {'a', 'A', 'b', 'B'} and
                                wstart[indexibackward] == wstart[indexjbackward]
                        ):
                            matrix[indexibackward][indexjbackward] = 1  # mark as checked
                            indexibackward -= 1  # continue backward
                            indexjbackward -= 1

                        wifinal2 = wstart[indexibackward] + wend[indexibackward]
                        wjfinal2 = wstart[indexjbackward] + wend[indexjbackward]
                        jrighti2 = checkJrightI(wifinal2, wjfinal2)

                        if (jrighti2 != -1 and jrighti1 != jrighti2):
                            numberOfIntersection += 1
                            # print('found at', i, j)
                    # end case 4

                    # case 5: start different, same end
                    if (
                            wi[0] != wj[0] and wi[1] == wj[1] and
                            wi[1] in {'a', 'A', 'b', 'B'}
                    ):
                        # print(i, j, wi, wj, "case 5: start different, same end")
                        # START FORWARD: forward until end different
                        indexiforward = i + 1
                        indexjforward = j + 1
                        while (
                                wend[indexiforward] in {'a', 'A', 'b', 'B'} and
                                wend[indexiforward] == wend[indexjforward]
                        ):
                            matrix[indexiforward][indexjforward] = 1  # mark as checked
                            indexiforward += 1  # continue forward
                            indexjforward += 1

                        matrix[indexiforward][indexjforward] = 1  # mark as checked
                        wifinal1 = wstart[indexiforward] + wend[indexiforward]
                        wjfinal1 = wstart[indexjforward] + wend[indexjforward]
                        jrighti1 = checkJrightI(wifinal1, wjfinal1)
                        # print(indexiforward, indexjforward, wifinal1, wjfinal1, jrighti1)

                        jrighti2 = checkJrightI(wi, wj)

                        if jrighti1 != -1 and jrighti1 != jrighti2:
                            numberOfIntersection += 1
                            # print('found at', i, j)
                    # end case 5

                    # case 6:   start i = end j, 
                    #           end i = start j
                    if (
                            wi[0] == wj[1] and wi[1] == wj[0]
                            and wi[0] in {'a', 'A', 'b', 'B'}
                            and wi[1] in {'a', 'A', 'b', 'B'}
                    ):
                        # start i = end j
                        # backward i, forward j 
                        indexibackward = i - 1
                        indexjforward = j + 1
                        while (
                                wstart[indexibackward] in {'a', 'A', 'b', 'B'} and
                                wstart[indexibackward] == wend[indexjforward]
                        ):
                            matrix[indexibackward][indexjforward] = 1  # mark as checked
                            indexibackward -= 1  # continue backward
                            indexjforward += 1  # continue forward

                        matrix[indexibackward][indexjforward] = 1  # mark as checked
                        wifinal1 = wstart[indexibackward] + wend[indexibackward]
                        wjfinal1 = wstart[indexjforward] + wend[indexjforward]
                        jrighti1 = checkJrightI(wifinal1, wjfinal1)

                        # end i = start j 
                        # forward i, backward j
                        indexiforward = i + 1
                        indexjbackward = j - 1
                        while (
                                wend[indexiforward] in {'a', 'A', 'b', 'B'} and
                                wend[indexiforward] == wstart[indexjbackward]
                        ):
                            matrix[indexiforward][indexjbackward] = 1  # mark as checked
                            indexiforward += 1  # continue forward
                            indexjbackward -= 1  # continue backward

                        matrix[indexiforward][indexjbackward] = 1  # mark as checked
                        wifinal2 = wstart[indexiforward] + wend[indexiforward]
                        wjfinal2 = wstart[indexjbackward] + wend[indexjbackward]
                        jrighti2 = checkJrightI(wifinal2, wjfinal2)

                        if (jrighti1 != -1 and jrighti2 != -1 and
                                jrighti1 != jrighti2
                        ):
                            numberOfIntersection += 1
                            # print('found at', i, j)
                    # end case 6

                    # case 7:   start i = end j, 
                    #           end i != start j
                    if (
                            wi[0] == wj[1] and wi[1] != wj[0]
                            and wi[0] in {'a', 'A', 'b', 'B'}
                    ):
                        # start i = end j
                        # backward i, forward j 
                        indexibackward = i - 1
                        indexjforward = j + 1
                        while (
                                wstart[indexibackward] in {'a', 'A', 'b', 'B'} and
                                wstart[indexibackward] == wend[indexjforward]
                        ):
                            matrix[indexibackward][indexjforward] = 1  # mark as checked
                            indexibackward -= 1  # continue backward
                            indexjforward += 1  # continue forward

                        matrix[indexibackward][indexjforward] = 1  # mark as checked
                        wifinal1 = wstart[indexibackward] + wend[indexibackward]
                        wjfinal1 = wstart[indexjforward] + wend[indexjforward]
                        jrighti1 = checkJrightI(wifinal1, wjfinal1)
                        # print("case 7 start i = endj", i, j, wifinal1, wjfinal1, jrighti1)

                        jrighti2 = checkJrightI(wi, wj)

                        if (jrighti1 != -1) and (jrighti1 != jrighti2):
                            numberOfIntersection += 1
                            # print('found at', i, j)
                    # end case 7

                    # case 8:   start i != end j, 
                    #           end i == start j
                    if (
                            wi[0] != wj[1] and wi[1] == wj[0]
                            and wi[1] in {'a', 'A', 'b', 'B'}
                    ):
                        jrighti1 = checkJrightI(wi, wj)
                        # print("jrighti1 ", jrighti1)
                        # print("in case 8 ")
                        # end i = start j

                        # print("in case 8: forward i, backward j")
                        # end i = start j 
                        # forward i, backward j
                        indexiforward = i + 1
                        indexjbackward = j - 1
                        while (
                                wend[indexiforward] in {'a', 'A', 'b', 'B'} and
                                wend[indexiforward] == wstart[indexjbackward]
                        ):
                            matrix[indexiforward][indexjbackward] = 1  # mark as checked
                            indexiforward += 1  # continue forward
                            indexjbackward -= 1  # continue backward

                        matrix[indexiforward][indexjbackward] = 1  # mark as checked
                        wifinal2 = wstart[indexiforward] + wend[indexiforward]
                        wjfinal2 = wstart[indexjbackward] + wend[indexjbackward]
                        jrighti2 = checkJrightI(wifinal2, wjfinal2)

                        if jrighti2 != -1 and jrighti1 != jrighti2:
                            numberOfIntersection += 1
                            # print('found at', i, j) 
                    # end case 8

    # print("current matrix ", matrix)
    return numberOfIntersection


###################################
###################################
# examples:
# my_word = '1baBA2'  # 4
# print("intersection", my_word, intersection(my_word))
