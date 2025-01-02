
class LaewTaeApp :
    def __init__(self, randomTimes=0):
        self.listmenu = ["Fried Chicken","Hamburger","Pizza","Steak"]
        self.randomTimes = randomTimes

    def random_foods(self) :
        return self.randomTimes + 1
    
    def list_food(self) :
        return self.listmenu


x = LaewTaeApp()

print(x.list_food())