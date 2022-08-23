class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    #def get_cart(self): #first method for len() (sh7al mn haja matalan tma)
        #return len(self.cart)

    def __len__(self): #second method for len() (sh7al mn haja matalan tma)
        return len(self.cart)

    def __call__(self):    #calling class with "order()"
        print(f"{self.customer}")

    def __str__(self): #that if u want to call order print(order) if u dont do that u will call memory adress 0x000001EC96E55B10>
        return f"{self.customer} bought {self.cart}"

    def __bool__(self): #this for boleans True Or False
        return len(self.cart) > 0

order = Order(["iphone", "microphone", "mouse", "keyboard"], "Bouviruss")
#print(order.get_cart())
#print(len(order))
#order() #is for calling class
print(bool(order))
