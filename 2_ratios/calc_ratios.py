import csv
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("in.csv")
OUTPUT_FILE = Path(__file__).with_name("out.csv")


def safe_ratio(numerator: str, denominator: str) -> str:
    """Return numerator/denominator as a string, or empty string if invalid."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return ""
        return f"{num / den:.6f}"
    except (TypeError, ValueError):
        return ""


def main() -> None:
    with INPUT_FILE.open("r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        if reader.fieldnames is None:
            raise ValueError("Input CSV has no header row.")

        output_fields = [
            *reader.fieldnames,
            "price_to_book_ratio",
            "pe_ratio",
        ]

        rows = []
        for row in reader:
            row["price_to_book_ratio"] = safe_ratio(row.get("price", ""), row.get("book_ratio", ""))
            row["pe_ratio"] = safe_ratio(row.get("price", ""), row.get("eps", ""))
            rows.append(row)

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()