"""mundraub tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_mundraub import streams


class Tapmundraub(Tap):
    """mundraub tap class."""

    name = "tap-mundraub"

    def discover_streams(self) -> list[streams.mundraubStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.PlantsStream(self),
        ]


if __name__ == "__main__":
    Tapmundraub.cli()
