# Define the Placements class
class Placements:
    def info(self):
        print("We have 623 selects and still counting.")
class Department:
    def display(self):
        departments = ["Civil", "Mech", "DS", "AI-ML"]
        print("Names of departments present in the college:")
        for dept in departments:
            print(dept)
class Pragati(Placements, Department):
    def welcome(self):
        print("Welcome to Pragati Engineering College")
        self.info()
        self.display()

pragati_college = Pragati()
pragati_college.welcome()
