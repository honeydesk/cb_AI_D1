import csv
from pathlib import Path
from typing import Dict, List


class RatioCalculator:
    def __init__(self, input_file: Path, output_file: Path) -> None:
        self.input_file = input_file
        self.output_file = output_file

    @staticmethod
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

    def calculate_row(self, row: Dict[str, str]) -> Dict[str, str]:
        row["price_to_book_ratio"] = self.safe_ratio(row.get("price", ""), row.get("book_ratio", ""))
        row["pe_ratio"] = self.safe_ratio(row.get("price", ""), row.get("eps", ""))
        return row

    def run(self) -> None:
        with self.input_file.open("r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            if reader.fieldnames is None:
                raise ValueError("Input CSV has no header row.")

            output_fields = [
                *reader.fieldnames,
                "price_to_book_ratio",
                "pe_ratio",
            ]

            rows: List[Dict[str, str]] = [self.calculate_row(row) for row in reader]

        with self.output_file.open("w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=output_fields)
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1] / "2_ratios"
    calculator = RatioCalculator(
        input_file=base_dir / "in.csv",
        output_file=base_dir / "out.csv",
    )
    calculator.run()


if __name__ == "__main__":
    main()