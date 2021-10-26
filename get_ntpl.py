#!usr/bin/env/python3

from typing import Union
from getnametuple import getnametuple
import zipfile
from loadutils.filterlist_inc import filterlist_inc

def get_ntpl(
    myzip: zipfile.ZipFile,
    ntpl: Union[list, tuple] = None,
    exclude: Union[str, list, tuple] = None
) -> list:
    return [ntpl if ntpl else
            [filter_lst_exc(exclude,
                            getnametuple(myzip))
             if exclude else getnametuple(myzip)][0]][0]

def main():
    if __name__ == __main__:
        get_ntpl(myzip, ntpl, exclude)
