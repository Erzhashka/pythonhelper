from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator

class ContactType(str, Enum):

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):

    contact_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Unique contact identifier (must start with 'AC')"
    )

    timestamp: datetime = Field(
        ...,
        description="Date and time of contact"
    )

    location: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Geographic location of contact"
    )

    contact_type: ContactType = Field(
        ...,
        description="Type of alien contact"
    )

    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Signal strength on 0-10 scale"
    )

    duration_minutes: int = Field(
        ...,
        ge=1,
        le=1440,
        description="Duration in minutes (1-1440, max 24 hours)"
    )

    witness_count: int = Field(
        ...,
        ge=1,
        le=100,
        description="Number of witnesses (1-100)"
    )

    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional message received from contact"
    )

    is_verified: bool = Field(
        default=False,
        description="Whether the contact has been verified"
    )

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include a received message")

        return self

def display_contact(contact: AlienContact) -> None:

    verified_status = "Verified" if contact.is_verified else "Unverified"
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Timestamp: {contact.timestamp.strftime('%Y-%m-%d %H:%M')}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Status: {verified_status}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")

def main() -> None:

    print("Alien Contact Log Validation")
    print("=" * 40)
    print()

    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-03-15T22:30:00",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        display_contact(valid_contact)
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print()
    print("=" * 40)
    print()

    print("Testing: Telepathic contact with only 1 witness")
    try:
        invalid_telepathic = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-03-16T03:00:00",
            location="Remote Mountain, Tibet",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=120,
            witness_count=1,
            is_verified=False
        )
        display_contact(invalid_telepathic)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Unverified physical contact")
    try:
        invalid_physical = AlienContact(
            contact_id="AC_2024_003",
            timestamp="2024-03-17T14:00:00",
            location="Farm, Nebraska",
            contact_type=ContactType.PHYSICAL,
            signal_strength=3.0,
            duration_minutes=30,
            witness_count=2,
            is_verified=False
        )
        display_contact(invalid_physical)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Invalid contact ID (doesn't start with 'AC')")
    try:
        invalid_id = AlienContact(
            contact_id="XY_2024_001",
            timestamp="2024-03-18T09:00:00",
            location="Desert, Arizona",
            contact_type=ContactType.VISUAL,
            signal_strength=4.0,
            duration_minutes=15,
            witness_count=3,
            is_verified=False
        )
        display_contact(invalid_id)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print()
    print("=" * 40)
    print()

    print("Testing: Strong signal (8.0) without message")
    try:
        invalid_signal = AlienContact(
            contact_id="AC_2024_004",
            timestamp="2024-03-19T20:00:00",
            location="Observatory, Hawaii",
            contact_type=ContactType.RADIO,
            signal_strength=8.0,
            duration_minutes=60,
            witness_count=4,
            message_received=None,
            is_verified=True
        )
        display_contact(invalid_signal)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"  - {error['msg']}")

if __name__ == "__main__":
    main()
