"""Extract basic object inventories from an EPA SWMM INP file."""
import re, csv, argparse
from pathlib import Path

def parse_section(text, section):
    m = re.search(r"(?ms)^\\[" + re.escape(section) + r"\\]\\s*\\n(.*?)(?=^\\[|\\Z)", text)
    if not m:
        return []
    rows = []
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s or s.startswith(";"):
            continue
        rows.append(re.split(r"\\s+", s.split(";;")[0].strip()))
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inp", help="Path to SWMM .inp file")
    parser.add_argument("--output", default="extracted_data")
    args = parser.parse_args()
    text = Path(args.inp).read_text(errors="replace")
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    sections = {
        "SUBCATCHMENTS": ["subcatchment","rain_gage","outlet","area","percent_impervious","width","percent_slope","curb_length","snow_pack"],
        "JUNCTIONS": ["node","elevation","max_depth","init_depth","sur_depth","aponded"],
        "CONDUITS": ["conduit","from_node","to_node","length","roughness","in_offset","out_offset","init_flow","max_flow"],
        "LID_USAGE": ["subcatchment","lid_control","number","area","width","init_sat","from_imperv","to_perv","report_file","drain_to","from_perv"],
    }
    for section, headers in sections.items():
        rows = parse_section(text, section)
        with (out / (section.lower()+".csv")).open("w", newline="") as f:
            writer = csv.writer(f); writer.writerow(headers); writer.writerows(rows)
        print(f"{section}: {len(rows)} records")

if __name__ == "__main__":
    main()
