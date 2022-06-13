import re
from random import shuffle


def get_input():
    substitutions = {}
    with open("input/2015/day_19", "r") as file:
        for line in file.readlines():
            split_line = line.strip("\n").split(" ")
            if split_line[0] not in substitutions:
                substitutions.update({split_line[0]: [split_line[2]]})
            elif split_line[0] in substitutions:
                substitutions[split_line[0]].append(split_line[2])
    return substitutions


class ReindeerPlant:
    def __init__(self, molecule=None) -> None:
        self.unique_molecules = set()
        self.substitutions = get_input()
        self.input_molecule = (
            "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCa"
            "SiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaF"
            "ArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRn"
            "PBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCa"
            "PBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSi"
            "RnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArTh"
            "SiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFAr"
            "CaSiThRnPBPMgAr"
        )
        self.molecule = self.input_molecule if not molecule else molecule

    def substitute(self, input=None):
        """add set and  include substitution"""
        replacement_input = self.molecule if not input else input
        options = []
        for key, value in self.substitutions.items():
            for match in re.finditer(key, replacement_input):
                for substitution in value:
                    new_molecule = (
                        replacement_input[: match.start()]
                        + substitution
                        + replacement_input[match.end() :]
                    )
                    self.unique_molecules.add(new_molecule)
                    options.append(new_molecule)
        # print(str(len(self.unique_molecules)))
        return options

    def generate(self):
        molecule_created = False
        current_combinations = {self.molecule: 0}
        while not molecule_created:
            working_combinations = current_combinations.copy()
            for molecule, count in current_combinations.items():
                working_combinations.pop(molecule)
                new_molecules = self.substitute(molecule)
                for new_molecule in new_molecules:
                    working_combinations.update({new_molecule: count + 1})
            print(str(count))
            current_combinations = working_combinations.copy()

            if self.input_molecule in current_combinations.keys():
                print(
                    "finished creating after: "
                    f"{current_combinations.get(self.input_molecule)}"
                )
                molecule_created = True

    def invert_substitutions(self):
        self.reverse_substitutions = dict()
        for key, value in self.substitutions.items():
            if type(value) == list:
                for sub in value:
                    self.reverse_substitutions.update({sub: key})
            else:
                self.reverse_substitutions.update({value: key})

    def reverse_engineer(self):
        self.invert_substitutions()
        count = 0
        old_molecule = ""
        while old_molecule != "e":
            working_molecule = self.molecule
            key_options = list(self.reverse_substitutions.keys())
            shuffle(key_options)
            while old_molecule != working_molecule:
                old_molecule = working_molecule
                for key in key_options:
                    while key in working_molecule:
                        count += working_molecule.count(key)
                        working_molecule = working_molecule.replace(
                            key, self.reverse_substitutions[key]
                        )
        print(str(count))


medication_plant = ReindeerPlant()
medication_plant.substitute()
medication_plant.reverse_engineer()
# there's multiple solutions,
# needs a nicer build to get to a more concrete answer
