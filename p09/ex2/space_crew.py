from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator

class Rank(str, Enum):

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"

class CrewMember(BaseModel):

    member_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Unique crew member identifier"
    )

    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Full name of the crew member"
    )

    rank: Rank = Field(
        ...,
        description="Military/organizational rank"
    )

    age: int = Field(
        ...,
        ge=18,
        le=80,
        description="Age in years (18-80)"
    )

    specialization: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Area of expertise"
    )

    years_experience: int = Field(
        ...,
        ge=0,
        le=50,
        description="Years of professional experience (0-50)"
    )

    is_active: bool = Field(
        default=True,
        description="Whether the crew member is active duty"
    )

class SpaceMission(BaseModel):

    mission_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Unique mission identifier (must start with 'M')"
    )

    mission_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Name of the mission"
    )

    destination: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Mission destination"
    )

    launch_date: datetime = Field(
        ...,
        description="Scheduled launch date and time"
    )

    duration_days: int = Field(
        ...,
        ge=1,
        le=3650,
        description="Mission duration in days (1-3650, max 10 years)"
    )

    crew: List[CrewMember] = Field(
        ...,
        min_length=1,
        max_length=12,
        description="List of crew members (1-12)"
    )

    mission_status: str = Field(
        default="planned",
        description="Current mission status"
    )

    budget_millions: float = Field(
        ...,
        ge=1.0,
        le=10000.0,
        description="Budget in millions of dollars (1-10000)"
    )

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leadership_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        has_leader = any(member.rank in leadership_ranks for member in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            required_experienced = len(self.crew) / 2
            if experienced_count < required_experienced:
                raise ValueError(
                    f"Long missions (>{365} days) require at least 50% experienced "
                    f"crew (5+ years). Found {experienced_count}/{len(self.crew)} "
                    f"experienced members."
                )

        inactive_members = [m.name for m in self.crew if not m.is_active]
        if inactive_members:
            raise ValueError(
                f"All crew members must be active. Inactive: {', '.join(inactive_members)}"
            )

        return self

def display_crew_member(member: CrewMember, indent: str = "  ") -> None:

    print(f"{indent}- {member.name} ({member.rank.value}) - {member.specialization}")
    print(f"{indent}  Experience: {member.years_experience} years, Age: {member.age}")

def display_mission(mission: SpaceMission) -> None:

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Launch Date: {mission.launch_date.strftime('%Y-%m-%d')}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Status: {mission.mission_status}")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        display_crew_member(member)

def main() -> None:

    print("Space Mission Crew Validation")
    print("=" * 40)
    print()

    commander = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        specialization="Mission Command",
        years_experience=20,
        is_active=True
    )

    lieutenant = CrewMember(
        member_id="LT002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=10,
        is_active=True
    )

    officer = CrewMember(
        member_id="OF003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=28,
        specialization="Engineering",
        years_experience=5,
        is_active=True
    )

    print("Valid mission created:")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-06-15T09:00:00",
            duration_days=900,
            crew=[commander, lieutenant, officer],
            mission_status="planned",
            budget_millions=2500.0
        )
        display_mission(valid_mission)
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print()
    print("=" * 40)
    print()

    print("Testing: Mission without Commander or Captain")
    try:
        cadet1 = CrewMember(
            member_id="CD001",
            name="Young Cadet",
            rank=Rank.CADET,
            age=22,
            specialization="Science",
            years_experience=1,
            is_active=True
        )
        cadet2 = CrewMember(
            member_id="CD002",
            name="Another Cadet",
            rank=Rank.OFFICER,
            age=25,
            specialization="Medical",
            years_experience=2,
            is_active=True
        )

        invalid_no_leader = SpaceMission(
            mission_id="M2024_001",
            mission_name="Moon Survey",
            destination="Moon",
            launch_date="2024-09-01T12:00:00",
            duration_days=30,
            crew=[cadet1, cadet2],
            budget_millions=100.0
        )
        display_mission(invalid_no_leader)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Invalid mission ID")
    try:
        invalid_id_mission = SpaceMission(
            mission_id="X2024_001",
            mission_name="Test Mission",
            destination="Space Station",
            launch_date="2024-08-01T10:00:00",
            duration_days=7,
            crew=[commander],
            budget_millions=50.0
        )
        display_mission(invalid_id_mission)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Long mission with inexperienced crew")
    try:
        inexperienced1 = CrewMember(
            member_id="IN001",
            name="Rookie One",
            rank=Rank.OFFICER,
            age=24,
            specialization="Pilot",
            years_experience=2,
            is_active=True
        )
        inexperienced2 = CrewMember(
            member_id="IN002",
            name="Rookie Two",
            rank=Rank.OFFICER,
            age=26,
            specialization="Engineer",
            years_experience=3,
            is_active=True
        )

        invalid_inexperienced = SpaceMission(
            mission_id="M2024_LONG",
            mission_name="Jupiter Exploration",
            destination="Jupiter",
            launch_date="2025-01-01T00:00:00",
            duration_days=730,
            crew=[commander, inexperienced1, inexperienced2],
            budget_millions=5000.0
        )
        display_mission(invalid_inexperienced)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Mission with inactive crew member")
    try:
        inactive_member = CrewMember(
            member_id="IA001",
            name="Retired Pilot",
            rank=Rank.LIEUTENANT,
            age=55,
            specialization="Navigation",
            years_experience=30,
            is_active=False
        )

        invalid_inactive = SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Flight",
            destination="Orbit",
            launch_date="2024-07-01T08:00:00",
            duration_days=3,
            crew=[commander, inactive_member],
            budget_millions=25.0
        )
        display_mission(invalid_inactive)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

if __name__ == "__main__":
    main()
