class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.b > 0:
            self.b-=1
            return True
        
        if carType == 2 and self.m > 0:
            self.m-=1
            return True
    
        if carType == 3 and self.s > 0:
            self.s-=1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
