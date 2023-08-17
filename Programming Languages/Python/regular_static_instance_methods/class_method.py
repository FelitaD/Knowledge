class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


print(Pizza.margherita())

# use class instead of create instance via a constructor
# margherita = Pizza(['mozzarella', 'tomatoes'])
# DRY principle
# __init__ provides a shortcut to remembering all ingredients
