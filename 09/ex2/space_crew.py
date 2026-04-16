#!/usr/bin/env python3

from pydantic import BaseModel, model_validator, field_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str
    name: str
    rank: Rank
    age: int
    specialization: str
    years_experience: int
    is_active: bool = True

    @field_validator("member_id")
    @classmethod
    def valid_id(cls, v) -> str:
        vlen = len(v)
        if vlen < 3 or vlen > 10:
            raise ValueError("Must be between 3 and 10 characters long")
        return v

    @field_validator("name")
    @classmethod
    def valid_name(cls, v) -> str:
        vlen = len(v)
        if vlen < 2 or vlen > 50:
            raise ValueError("Must be between 2 and 50 characters long")
        return v

    @field_validator("age")
    @classmethod
    def valid_age(cls, v) -> int:
        if v > 80 or v < 18:
            raise ValueError("Must be between 18 and 80 years old")
        return v

    @field_validator("specialization")
    @classmethod
    def valid_special(cls, v) -> str:
        vlen = len(v)
        if vlen < 3 or vlen > 30:
            raise ValueError("Must be between 3 and 30 characters long")
        return v

    @field_validator("years_experience")
    @classmethod
    def valid_xp(cls, v) -> int:
        if v < 0 or v > 50:
            raise ValueError("Must have 0 to 50 years of experience")
        return v


class SpaceMission(BaseModel):
    mission_id: str
    mission_name: str
    destination: str
    launch_date: datetime
    duration_days: int
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float

    @field_validator("mission_id")
    @classmethod
    def valid_id(cls, v) -> str:
        vlen = len(v)
        if vlen < 5 or vlen > 15:
            raise ValueError("Must be between 5 and 15 characters long")
        return v

    @field_validator("mission_name")
    @classmethod
    def valid_name(cls, v) -> str:
        vlen = len(v)
        if vlen < 3 or vlen > 100:
            raise ValueError("Must be between 3 and 100 characters long")
        return v

    @field_validator("destination")
    @classmethod
    def valid_dest(cls, v) -> str:
        vlen = len(v)
        if vlen < 3 or vlen > 50:
            raise ValueError("Must be between 3 and 50 characters long")
        return v

    @field_validator("duration_days")
    @classmethod
    def valid_dur(cls, v) -> int:
        if v < 1 or v > 3650:
            raise ValueError("Must be between 1 and 3650 days")
        return v

    @field_validator("crew")
    @classmethod
    def valid_crew(cls, v) -> list[CrewMember]:
        vlen = len(v)
        if vlen < 1 or vlen > 12:
            raise ValueError("Must be between 1 and 12 members")
        return v

    @field_validator("budget_millions")
    @classmethod
    def valid_budget(cls, v) -> float:
        if v < 1.0 or v > 10000.0:
            raise ValueError("Must be between 1.0 and 10000.0 million dollars")
        return v

    @model_validator(mode='after')
    def validation(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        if not any(
            True for m in self.crew if m.rank == Rank.COMMANDER
            or m.rank == Rank.CAPTAIN
        ):
            raise ValueError("Must have at least one Commander or Captain")

        over_5_xp = [m for m in self.crew if m.years_experience >= 5]
        crew_count = len(self.crew)
        xp_percent = len(over_5_xp) / crew_count if crew_count else 0
        if self.duration_days > 365 and not xp_percent >= 0.5:
            raise ValueError(
                "Long missions (> 365 days) "
                "need 50% experienced crew (5+ years)"
            )

        if not all(True for m in self.crew if m.is_active):
            raise ValueError("All crew members must be active")


def crew_factory() -> list[CrewMember]:
    crew_data = [
        ("M01", "Alice Chen", Rank.COMMANDER, 45, "Navigation", 20, True),
        ("M02", "Bob Tanaka", Rank.CAPTAIN, 38, "Engineering", 15, True),
        ("M03", "Sara Kim", Rank.LIEUTENANT, 29, "Medicine", 6, True),
        ("M04", "James Obi", Rank.OFFICER, 32, "Weapons", 8, True),
        ("M05", "Yuki Mori", Rank.CADET, 22, "Science", 1, True),
        ("M06", "Leo Rossi", Rank.OFFICER, 35, "Piloting", 10, True),
        ("M07", "Nadia Patel", Rank.LIEUTENANT, 41, "Media", 12, True),
        ("M08", "Omar Hassan", Rank.CADET, 23, "Geology", 2, True),
        ("M09", "Eva Larsson", Rank.OFFICER, 30, "Biology", 5, True),
        ("M10", "Kai Nguyen", Rank.LIEUTENANT, 36, "Astrophysics", 9, True),
        ("M11", "Priya Singh", Rank.CADET, 21, "Chemistry", 0, True),
        ("M12", "Tomas Bauer", Rank.OFFICER, 44, "Security", 18, True),
        # ("M13", "Zoe Carter", Rank.CADET, 24, "Meteorology", 3, True),
    ]
    crew = []
    for c in crew_data:
        crew.append(CrewMember(
            member_id=c[0],
            name=c[1],
            rank=c[2],
            age=c[3],
            specialization=c[4],
            years_experience=c[5],
            is_active=c[6],
        ))
    return crew


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        crew_members = crew_factory()
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-11-05",
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_id}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print(f"Crew members:")
        print(*(f"- {n} ({r}) - {sp}" for _, n, r, _, sp, _, _ in mission.crew), sep="\n")
    except Exception as e:
        print("Expected validation error:")
        print(f"Error: ***{e}***")


main()
