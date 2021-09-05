from Enums import ElementsEnum
import HeavenlyStems
import EarthlyBranches


class ElementalComparator:
    # 生
    empowers = {
        ElementsEnum.METAL: ElementsEnum.WATER,
        ElementsEnum.WATER: ElementsEnum.WOOD,
        ElementsEnum.WOOD: ElementsEnum.FIRE,
        ElementsEnum.FIRE: ElementsEnum.EARTH,
        ElementsEnum.EARTH: ElementsEnum.METAL
    }
    # 克
    subdues = {
        ElementsEnum.METAL: ElementsEnum.WOOD,
        ElementsEnum.WOOD: ElementsEnum.EARTH,
        ElementsEnum.EARTH: ElementsEnum.WATER,
        ElementsEnum.WATER: ElementsEnum.FIRE,
        ElementsEnum.FIRE: ElementsEnum.METAL
    }

    def get_relation(self, primaryWord, secondaryWord):
        if primaryWord.type() != secondaryWord.type():
            return 'incompatible comparison'
        primaryElement = primaryWord.element
        secondaryElement = secondaryWord.element
        if primaryElement == secondaryElement:
            return f'{primaryElement} 同 {secondaryElement}'
        elif ElementalComparator.empowers[primaryElement] == secondaryElement:
            return f'{primaryElement} 生 {secondaryElement}'
        elif ElementalComparator.subdues[primaryElement] == secondaryElement:
            return f'{primaryElement} 克 {secondaryElement}'
        elif ElementalComparator.empowers[secondaryElement] == primaryElement:
            return f'{secondaryElement} 生 {primaryElement}'
        elif ElementalComparator.subdues[secondaryElement] == primaryElement:
            return f'{secondaryElement} 克 {primaryElement}'
        else:
            return 'invalid input'


c = ElementalComparator()
zi = EarthlyBranches.Zi()
chou = EarthlyBranches.Chou()

jia = HeavenlyStems.Jia()
yi = HeavenlyStems.Yi()
xin = HeavenlyStems.Xin()
print(c.get_relation(jia, xin))
#print(c.get_relation(zi, chou))
