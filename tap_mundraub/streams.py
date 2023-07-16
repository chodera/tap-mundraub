"""Stream type classes for tap-mundraub."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mundraub.client import mundraubStream

class PlantsStream(mundraubStream):
    """Define custom stream."""

    name = "plants"
    path = "plant?bbox=-180,-90,180,90&zoom=16&cat=4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37"
    primary_keys = ["nid"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("latitude", th.StringType),
        th.Property("longitude", th.StringType),
        th.Property("nid", th.IntegerType),
        th.Property("tid", th.IntegerType),
    ).to_dict()
