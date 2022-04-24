A = [7, 8, 4, 5, 28]
B = [5, 5, 4, 5, 19]
C = [21, 6]
D = [5, 9, 33]
# by hand, just some notes here ^

"""
#############
#...........#
###C#C#A#B###
  #D#D#B#A#
  #########
"""

# part 2
ans = sum(A) + sum(B) * 10 + sum(C) * 100 + sum(D) * 1000
print(ans)
