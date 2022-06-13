import re

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
    def __init__(self) -> None:
        self.substitutions = get_input()
        self.molocule = (
            "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCa"
            "SiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaF"
            "ArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRn"
            "PBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCa"
            "PBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSi"
            "RnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArTh"
            "SiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFAr"
            "CaSiThRnPBPMgAr"
        )

    def substitude(self):
        for key, value in self.substitutions.items():
            for match in re.search(key, self.molocule):
                print(match.start())


ReindeerPlant().substitude()
