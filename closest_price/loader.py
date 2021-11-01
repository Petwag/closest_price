import csv
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Loader:
    values: Optional[List[float]] = field(default_factory=list)

    def load_csv(self, file_path, delimiter=" "):
        # Load csv file and fetch data
        with open(file_path, newline="") as csv_file:
            spamreader = csv.reader(csv_file, delimiter=delimiter)
            self.values.extend([float(row[0]) for row in spamreader])

        return self.values

    def load_input(self, value: float):
        self.values.append(value)

        return self.values
