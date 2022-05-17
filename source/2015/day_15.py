"""takeaway
use itertools for combination exploration and Counter for easy turfing
"""

from itertools import combinations_with_replacement
from collections import Counter


def get_data():
    with open("./input/2015/day_15", "r") as file:
        data = file.readlines()
        striped_data = [line.strip("\n").split(" ") for line in data]
        return {
            line[0].strip(":"): {
                line[1]: int(line[2].strip(",")),
                line[3]: int(line[4].strip(",")),
                line[5]: int(line[6].strip(",")),
                line[7]: int(line[8].strip(",")),
                line[9]: int(line[10].strip(",")),
            }
            for line in striped_data
        }


class CookieScoreFactory:
    def __init__(self, ingredients_and_score: dict, teaspoons=100):
        self.ingredients_and_score = ingredients_and_score
        self.ingredients = list(self.ingredients_and_score.keys())
        self.teaspoons = teaspoons

    def determine_highest_scoring_cookie(self):
        self.determine_combinations()
        scores = self.determine_combination_score()
        print(max(scores))

    def determine_combinations(self):
        self.combinations = combinations_with_replacement(
            self.ingredients, self.teaspoons
        )

    def determine_combination_score(self):
        total_scores = []
        for combination in self.combinations:
            scores = []
            calories = 0
            spoon_counter = Counter(combination)
            for ingredient, spoons in spoon_counter.items():
                scores.append(self.get_ingredient_score(ingredient, spoons))
                calories += self.get_calory_score(ingredient, spoons)
            if calories == 500:
                total_scores.append(self.get_recipe_score(scores))
        return total_scores

    def get_calory_score(self, ingredient, spoons):
        calories = self.ingredients_and_score[ingredient]["calories"]
        return calories * spoons

    def get_ingredient_score(self, ingredient, spoons):
        scores = self.ingredients_and_score[ingredient]
        intermediate_scores = []
        for key, score in scores.items():
            if key != "calories":
                intermediate_scores.append(score * spoons)
        return intermediate_scores

    @staticmethod
    def get_recipe_score(scores):
        transposed_scores = list(map(list, zip(*scores)))
        summed_scores = []
        for t_scores in transposed_scores:
            added = sum(t_scores)
            if added <= 0:
                added = 0
            summed_scores.append(added)
        total_score = 1
        for score in summed_scores:
            total_score = total_score * score
        return total_score


score = CookieScoreFactory(get_data()).determine_highest_scoring_cookie()
