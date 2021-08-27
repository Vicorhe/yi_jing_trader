from Base import HeavenlyStem
from Enums import HeavenlyStemsEnum, YinYangEnum, ElementsEnum


class Jia(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.JIA,
                              YinYangEnum.YANG, ElementsEnum.WOOD)


class Yi(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.YI,
                              YinYangEnum.YIN, ElementsEnum.WOOD)


class Bing(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.BING,
                              YinYangEnum.YANG, ElementsEnum.FIRE)


class Ding(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.DING,
                              YinYangEnum.YIN, ElementsEnum.FIRE)


class Wu(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.WU,
                              YinYangEnum.YANG, ElementsEnum.EARTH)


class Ji(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.JI,
                              YinYangEnum.YIN, ElementsEnum.EARTH)


class Geng(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.GENG,
                              YinYangEnum.YANG, ElementsEnum.METAL)


class Xin(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.XIN,
                              YinYangEnum.YIN, ElementsEnum.METAL)


class Ren(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.REN,
                              YinYangEnum.YANG, ElementsEnum.WATER)


class Gui(HeavenlyStem):
    def __init__(self):
        HeavenlyStem.__init__(self, HeavenlyStemsEnum.GUI,
                              YinYangEnum.YIN, ElementsEnum.WATER)
