from datetime import datetime
from enum import Enum
from typing import List


class BaseModel:
    def __init__(self, id):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


class ParkingLotStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class SlotStatus(Enum):
    FILLED = 'FILLED'
    EMPTY = 'EMPTY'
    BLOCKED = 'BLOCKED'
    RESERVED = 'RESERVED'


class FloorStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class GateStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'


class GateType(Enum):
    ENTRY = 'ENTRY'
    EXIT = 'EXIT'


class VehicleType(Enum):
    BIKE = 'BIKE'
    CAR = 'CAR'
    BUS = 'BUS'
    TRUCK = 'TRUCK'


class BillStatus(Enum):
    PAID = 'PAID'
    PENDING = 'PENDING'
    PARTIALLY_PAID = 'PARTIALLY_PAID'


class PaymentModes(Enum):
    ONLINE = 'ONLINE'
    CASH = 'CASH'
    CARD = 'CARD'
    UPI = 'UPI'


class PaymentStatus(Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class SlotAssignmentStrategyEnum(Enum):
    RANDOM = 'RANDOM'
    LIFO = 'LIFO'
    FIFO = 'FIFO'


class FeeCalculationStrategyEnum(Enum):
    HOURLY = 'HOURLY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'


class Bill(BaseModel):
    def __init__(self, id: int, amount: int, exit_time: datetime, token, exited_at, bill_status: BillStatus,
                 payments: List):
        super().__init__(id)
        self.amount = amount
        self.exit_time = exit_time
        self.token = token
        self.exited_at = exited_at
        self.bill_status = bill_status
        self.payments = payments


class Payment(BaseModel):
    def __init__(self, id: int, amount: int, payment_mode: PaymentModes, payment_status: PaymentStatus,
                 paid_at: datetime, ref_id: str, bill):
        super().__init__(id)
        self.amount = amount
        self.payment_mode = payment_mode
        self.payment_status = payment_status
        self.paid_at = paid_at
        self.ref_id = ref_id
        self.bill = bill


class Gate(BaseModel):
    def __init__(self, id: int, gate_no: int, gate_type: GateType, parking_lot, gate_status: GateStatus):
        super().__init__(id)
        self.gate_no = gate_no
        self.gate_type = gate_type
        self.parking_lot = parking_lot
        self.gate_status = gate_status


class Floor(BaseModel):
    def __init__(self, id: int, parking_slots_list: List, floor_no: int, floor_status: FloorStatus,
                 allowed_vehicles: List[VehicleType]):
        super().__init__(id)
        self.parking_slots_list = parking_slots_list
        self.floor_no = floor_no
        self.floor_status = floor_status
        self.allowed_vehicles = allowed_vehicles


class Slot(BaseModel):
    def __init__(self, id: int, slot_no: int, vehicle_type: VehicleType, parking_slot_status: SlotStatus,
                 parking_floor: Floor):
        super().__init__(id)
        self.slot_no = slot_no
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor


class Ticket(BaseModel):
    def __init__(self, id: int, ticket_no: str, entry_time: datetime, vehicle, parking_slot: Slot,
                 generated_at: Gate):
        super().__init__(id)
        self.ticket_no = ticket_no
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_at = generated_at


class Vehicle(BaseModel):
    def __init__(self, id: int, owner_name: str, vehicle_type: VehicleType):
        super().__init__(id)
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name


class ParkingLotTimings(Enum):
    DAILY = '9AM-9PM'
    WEEKENDS = '9AM-11PM'


class ParkingLot(BaseModel):
    def __init__(self, id: int, name: str, address: str, parking_floors: List[Floor], gates: List[Gate],
                 allowed_vehicles: List[Vehicle], capacity: int, status: ParkingLotStatus,
                 slot_assignment_stgy: SlotAssignmentStrategyEnum, fee_calculation_stgy: FeeCalculationStrategyEnum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_stgy = slot_assignment_stgy
        self.fee_calculation_stgy = fee_calculation_stgy
