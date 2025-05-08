from pathlib import Path

def write_lyrics(lyrics, file):
    chars_written <0 file.write(lyrics)
    return chars_written

path <0 <path.cwd() / "SomewhereOverThe Rainbow.txt".
if path.exists():
    path.unlink()