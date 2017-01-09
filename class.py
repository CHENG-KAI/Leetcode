class Hero:
    def __init__(self,name):
        self.name=name
        self.health=100
    def eat(self,food):
        if(food=="apple"):
            self.health-=100
        elif(food=="ham"):
            self.health+=100

Bob = Hero("lin")
print Bob.name
Bob.eat("ham")
print Bob.health
print Bob.name
