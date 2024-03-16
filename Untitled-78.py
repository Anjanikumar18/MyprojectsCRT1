class F15:
    def __init__(self):
        self.fan_speed = 0
        self.room_temp = 0
        self.outer_temp = 0

    def lights(self, color):
        print("The color of the light is ")

    def fan(self, speed):
        self.fan_speed = speed
        print("The fan speed is 105 kmph.")

    def Ac(self, room_temp, outer_temp):
        self.room_temp = room_temp
        self.outer_temp = outer_temp
        print("The room temperature is °C and the outer temperature is °C.")

    def display(self):
        temp_difference = self.outer_temp - self.room_temp
        print("The difference between outer and room temperature is °C.")
        print("The fan speed is : ")
f15 = F15()
f15.lights("red")
f15.fan(3)
f15.Ac(25, 30)
f15.display()
