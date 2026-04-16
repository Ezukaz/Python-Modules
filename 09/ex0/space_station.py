#!/usr/bin/env python3

from pydantic import BaseModel, field_validator
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    # ISO 8601は日時の国際標準フォーマット。基本形は：
    # YYYY-MM-DD
    # YYYY-MM-DDTHH:MM:SS
    # YYYY-MM-DDTHH:MM:SSZ  # Z = UTC
    is_operational: bool
    notes: str | None = None

    @field_validator("crew_size")
    @classmethod
    def validate_crew(cls, v) -> int:
        if v > 20 or v < 0:
            raise ValueError(
                "Input should be less than or equal to 20 and "
                "above or equal to 0"
            )
        return v

    @field_validator("power_level")
    @classmethod
    def validate_power(cls, v) -> float:
        if v > 100 or v < 0:
            raise ValueError(
                "Input should be less than or equal to 100 and "
                "more or equal to 0"
            )
        return v

    @field_validator("oxygen_level")
    @classmethod
    def validate_oxygen(cls, v) -> float:
        if v > 100 or v < 0:
            raise ValueError(
                "Input should be less than or equal to 100 and "
                "more or equal to 0"
            )
        return v


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=81.3,
            oxygen_level=94.6,
            last_maintenance="2024-04-13",
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(
            f"Crew: {station.validate_crew(station.crew_size)} "
            f"{'people' if station.crew_size != 1 else 'person'}"
        )
        print(f"Power: {station.validate_power(station.power_level)}%")
        print(f"Oxygen: {station.validate_oxygen(station.oxygen_level)}%")
        print(
            "Status: "
            f"{'Operational' if station.is_operational else 'Disfunctional'}"
        )
    except Exception as e:
        print("Expected validation error:")
        print(f"Error: ***{e}***")
