from enum import Enum
from typing import List, Union


class VehicleType(Enum):
    TWO_WHEELER= "TWO_WHEELER"
    FOUR_WHEELER="FOUR_WHEELER"

class Vehicle:
    number: str
    type: VehicleType


    

    
class ParkingSpot:
    id: int
    isEmpty: bool
    vehicle: Vehicle
    price: int
    type: VehicleType
    
    def parkVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.isEmpty = False
    
    def removeVehicle(self, vehicle: Vehicle):
        self.vehicle = None
        self.isEmpty = True
    
class TwoWheelerSpot(ParkingSpot):
    
    def price():
        return 10

class FourWheelerSpot(ParkingSpot):
    
    def price():
        return 10

class ParkingStrategy:
    pass

class NearToEntrance(ParkingStrategy):
    def find():
        pass

class DefaultParkingStrategy(ParkingStrategy):
    def find():
        pass


class ParkingSpotManager:
    spots: List[ParkingSpot]
    parkingStrategy: ParkingStrategy
    
    def __init__(self, spots, parkingStrategy: ParkingStrategy = DefaultParkingStrategy()) -> None:
        self.spots = spots
        self.parkingStrategy = parkingStrategy
        
    def addSpot():
        pass

    def findParkingSpace():
        pass

    def removeParkingSpace():
        pass

    def removeVehicle():
        pass
    
    def parkVehicle():
        pass

class TwoWheelerSpotManager(ParkingSpotManager):
    spots: List[TwoWheelerSpot]
    
    def __init__(self, spots) -> None:
        self.spots = spots
        super(self.spots, NearToEntrance())
    

class Ticket:
    entryTime: int
    spot: ParkingSpot
    vehicle: Vehicle


class ParkingManagerFactory():
    def getParkingManager(type: VehicleType) -> Union[ParkingSpotManager]:
        pass
        
class EntranceGate:
    psFactory: ParkingManagerFactory
    psManager: ParkingSpotManager
    ticket: Ticket
    def __init__(self) -> None:
        pass
    
    def findParkingSpace(type: VehicleType, gateNumber):
        pass
    
    def bookParkingSpace():
        pass
    
    def updateParkingSpace():
        pass
    
    def generateTicket(type, spot):
        pass

class PricingStategy:
    
    def price():
        return 10

class HourlyPricingStategy(PricingStategy):
    
    def price(ticket: Ticket):
        pass

class ByMinutePricingStategy(PricingStategy):
    
    def price(ticket: Ticket):
        pass
    
class CostComputation:
    pricingStategy: PricingStategy

class TwoWheelerCC(CostComputation):
    
    def __init__(self) -> None:
        super(HourlyPricingStategy()).__init__()


class FourWheelerCC(CostComputation):
    
    def __init__(self) -> None:
        super(ByMinutePricingStategy()).__init__()


class CostComputationFactory:

    def getCostComputation(ticket) -> CostComputation:
        pass
    
class ExitGate:
    
    ticket: Ticket
    obj: CostComputationFactory
    costCC: CostComputation
    spotManager: ParkingSpotManager
    
    def costCalculation():
        pass
    
    def payment():
        pass
    
    def updateSpot():
        pass
