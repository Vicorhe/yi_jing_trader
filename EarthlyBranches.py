from Base import EarthlyBranch
from Enums import EarthlyBranchesEnum, YinYangEnum, ElementsEnum


class Zi(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.ZI,
                               YinYangEnum.YANG, ElementsEnum.WATER)


class Chou(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.CHOU,
                               YinYangEnum.YIN, ElementsEnum.EARTH)


class Yin(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.YIN,
                               YinYangEnum.YANG, ElementsEnum.WOOD)


class Mao(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.MAO,
                               YinYangEnum.YIN, ElementsEnum.WOOD)


class Chen(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.CHEN,
                               YinYangEnum.YANG, ElementsEnum.EARTH)


class Si(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.SI,
                               YinYangEnum.YIN, ElementsEnum.FIRE)


class Wu(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.WU,
                               YinYangEnum.YANG, ElementsEnum.FIRE)


class Wei(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.WEI,
                               YinYangEnum.YANG, ElementsEnum.EARTH)


class Shen(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.SHEN,
                               YinYangEnum.YANG, ElementsEnum.METAL)


class You(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.YOU,
                               YinYangEnum.YIN, ElementsEnum.METAL)


class Xu(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.XU,
                               YinYangEnum.YIN, ElementsEnum.EARTH)


class Hai(EarthlyBranch):
    def __init__(self):
        EarthlyBranch.__init__(self, EarthlyBranchesEnum.HAI,
                               YinYangEnum.YIN, ElementsEnum.WATER)
