#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def conflict(chesses_placed, next_chess_xcor):
    """
    This is a conflicting function defined
    :param chesses_placed: use a tuple to save chesses placed
    :param next_chess_xcor: the x coordinate of next chess to place
    :return: true or false
    """
    # get the next y coordinate by chessed placed
    next_chess_ycor = len(chesses_placed)

    # use next chess y coordinate to confirm the count of loop
    for i in range(next_chess_ycor):
        # use absolute value to confirm the same oblique line
        print(chesses_placed)
        if abs(chesses_placed[i] - next_chess_xcor) in (0, abs(i - next_chess_ycor)):

            return True
    return False


def place_queens(num=8, chesses_placed_tuple=()):
    """
    This is a placing queens function defined
    :param num: the count of queens
    :param chesses_placed_tuple: such as (1, 5, 0)
    :return: a generator
    """
    for i in range(num):
        if not conflict(chesses_placed_tuple, i):

            # judge the last line
            if len(chesses_placed_tuple) == num - 1:
                yield (i,)
            else:

                # get one bye one element from the generator
                for j in place_queens(num, chesses_placed_tuple + (i,)):  # 如果不是最后一行，那就把原来的元组相加并重新执行
                    # superimpose elements to the newest tuple
                    print(j)
                    yield (i,) + j


res = list(place_queens(8))
print(res)
print(len(res))







