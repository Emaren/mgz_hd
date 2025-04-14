from mgz_hd.mgz.header.hd import hd as HDStruct
from construct import Container

class Header:
    def __init__(self, data: bytes):
        self.raw: Container = HDStruct.parse(data)

    def get_players(self):
        return [
            {
                "name": p.name.value.decode("utf-8", errors="ignore") if hasattr(p.name, "value") else "Unknown",
                "civ_id": p.civ_id,
                "steam_id": p.steam_id,
                "color_id": p.color_id,
                "team_index": p.team_index,
                "type": p.type
            }
            for p in getattr(self.raw, "players", [])
        ]

    def get_civilizations(self):
        return [p.civ_id for p in getattr(self.raw, "players", [])]

    def get_duration(self):
        # HD doesn't encode duration in header. Return 0 for now.
        return 0

    def get_version(self):
        return str(self.raw.version)

    def get_map(self):
        return {
            "id": getattr(self.raw, "resolved_map_id", -1),
            "name": "Unknown"
        }

    def get_events(self):
        # Placeholder — you probably had logic elsewhere
        return []
