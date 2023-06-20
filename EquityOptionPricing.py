
from Decorator import Node
from DependencyGraph import dependencyGraph


class EquityOptionPricing:

    @Node
    def presentValue(self):
        print(" inside calculation logic")
        return self.impliedVolatility() * self.stockPrice() * self.timeToExp() * self.strike()
    
    def impliedVolatility(self):
        return 0.3

    def stockPrice(self):
        return 25
    
    def timeToExp(self):
        return 0.42191781
    
    def strike(self):
        return 27.5
        

P = EquityOptionPricing()
print("First pricing:")
print(" price: " + str(P.presentValue()))
print("Second pricing: ")
print(" price: " + str(P.presentValue()))
