from Card import *

### TESTS ###

# double run for 8, four 15's for 16
print(Hand([Card(4, "h"), Card(5, "d"), Card(6, "h"), Card(10, "c")], Card(5, "h")).calculatePoints())

# double double for 16, four 15's for 24
print(Hand([Card(4, "h"), Card(5, "d"), Card(6, "h"), Card(6, "c")], Card(5, "h")).calculatePoints())

# 29
print(Hand([Card(5, "h"), Card(5, "d"), Card(5, "s"), Card(11, "c")], Card(5, "c")).calculatePoints())

# 12
print(Hand([Card(1, "h"), Card(2, "h"), Card(3, "h"), Card(4, "h")], Card(5, "h")).calculatePoints())

# 11
print(Hand([Card(1, "h"), Card(2, "h"), Card(3, "h"), Card(4, "h")], Card(5, "d")).calculatePoints())
