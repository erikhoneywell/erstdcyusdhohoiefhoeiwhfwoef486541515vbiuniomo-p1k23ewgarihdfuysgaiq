
class ModelResponse():

    def __init__(self):
        self.components = []
        self.restricted = []

    def add_recommendation(self, componets):
        for c in componets:   
            self.components.append(c)

    def add_restriction(self, x):
        self.restricted.extend(x)
