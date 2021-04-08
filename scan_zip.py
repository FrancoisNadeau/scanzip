#! /usr/bin/env python

import os
import zipfile
from tqdm import tqdm
from typing import Union
from os.path import expanduser as xpu
import pandas as pd
from load_utils.evenodd import evenodd
from load_utils.get_dst_path import get_dst_path
from sniffbytes.filter_lst_exc import filter_lst_exc
from sniffbytes.filter_lst_inc import filter_lst_inc
from sniffbytes.stream2file import stream2file
from .get_ntpl import get_ntpl
from .zscanner import zscanner
from .save_archv import save_archv
from .xtrct_archv import xtct_archv

def scan_zip(
    archv_path: Union[os.PathLike, str],
    ntpl: Union[str, list, tuple] = None,
    exclude: Union[str, list, tuple] = None,
    to_xtrct: Union[str, list, tuple] = None,
    dst_path: Union[str, os.PathLike] = None
) -> object:
    ''' Scans contents of ZipFile object as bytes
        Returns DataFrame containing typical ZipFile.ZipInfos
        objects informations along with a raw bytes buffer
        for future editing

        Parameters
        ----------
        archv_path: Path to zip file
        ntpl: Sequence of file names from the archive
                - See - help(getnametpl)
        exclude: Sequence of either names, extensions or
                 some pattern found in file names of files
                 to be excluded from 'scanzip' return value
    '''
    myzip = zipfile.ZipFile(archv_path)
    ntpl = get_ntpl(myzip, ntpl, exclude)
    vals = zscanner(myzip, ntpl)
    vals['filename'] = [row[1].filename.replace("/", "_")
                        for row in vals.iterrows()]
    vals['src_names'] = sorted(ntpl)
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
