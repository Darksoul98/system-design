
from enum import Enum
from typing import List


class User:
    pass
class Location:
    pass


    
class Status(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class VehicleType(Enum):
    pass

class Vehicle:
    id: int
    vehicleNumber: int
    type: VehicleType
    kmDriven: int
    status: Status
    
    
class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Reserve:
    pass

class Bill:
    pass

class Payment:
    pass

class Reservation:
    pass
    
class VehicleInventoryManagement:
    obj: List[Vehicle]
    
class CarInventoryManagement(VehicleInventoryManagement):
    obj: List[Car]

class BikeInventoryManagement(VehicleInventoryManagement):
    obj: List[Bike]

class Store:
    id: int
    location: str
    obj: VehicleInventoryManagement
    reservation: List[Reservation]