#!/usr/bin/env python3

from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

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

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self  # Don't forget to return self


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
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")
        print()
    except Exception as e:
        print("Expected validation error:")
        print(f"Error: ***{e}***")


if __name__ == "__main__":
    main()
