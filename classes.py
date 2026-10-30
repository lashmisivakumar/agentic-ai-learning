class Robot:
    def __init__(self,name,Battery):
        self.name=name
        self.Battery=Battery

    def status(self):
        print(self.name,self.Battery)
        print(self)

    def charge(self):
        a=self.Battery+10
        print(f"New battery level: {a}%")



#r1=Robot("turtle",80)

name=input("Enter the name")
battery=int(input("Enter the battery level"))
r1=Robot(name,battery)
r2=Robot(name,battery)
print(r1.name)
r1.status()
r2.status()
r1.charge()