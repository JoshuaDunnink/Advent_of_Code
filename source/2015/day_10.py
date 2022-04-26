"""
Today, the Elves are playing a game called look-and-say. They take
turns making sequences by reading aloud the previous sequence and using
that reading as the next sequence. For example, 211 is read as "one two,
 two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous
value as input for the next step. For each step, take the previous
value, and replace each run of digits (like 111) with the number of
digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input,
apply this process 40 times. What is the length of the result?

Your puzzle input is 1113222113.
"""


class RepeatedLookAndSay:

    def __init__(self, repeats: int, puzzle_input: list) -> None:
        test_list = [4, 1, 1, 2]
        self.look_and_say_list = puzzle_input if puzzle_input else test_list
        self.repeats = repeats
        self.repeat_look_say()

    def repeat_look_say(self) -> None:
        for _ in range(self.repeats):
            self.look_and_say_list = self.look_say()
        print(len(self.look_and_say_list))

    def look_say(self) -> list:
        new_list_of_numbers = []
        counter = 0
        while not self.at_end_of_the_list(counter):
            count, number = self.get_next_new_number(counter)
            new_list_of_numbers.extend([count, number])
            counter += count
        return new_list_of_numbers

    def get_next_new_number(self, index: int) -> tuple:
        number = self.look_and_say_list[index]
        count = 1
        while self.index_still_in_range(index):
            if self.look_and_say_list[index+1] == number:
                index += 1
                count += 1
            else:
                break
        return (count, number)

    def at_end_of_the_list(self, counter: int) -> bool:
        return counter >= len(self.look_and_say_list)

    def index_still_in_range(self, index_iterator: int) -> bool:
        return index_iterator + 1 <= len(self.look_and_say_list) - 1


starting_list = [int(num) for num in "1113222113"]

RepeatedLookAndSay(40, starting_list)
RepeatedLookAndSay(50, starting_list)
