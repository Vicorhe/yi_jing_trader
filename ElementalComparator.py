from Enums import ElementsEnum
import HeavenlyStems
import EarthlyBranches


class ElementalComparator:
    empowers = {
        ElementsEnum.METAL: ElementsEnum.WATER,
        ElementsEnum.WATER: ElementsEnum.WOOD,
        ElementsEnum.WOOD: ElementsEnum.FIRE,
        ElementsEnum.FIRE: ElementsEnum.EARTH,
        ElementsEnum.EARTH: ElementsEnum.METAL
    }
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
            return f'{primaryElement} is the same as {secondaryElement}'
        elif ElementalComparator.empowers[primaryElement] == secondaryElement:
            return f'{primaryElement} empowers {secondaryElement}'
        elif ElementalComparator.subdues[primaryElement] == secondaryElement:
            return f'{primaryElement} subdues {secondaryElement}'
        elif ElementalComparator.empowers[secondaryElement] == primaryElement:
            return f'{secondaryElement} empowers {primaryElement}'
        elif ElementalComparator.subdues[secondaryElement] == primaryElement:
            return f'{secondaryElement} subdues {primaryElement}'
        else:
            return 'invalid input'


c = ElementalComparator()
zi = EarthlyBranches.Zi()
chou = EarthlyBranches.Chou()

jia = HeavenlyStems.Jia()

print(c.get_relation(jia, chou))
print(c.get_relation(zi, chou))
