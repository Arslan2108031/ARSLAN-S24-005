class ReflexAgent:
    def __init__(self, threshold=22):
        self.threshold = threshold 
        self.previous_action = None  
    def decide_action(self, temperature):
        if temperature < self.threshold and self.previous_action != "Heater ON":
            self.previous_action = "Heater ON"
        elif temperature >= self.threshold and self.previous_action != "Heater OFF":
            self.previous_action = "Heater OFF"
        return self.previous_action
agent = ReflexAgent()
temperatures = [20, 26, 24, 16, 18, 25, 26]  
for temp in temperatures:
    action = agent.decide_action(temp)
    print(f"Temperature: {temp}°C → {action}")
