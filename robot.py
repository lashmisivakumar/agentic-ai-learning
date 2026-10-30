class Robot:
    def __init__(self,name,battery_level):
        self.name=name
        self.battery_level=battery_level
    def status(self):
        print(f"Value of Robot is {self.name} is {self.battery_level}")
    def charge(self):
        print(f"New battery level is {self.battery_level+10}%")
    def move(self):
        print("Move called")
    def turn(self):
        print("Turncalled")
    def battery(self):
        print("battery called")
        print(f"Battery level is {self.battery_level} %")
    def stop(self):
        print("Robot stopped")