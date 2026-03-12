from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError

class SpaceStation(BaseModel):

    station_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Unique identifier for the space station"
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Name of the space station"
    )

    crew_size: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of crew members (1-20)"
    )

    power_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Power level percentage (0-100)"
    )

    oxygen_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Oxygen level percentage (0-100)"
    )

    last_maintenance: datetime = Field(
        ...,
        description="Date and time of last maintenance"
    )

    is_operational: bool = Field(
        default=True,
        description="Whether the station is operational"
    )

    notes: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Optional notes about the station"
    )

def display_station(station: SpaceStation) -> None:

    status = "Operational" if station.is_operational else "Non-operational"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last Maintenance: {station.last_maintenance.strftime('%Y-%m-%d %H:%M')}")
    print(f"Status: {status}")
    if station.notes:
        print(f"Notes: {station.notes}")

def main() -> None:

    print("Space Station Data Validation")
    print("=" * 40)
    print()

    print("Valid station created:")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-03-15T10:30:00",
            is_operational=True,
            notes="All systems nominal"
        )
        display_station(valid_station)
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print()
    print("=" * 40)
    print()

    print("Attempting to create invalid station (crew_size=25):")
    try:
        invalid_station = SpaceStation(
            station_id="TST002",
            name="Test Station",
            crew_size=25,
            power_level=75.0,
            oxygen_level=88.0,
            last_maintenance="2024-03-10T08:00:00"
        )
        display_station(invalid_station)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['loc'][0]}: {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Demonstrating automatic type conversion:")
    print("Passing string '2024-01-01T12:00:00' to datetime field...")
    station_auto = SpaceStation(
        station_id="AUTO01",
        name="Auto Convert Station",
        crew_size=3,
        power_level=90.0,
        oxygen_level=95.0,
        last_maintenance="2024-01-01T12:00:00"
    )
    print(f"Converted to: {station_auto.last_maintenance} (type: {type(station_auto.last_maintenance).__name__})")

if __name__ == "__main__":
    main()
