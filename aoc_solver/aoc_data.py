# import from standard library packages
from dataclasses import dataclass
import itertools
from typing import Callable, Optional, Tuple

# import from third-party packages
import polars
from polars import DataFrame


# create class to hold puzzle input data from https://adventofcode.com/
@dataclass
class AoCData:
    raw_data: str

    def __post_init__(self):
        """ remove any trailing white space from self.raw_data """
        self.raw_data = self.raw_data.strip()

    def __repr__(self):
        """ returns the default string representation of self.raw_data """
        return self.raw_data

    @property
    def as_int(self):
        """
            returns self.raw_data as an int after filtering out all non-digits
        """
        return int(''.join(char for char in self.raw_data if str.isdigit(char)))

    @property
    def as_polars(self):
        """
            AoCData.as_polars = AoCData.create_polars(int, None) with any
            amount of contiguous white space treated as a single column
            delimiter and all values coerced to integers
        """
        return self.create_polars(int, None)

    def create_polars(
        self,
        dtype: Callable = str,
        separator: Optional[str] = ''
    ) -> DataFrame:
        """
            returns self.raw_data as a polars DataFrame with standardized
            column names, attempting to coerce all values to the provided data
            type, treating the provided seperator as column delimiters, and
            naming columns col1, col2, ..., col<n>
        """
        rows = list(
            zip(
                *itertools.zip_longest(
                    *[
                        [
                            dtype(i) for i in (
                                row.split(separator) if separator != ''
                                else list(row)
                            )
                        ]
                        for row in self.raw_data.splitlines() if row
                    ]
                )
            )
        )
        number_of_columns = max(len(row) for row in rows)
        column_names = [f'col{i+1}' for i in range(number_of_columns)]
        return polars.DataFrame(
            data=rows,
            schema=column_names,
            strict=False,
            orient='row',
        )

    @property
    def as_string(self):
        return self.raw_data

    @property
    def as_tuple(self):
        """
            AoCData.as_tuple = AoCData.create_tuple(int, None) with any
            amount of contiguous white space treated as a single column
            delimiter and all values coerced to integers
        """
        return self.create_tuple(int, None)

    def create_tuple(
        self,
        dtype: Callable = str,
        separator: Optional[str] = '\n\n'
    ) -> Tuple:
        """
            returns self.raw_data as a tuple, attempting to coerce all values
            to the provided data type and treating the provided seperator as
            element delimiters
        """
        return tuple(dtype(i) for i in self.raw_data.split(separator))


# inline test code follows
if __name__ == '__main__':

    test_data = AoCData('1 2 3\n7 8\n9\n\n4 10\n5 11\n6 12 13\n')
    print(f'{test_data=}')
    print(f'{test_data.as_int=}')
    print(f'{test_data.as_polars=}')
    print(f'{test_data.create_polars()=}')
    print(f'{test_data.as_string=}')
    print(f'{test_data.as_tuple=}')
    print(f'{test_data.create_tuple()=}')
