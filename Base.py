from Enums import EarthlyBranchesEnum, HeavenlyStemsEnum, YinYangEnum, ElementsEnum


class Word:
    def __init__(self, character, yinyang, element):
        self.character = character
        self.yinyang = yinyang
        self.element = element


class HeavenlyStem(Word):
    def __init__(self, character, yinyang, element):
        Word.__init__(self, character, yinyang, element)

    def type(self):
        return 'HeavenlyStem'


class EarthlyBranch(Word):
    def __init__(self, character, yinyang, element):
        Word.__init__(self, character, yinyang, element)

    def type(self):
        return 'EarthlyBranch'
