"""Sunsynk 5kW&8kW hybrid inverter sensor definitions."""
from typing import Dict, Final, List

from sunsynk.rwsensors import NumberRWSensor, SelectRWSensor, TimeRWSensor
from sunsynk.sensors import (
    FaultSensor,
    InverterStateSensor,
    MathSensor,
    SDStatusSensor,
    Sensor,
    SerialSensor,
    TempSensor,
)

CELSIUS: Final = "°C"
KWH: Final = "kWh"
AMPS: Final = "A"
VOLT: Final = "V"
WATT: Final = "W"

_SENSORS: List[Sensor] = []
DEPRECATED: Dict[str, Sensor] = {}

##########
# Battery
##########
_SENSORS += (
    TempSensor(586, "Battery temperature", CELSIUS, 0.1),
    Sensor(587, "Battery voltage", VOLT, 0.01),
    Sensor(588, "Battery SOC", "%"),
    Sensor(590, "Battery power", WATT, -1),
    Sensor(591, "Battery current", AMPS, -0.01),
)

#################
# Inverter Power
#################
_SENSORS += (
    Sensor(636, "Inverter power", WATT, -1),
    Sensor(633, "Inverter L1 power", WATT, -1),
    Sensor(634, "Inverter L2 power", WATT, -1),
    Sensor(635, "Inverter L3 power", WATT, -1),
    Sensor(627, "Inverter voltage", VOLT, 0.1),
    Sensor(638, "Inverter frequency", "Hz", 0.01),
)

#############
# Grid Power
#############
_SENSORS += (
    Sensor(609, "Grid frequency", "Hz", 0.01),
    Sensor(625, "Grid power", WATT, -1),            # gridTotalPac
    Sensor(622, "Grid L1 power", WATT, -1),         # aPower
    Sensor(623, "Grid L2 power", WATT, -1),         # bPower
    Sensor(624, "Grid L3 power", WATT, -1),         # cPower
    Sensor(601, "Grid voltage", VOLT, 0.1),         # aLineVolt
    MathSensor((610, 611, 612), "Grid current", AMPS, factors=(0.01, 0.01, 0.01)),  # iac1,iac2,iac3
    Sensor(619, "Grid CT power", WATT, -1),         # gridOutsideTotalPac (unsure ??)
)

#############
# Load Power
#############
_SENSORS += (
    Sensor(653, "Load power", WATT, -1),
    Sensor(650, "Load L1 power", WATT, -1),
    Sensor(651, "Load L2 power", WATT, -1),
    Sensor(652, "Load L3 power", WATT, -1),
)

################
# Solar Power 1
################
_SENSORS += (
    Sensor(672, "PV1 power", WATT, -1),
    Sensor(676, "PV1 voltage", VOLT, 0.1),
    Sensor(677, "PV1 current", AMPS, 0.1),
)

################
# Solar Power 2
################
_SENSORS += (
    Sensor(673, "PV2 power", WATT, -1),
    Sensor(678, "PV2 voltage", VOLT, 0.1),
    Sensor(679, "PV2 current", AMPS, 0.1),
)

################
# Solar Power 3 (?? deye 12k only has 2 MPPT)
################
_SENSORS += (
    Sensor(674, "PV3 power", WATT, -1),
    Sensor(680, "PV3 voltage", VOLT, 0.1),
    Sensor(681, "PV3 current", AMPS, 0.1),
)

################
# Solar Power 4 (?? deye 12k only has 2 MPPT)
################
_SENSORS += (
    Sensor(675, "PV4 power", WATT, -1),
    Sensor(682, "PV4 voltage", VOLT, 0.1),
    Sensor(683, "PV4 current", AMPS, 0.1),
)


###################
# Power on Outputs (aka GEN - which has multiple modes on the deye 12k)
###################
_SENSORS += (
    Sensor(667, "Gen power", WATT, -1),
    Sensor(664, "Gen L1 power", WATT, -1),
    Sensor(665, "Gen L2 power", WATT, -1),
    Sensor(666, "Gen L3 power", WATT, -1),
)

###################
# Energy
###################
_SENSORS += (
    Sensor(502, "Day Active Energy", KWH, -0.1),
    Sensor(514, "Day Battery Charge", KWH, 0.1),
    Sensor(515, "Day Battery discharge", KWH, 0.1),
    Sensor(521, "Day Grid Export", KWH, 0.1),
    Sensor(520, "Day Grid Import", KWH, 0.1),
    Sensor(536, "Day Gen Energy", KWH, 0.1),
    Sensor(526, "Day Load Energy", KWH, 0.1),      # I guess "used" = load?
    Sensor(529, "Day PV Energy", KWH, 0.1),
    ### not for 12k?? Sensor(61, "Day Reactive Energy", "kVarh", -0.1),
    ### not for 12k?? Sensor(67, "Month Grid Energy", KWH, 0.1),
    ### not for 12k?? Sensor(66, "Month Load Energy", KWH, 0.1),
    ### not for 12k?? Sensor(65, "Month PV Energy", KWH, 0.1),
    Sensor((506, 507), "Total Active Energy", KWH, 0.1),  # signed?
    Sensor((516, 517), "Total Battery Charge", KWH, 0.1),
    Sensor((518, 519), "Total Battery Discharge", KWH, 0.1),
    Sensor((524, 525), "Total Grid Export", KWH, 0.1),
    Sensor((522, 523), "Total Grid Import", KWH, 0.1),
    Sensor((527, 528), "Total Load Energy", KWH, 0.1),
    Sensor((534, 535), "Total PV Energy", KWH, 0.1),
    ### not for 12k?? Sensor((98, 99), "Year Grid Export", KWH, 0.1),
    ### not for 12k?? Sensor((87, 88), "Year Load Energy", KWH, 0.1),
    ### not for 12k?? Sensor((68, 69), "Year PV Energy", KWH, 0.1),
)

##########
# General
##########
RATED_POWER = Sensor((16, 17), "Rated power", WATT, 0.1)        # 12k incorret: 26850kW
_SENSORS.append(RATED_POWER)
_SENSORS += (
    Sensor(0, "Device Type"),
    FaultSensor((103, 104, 105, 106, 107), "Fault"),            # 12k??
    InverterStateSensor(59, "Overall state"),                   # 12k??
    SDStatusSensor(92, "SD Status", ""),  # type: ignore        # 12k??
    SerialSensor((3, 4, 5, 6, 7), "Serial"),                    # seems good for 12k
    TempSensor(540, "DC transformer temperature", CELSIUS, 0.1),
    TempSensor(217, "Environment temperature", CELSIUS, 0.1),   # 12k: realtimeTemp
    TempSensor(541, "Radiator temperature", CELSIUS, 0.1),
    Sensor(194, "Grid Connected Status"),                       # 12k??
)

## end of changes for 12k for now

###########
# Settings
###########
_SENSORS += (
    Sensor(200, "Control Mode"),
    Sensor(230, "Grid Charge Battery current", AMPS, -1),
    Sensor(232, "Grid Charge enabled", "", -1),
    Sensor(312, "Battery charging voltage", VOLT, 0.01),
    Sensor(603, "Bat1 SOC", "%"),
    Sensor(611, "Bat1 Cycle"),
)

# Absolute min and max voltage based on Deye inverter
MIN_VOLTAGE = 41
MAX_VOLTAGE = 60

BATTERY_EQUALIZATION_VOLTAGE = NumberRWSensor(
    201, "Battery Equalization voltage", VOLT, 0.01, min=MIN_VOLTAGE, max=MAX_VOLTAGE
)
BATTERY_ABSORPTION_VOLTAGE = NumberRWSensor(
    202, "Battery Absorption voltage", VOLT, 0.01, min=MIN_VOLTAGE, max=MAX_VOLTAGE
)
BATTERY_FLOAT_VOLTAGE = NumberRWSensor(
    203, "Battery Float voltage", VOLT, 0.01, min=MIN_VOLTAGE, max=MAX_VOLTAGE
)

BATTERY_SHUTDOWN_CAPACITY = NumberRWSensor(217, "Battery Shutdown Capacity", "%")
BATTERY_RESTART_CAPACITY = NumberRWSensor(218, "Battery Restart Capacity", "%")
BATTERY_LOW_CAPACITY = NumberRWSensor(
    219,
    "Battery Low Capacity",
    "%",
    min=BATTERY_SHUTDOWN_CAPACITY,
    max=BATTERY_RESTART_CAPACITY,
)
BATTERY_SHUTDOWN_CAPACITY.max = BATTERY_LOW_CAPACITY
BATTERY_RESTART_CAPACITY.min = BATTERY_LOW_CAPACITY

BATTERY_SHUTDOWN_VOLTAGE = NumberRWSensor(
    220, "Battery Shutdown voltage", VOLT, 0.01, min=MIN_VOLTAGE
)
BATTERY_RESTART_VOLTAGE = NumberRWSensor(
    221, "Battery Restart voltage", VOLT, 0.01, max=MAX_VOLTAGE
)
BATTERY_LOW_VOLTAGE = NumberRWSensor(
    222,
    "Battery Low voltage",
    VOLT,
    0.01,
    min=BATTERY_SHUTDOWN_VOLTAGE,
    max=BATTERY_RESTART_VOLTAGE,
)
BATTERY_SHUTDOWN_VOLTAGE.max = BATTERY_LOW_VOLTAGE
BATTERY_RESTART_VOLTAGE.min = BATTERY_LOW_VOLTAGE

_SENSORS += (
    BATTERY_EQUALIZATION_VOLTAGE,
    BATTERY_ABSORPTION_VOLTAGE,
    BATTERY_FLOAT_VOLTAGE,
    BATTERY_SHUTDOWN_CAPACITY,
    BATTERY_RESTART_CAPACITY,
    BATTERY_LOW_CAPACITY,
    BATTERY_SHUTDOWN_VOLTAGE,
    BATTERY_RESTART_VOLTAGE,
    BATTERY_LOW_VOLTAGE,
)

#################
# System program
#################
_SENSORS.append(
    SelectRWSensor(243, "Priority Mode", options={0: "Battery first", 1: "Load first"})
)
_SENSORS.append(
    SelectRWSensor(
        244,
        "Load Limit",
        options={0: "Allow Export", 1: "Essentials", 2: "Zero Export"},
    )
)
PROG1_TIME = TimeRWSensor(250, "Prog1 Time")
PROG2_TIME = TimeRWSensor(251, "Prog2 Time", min=PROG1_TIME)
PROG3_TIME = TimeRWSensor(252, "Prog3 Time", min=PROG2_TIME)
PROG4_TIME = TimeRWSensor(253, "Prog4 Time", min=PROG3_TIME)
PROG5_TIME = TimeRWSensor(254, "Prog5 Time", min=PROG4_TIME)
PROG6_TIME = TimeRWSensor(255, "Prog6 Time", min=PROG5_TIME)
PROG1_TIME.min = PROG6_TIME
PROG1_TIME.max = PROG2_TIME
PROG2_TIME.max = PROG3_TIME
PROG3_TIME.max = PROG4_TIME
PROG4_TIME.max = PROG5_TIME
PROG5_TIME.max = PROG6_TIME
PROG6_TIME.max = PROG1_TIME

PROG_CHARGE_OPTIONS = {
    0: "No Grid or Gen",
    1: "Allow Grid",
    2: "Allow Gen",
    3: "Allow Grid & Gen",
}
PROG_MODE_OPTIONS = {
    0: "None",
    4: "General",
    8: "Backup",
    16: "Charge",
}

PROGRAM = (
    PROG1_TIME,
    PROG2_TIME,
    PROG3_TIME,
    PROG4_TIME,
    PROG5_TIME,
    PROG6_TIME,
    NumberRWSensor(256, "Prog1 power", WATT, max=RATED_POWER),
    NumberRWSensor(257, "Prog2 power", WATT, max=RATED_POWER),
    NumberRWSensor(258, "Prog3 power", WATT, max=RATED_POWER),
    NumberRWSensor(259, "Prog4 power", WATT, max=RATED_POWER),
    NumberRWSensor(260, "Prog5 power", WATT, max=RATED_POWER),
    NumberRWSensor(261, "Prog6 power", WATT, max=RATED_POWER),
    NumberRWSensor(268, "Prog1 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    NumberRWSensor(269, "Prog2 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    NumberRWSensor(270, "Prog3 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    NumberRWSensor(271, "Prog4 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    NumberRWSensor(272, "Prog5 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    NumberRWSensor(273, "Prog6 Capacity", "%", min=BATTERY_LOW_CAPACITY),
    SelectRWSensor(274, "Prog1 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(275, "Prog2 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(276, "Prog3 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(277, "Prog4 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(278, "Prog5 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(279, "Prog6 charge", options=PROG_CHARGE_OPTIONS, bitmask=0x03),
    SelectRWSensor(274, "Prog1 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
    SelectRWSensor(275, "Prog2 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
    SelectRWSensor(276, "Prog3 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
    SelectRWSensor(277, "Prog4 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
    SelectRWSensor(278, "Prog5 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
    SelectRWSensor(279, "Prog6 mode", options=PROG_MODE_OPTIONS, bitmask=0x1C),
)
_SENSORS.extend(PROGRAM)
PROG_VOLT = (
    NumberRWSensor(
        262,
        "Prog1 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
    NumberRWSensor(
        263,
        "Prog2 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
    NumberRWSensor(
        264,
        "Prog3 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
    NumberRWSensor(
        265,
        "Prog4 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
    NumberRWSensor(
        266,
        "Prog5 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
    NumberRWSensor(
        267,
        "Prog6 voltage",
        VOLT,
        0.01,
        min=BATTERY_LOW_VOLTAGE,
        max=BATTERY_FLOAT_VOLTAGE,
    ),
)
_SENSORS.extend(PROG_VOLT)


#############
# Deprecated
#############
ALL_SENSORS: Dict[str, Sensor] = {s.id: s for s in _SENSORS}


def _deprecated() -> None:
    """Populate the deprecated sensors."""
    dep_map: Dict[str, Sensor] = {
    }

    for newname, sen in dep_map.items():
        DEPRECATED[sen.id] = ALL_SENSORS[newname]
        ALL_SENSORS[sen.id] = sen


_deprecated()
