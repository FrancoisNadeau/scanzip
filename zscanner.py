#!usr/bin/env/python3

import os
import zipfile
from typing import Union
import pandas as pd

from getnametuple import getnametuple
from loadutils.evenodd import evenodd

def zscanner(
    myzip: Union[str, zipfile.ZipFile],
    ntpl: Union[list, tuple] = None,
    exclude: Union[str, list, tuple] = None
) -> pd.DataFrame:
    return pd.DataFrame(tuple(dict((zip(evenodd(itm)[0],
                              evenodd(itm)[1])))
                    for itm in tuple(tuple(
                        snif.is_printable(repr(itm.lower()))
                        .strip()
                        .replace("'", "")
                        .replace("'", "")
                        .replace("=", " ")[:-2]
                        .split())[1:] for itm in tqdm(
                        set(repr(myzip.getinfo(itm)).strip(" ")
                            .replace(itm, itm.replace(" ", "_"))
                            if " " in itm
                            else repr(myzip.getinfo(itm)).strip(" ")
                            for itm in get_ntpl(myzip, ntpl, exclude)),
                        desc = "scanning archive"))),
              dtype = object).sort_values("filename").reset_index(drop=True)

def main():
    if __name__ == __main__:
        zscanner(myzip, ntpl, exclude)

