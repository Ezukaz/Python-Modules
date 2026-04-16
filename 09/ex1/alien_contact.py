#!/usr/bin/env python3

from pydantic import BaseModel, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: ContactType
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_received: str | None = None
    is_verified: bool

    @model_validator(mode='after')
    def validate(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Id must start with "AC"')
        if not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witness")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals must include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-01-01",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=3,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        contact.validate()
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        plural_suf = f"{'s' if contact.duration_minutes != 1 else ''}"
        print(f"Duration: {contact.duration_minutes} minute{plural_suf}")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: {contact.message_received}")
    except Exception as e:
        print("Expected validation error:")
        print(f"Error: ***{e}***")
