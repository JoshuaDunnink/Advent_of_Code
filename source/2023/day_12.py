import re

test_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


for line in test_data.split("\n"):
    series, sequence = line.strip().split(" ")
    test_sequence = series
    for iter_match in re.finditer("\?", series):
        iter_match.start()
