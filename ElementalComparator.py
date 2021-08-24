class ElementalComparator:
    empowers = {'金': '水', '水': '木', '木': '火', '火': '土', '土': '金'}
    subdues = {'金': '木', '木': '土', '土': '水', '水': '火', '火': '金'}

    def get_relation(self, primary, secondary):
        if primary == secondary:
            return f'{primary} is the same as {secondary}'
        elif ElementalComparator.empowers[primary] == secondary:
            return f'{primary} empowers {secondary}'
        elif ElementalComparator.subdues[primary] == secondary:
            return f'{primary} subdues {secondary}'
        elif ElementalComparator.empowers[secondary] == primary:
            return f'{secondary} empowers {primary}'
        elif ElementalComparator.subdues[secondary] == primary:
            return f'{secondary} subdues {primary}'
        else:
            return 'invalid input'


c = ElementalComparator()

print(c.get_relation('水', '火'))
