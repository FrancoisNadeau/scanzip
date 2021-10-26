#! /usr/bin/env python

import os
import zipfile
from tqdm import tqdm
from typing import Union
from os.path import expanduser as xpu
import pandas as pd
from loadutils.filterlist_exc import filterlist_exc
from loadutils.filterlist_inc import filterlist_inc
from get_ntpl import get_ntpl
from zscanner import zscanner
from save_archv import save_archv
from xtrct_archv import xtrct_archv

def scan_zip(
    archv_path: Union[os.PathLike, str],
    ntpl: Union[str, list, tuple] = None,
    exclude: Union[str, list, tuple] = None,
    to_xtrct: Union[str, list, tuple] = None,
    dst_path: Union[str, os.PathLike] = None,
    get_bufs: bool = False
) -> object:
    ''' Scans contents of ZipFile object.

    Returns DataFrame containing typical ZipFile.ZipInfos
    objects informations along with a raw bytes buffer
    for future editing if desired.

    Args:
        archv_path: Path to the zip file to scan
        ntpl: Sequence of file names from the archive
              - See help(getnametpl) for more details
        exclude: Sequence of either names, extensions or
                 some pattern found in file names of files
                 to be excluded from 'scanzip' return value
    Returns:
        DataFrame containing info about zip file contents

    '''
    myzip = zipfile.ZipFile(archv_path)
    ntpl = get_ntpl(myzip, ntpl, exclude)
    vals = zscanner(myzip, ntpl)
    vals['filename'] = [row[1].filename.replace("/", "_")
                        for row in vals.iterrows()]
    vals['src_names'] = sorted(ntpl)
    if get_bufs:
        vals['bsheets'] = [myzip.open(row[1].src_names).read().lower()
                           for row in tqdm(vals.iterrows(),
                                           desc = "reading archive")]

    myzip.close()    

    if to_xtrct:
        save_archv(vals, to_xtrct, dst_path)
        return xtrct_archv(vals, to_xtrct, dst_path)
    else:
        return vals

def main():    
    if __name__ == "__main__":
        scan_zip(archv_path, ntpl, exclude, to_xtrct, dst_path)
