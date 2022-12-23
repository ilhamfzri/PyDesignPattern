from typing import List

class MotorycleTransportation:
    def __init__(self):
        self.PRICE_PER_KM = 75
        self.MAX_WEIGHT = 10
        self.MAX_WIDTH_IN_CM = 10
        self.MAX_LENGTH_IN_CM = 10
        self.MAX_HEIGHT_IN_CM = 10

    def calculate_cost(self, distance_in_km:int) -> int:
        cost = self.PRICE_PER_KM * distance_in_km
        return cost
    
    def get_max_weight(self) -> int:
        return self.MAX_WEIGHT

    def get_max_dimension(self) -> List[int]:
        return [self.MAX_WIDTH_IN_CM, self.MAX_LENGTH_IN_CM, self.MAX_HEIGHT_IN_CM]

