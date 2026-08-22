# PEAS Representation of an Intelligent Agent

class Agent:
    def __init__(self, name, p, e, a, s):
        self.name = name
        self.performance = p
        self.environment = e
        self.actuators = a
        self.sensors = s

    def show(self):
        print("Agent :", self.name)
        print("Performance :", self.performance)
        print("Environment :", self.environment)
        print("Actuators :", self.actuators)
        print("Sensors :", self.sensors)

agent = Agent(
    "Self-Driving Car",
    "Safe and Fast Driving",
    "Road, Traffic, Weather",
    "Steering, Brake, Accelerator",
    "Camera, GPS, Radar"
)

agent.show()