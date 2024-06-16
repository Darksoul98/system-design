from enum import Enum
from typing import List

# Number of Lift: Can be multiple
# Lift Dispatch Algorithm: There can be multiple

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    
class Status(Enum):
    MOVING = "MOVING"
    IDLE = "IDLE"
    
class Door:
    pass

class Display:
    floor: int
    direction: Direction
    
class ElevatorCar:
    id: int
    # has-a 
    display: Display
    currentFloor: 'Floor'
    direction: Direction
    status: Status
    internalButton: 'InternalButton'
    # has-a 
    door: Door

    def move(self, destinationFloor: 'Floor', direction: Direction):
        pass
    

class ElevatorController:
    # for specific car
    obj: ElevatorCar
    minHeap: List[int]
    maxHeap: List[int]
    pendingJobs: List[int]
    
    def submitNewRequest(self, floor: int, direction: Direction):
        pass

    def controlCar(self):
        # if going up, requested floor, UP < current floor add in pendingQ
        # if going up, requested floor, UP > current floor add in min heap
        # if going up, requested floor, DOWN > current floor add in max heap
        # if going up, requested floor, DOWN < current floor add in max heap
        pass

# requests can come from internal and external button
class ExternalButtonDispatcher:
    # has-a
    obj: List[ElevatorController]
    
    def submitRequest(self, floor: int, direction: Direction):
        pass

# is-a
class OddEvenDispatcher(ExternalButtonDispatcher):
    pass

# is-a
class FixedFloorDispatcher(ExternalButtonDispatcher):
    pass

class ExternalButton:
    
    dispatcher: ExternalButtonDispatcher
    def pressButton(self, floor: int, direction: Direction):
        pass
    

class InternalButtonDispatcher:
    obj: List[ElevatorController]
    
    def submitRequest(self, liftId: int):
        self.obj[liftId].submitNewRequest()
        pass    

class InternalButton:
    obj: InternalButtonDispatcher
    
    def pressButton(self, button: int):
        pass

class Floor:
    id: int
    extbtn: ExternalButton

class Building:
    floors: List[Floor]
    
    