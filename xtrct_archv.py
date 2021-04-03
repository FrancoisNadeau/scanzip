#!usr/bin/env/python3

import os
from typing import Union
import pandas as pd
from load_utils.get_dst_path import get_dst_path
from load_utils.filterlist_inc import filterlist_inc
from sniffbytes.stream2file import stream2file

''' Doesn't actually run the extraction job '''
def xtrct_archv(
    vals: pd.DataFrame,
    to_xtrct: Union[str, os.PathLike],
    dst_path: Union[str, os.PathLike]
) -> pd.DataFrame:
    return vals.loc[[row[0] for row in vals.iterrows()
                     if row[1].src_names not in
                     filter_lst_inc(to_xtrct, vals.src_names)]]

def main():
    if __name__ == __main__:
        xtrct_archv(vals, to_xtrct, dst_path)
