class Budget:
    def __init__(self, category):
        self.category = category
        self.amount = 600
    
    def deposit(self, amount):
       self.amount += amount
       return self.amount

    def withdrawal(self, amount):
        self.amount -= amount
        return self.amount

    def transfer(self):
        if self.amount > amount
            return False
    
    def emergency(self, amount):
        if self.amount += amount
            return True
        else:
            self.amount -= amount
            print True
         pass

    category = Budget('clothing')
    print('This is deposit for clothing', category.deposit(250))
    print('This is withdrawal for clothing', category.withdrawal(250))

    category_1 = Budget('entertainment')
    print('This is deposit for entertainment', category.deposit(250))
    print('This is withdrawal for entertainment', category.withdrawal(250))

    category_2 = Budget('food')
    print('This is deposit for food', category.deposit(250))
    print('This is withdrawal for food', category.withdrawal(250))

    category_3 = Budget('emergency')
    print('This is deposit for emergency', category.deposit(250))
    print('This is withdrawal for emergency', category.withdrawal(250))

