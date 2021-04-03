#! /usr/bin/env python

import os
from typing import Union
from zipfile import ZipFile

def getnametuple(myzip):
    """
    Adjustment to ZipFile.namelist() function to prevent MAC-exclusive
    '__MACOSX' and '.DS_Store' files from interfering.
    Only necessary for files compressed with OS 10.3 or earlier.
    Source: https://superuser.com/questions/104500/what-is-macosx-folder
    Command line solution:
        ``` zip -r dir.zip . -x ".*" -x "__MACOSX"
    Source: https://apple.stackexchange.com/questions/239578/compress-without-ds-store-and-macosx

    Parameters
    ----------
    myzip: ZipFile object
    """
    return tuple(
        sorted(
            list(
                itm
                for itm in myzip.namelist()
                if os.path.basename(itm).startswith(".") == False
                and "__MACOSX" not in itm
                and "textClipping" not in itm
                and itm != os.path.splitext(os.path.basename(
                    os.path.dirname(itm)))[0] + "/"
            )
        )
    )

def main():
    if __name__ == __main__:
        getnametuple(myzip)
