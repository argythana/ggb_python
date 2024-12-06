"""
Parse NACE codes from ELSTAT file.
Create a dictionary with the two digits codes and their corresponding descriptions.
Download the file from ELSTAT website: https://www.statistics.gr/el/economic-activities
The MIS works the nace rev.2 codes.
The correct file url is:
https://www.statistics.gr/documents/20181/1554245/EconActiv_nace_2_gr.xls/988ff8f0-95b5-4e2f-acb8-87760096dce1
The code is in the column `CD` and the description in the column `DSCR`.
Keep only the rows with two digits codes.
Save the codes in a dictionary as string.
"""

import pandas as pd


def parse_nace_codes(filename: str) -> dict:
    """
    Args: filename: str: path to the file with the NACE codes.
        Parse NACE codes from ELSTAT file.
        Create a dictionary with the two digits codes and their corresponding descriptions.
    Return:
        dict: dictionary with the two digits codes and their corresponding descriptions.
    """

    nace_codes = pd.read_excel(filename)
    nace_codes = nace_codes[["CD", "DSCR"]]

    # strip whitespace from column 'CD' values
    nace_codes["CD"] = nace_codes["CD"].str.strip()
    # strip ' \xa0' from column 'DSCR' values
    nace_codes["DSCR"] = nace_codes["DSCR"].str.replace(" \xa0", "")

    # keep rows with two digits codes
    nace_codes = nace_codes[nace_codes["CD"].apply(lambda x: len(str(x)) == 2)]

    nace_codes.loc[:, "CD"] = nace_codes["CD"].apply(str)
    nace_codes = nace_codes.set_index("CD")
    nace_codes = nace_codes.to_dict()["DSCR"]

    return nace_codes
