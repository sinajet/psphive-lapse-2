import datetime
from pathlib import Path

def make_timestamp():
    now = datetime.datetime.now()
    centiseconds = f"{int(now.microsecond/10000):02d}"
    return now.strftime(f"%d/%m/%Y-%H:%M:%S.{centiseconds}")

def collect_files(base_dir: Path):
    files = []
    for path in base_dir.rglob("*"):
        if path.is_file():
            rel_path = path.relative_to(base_dir).as_posix()
            files.append(rel_path)
    return files

def build_manifest(files, title_comment="# PS-Phive! For PS4 7.00-9.60 By Leeful/Sinajet"):
    lines = []
    lines.append("CACHE MANIFEST")
    lines.append(title_comment)
    lines.append(f"# {make_timestamp()}")
    lines.append("")

    for f in files:
        lines.append(f)

    lines.append("")
    lines.append("NETWORK:")
    lines.append("*")
    lines.append("")
    lines.append("SETTINGS:")
    lines.append("prefer-online:")
    return "\n".join(lines)

def write_manifest(output_path, files, title_comment=None):
    manifest = build_manifest(files, title_comment=title_comment or "# PS-Phive! For PS4 7.00-9.60 By Leeful/Sinajet")
    Path(output_path).write_text(manifest, encoding="utf-8")
    return output_path

if __name__ == "__main__":
    host_dir = input("Enter the path to the hosts folder: ").replace("& '",'').replace("'",'').replace('"','').strip()
    base_dir = Path(host_dir)

    if not base_dir.exists() or not base_dir.is_dir():
        print("The path is not valid.")
    else:
        files = collect_files(base_dir)
        out = write_manifest(host_dir+"\\offline.cache", files)
        print(f"Manifest created: {out}")
