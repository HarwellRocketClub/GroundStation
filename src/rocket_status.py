from enum import Enum, unique


@unique
class RocketStatus(Enum):
    IN_FLIGHT = {"colour": "rgb(51, 255, 51)", "text": "In Flight"}
    READY_FOR_FLIGHT = {"colour": "rgb(51, 153, 255)", "text": "Ready For Flight"}
    READYING = {"colour": "rgb(255, 255, 51)", "text": "Readying"}
    OFFLINE = {"colour": "rgb(255, 51, 51)", "text": "Offline"}
