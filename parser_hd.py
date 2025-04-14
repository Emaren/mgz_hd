import logging
from mgz_hd.header import Header
from mgz_hd.resign import detect_resign  # assuming this exists now

def parse_hd_replay(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        header = Header(data)  # ← FIXED THIS LINE

        return {
            "players": header.get_players(),
            "civs": header.get_civilizations(),
            "duration": header.get_duration(),
            "version": header.get_version(),
            "map": header.get_map(),
            "winner": detect_resign(header.get_events()),
        }

    except Exception as e:
        logging.error(f"Failed to parse HD replay: {file_path} — {e}")
        return None
