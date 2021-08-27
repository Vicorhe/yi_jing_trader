from enum import Enum


class HeavenlyStemsEnum(Enum):
    JIA = 1  # 甲
    YI = 2  # 乙
    BING = 3  # 丙
    DING = 4  # 丁
    WU = 5  # 戊
    JI = 6  # 己
    GENG = 7  # 庚
    XIN = 8  # 辛
    REN = 9  # 壬
    GUI = 10  # 癸


class EarthlyBranchesEnum(Enum):
    ZI = 1  # 子
    CHOU = 2  # 丑
    YIN = 3  # 寅
    MAO = 4  # 卯
    CHEN = 5  # 辰
    SI = 6  # 巳
    WU = 7  # 午
    WEI = 8  # 未
    SHEN = 9  # 申
    YOU = 10  # 酉
    XU = 11  # 戌
    HAI = 12  # 亥


class YinYangEnum(Enum):
    YIN = 1  # 阴
    YANG = 2  # 阳


class ElementsEnum(Enum):
    METAL = 1  # 金
    WATER = 2  # 水
    WOOD = 3  # 木
    FIRE = 4  # 火
    EARTH = 5  # 土
