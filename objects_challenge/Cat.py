class cat:
    def __init__(self, name, color, type, age, stepPerWalk, stepPerRun):
        self.name = name
        self.color = color
        self.type = type
        self.age = age
        self.stepPerWalk = stepPerWalk
        self.stepPerRun = stepPerRun

    def run(self):
        result = f"I am {self.name} , I am  {self.age} months old , My color is {self.color} , I am {self.type}"
        result += f" and I can run{self.stepPerRun} steps/sec"
        print(result)

    def walk(self):
        result = f"I am {self.name} , I am  {self.age} months old , My color is {self.color} , I am {self.type}"
        result += f" and I can walk {self.stepPerWalk} steps/sec"
        print(result)
