#!usr/bin/env/python3

# ''' Could be made independant from pandas '''

# import os
# from typing import Union
# import pandas as pd
# from loadutils.get_dst_path import get_dst_path
# from loadutils.filterlist_inc import filterlist_inc
# from sniffbytes.stream2file import stream2file

# def save_archv(
#     vals: pd.DataFrame,
#     to_xtrct: Union[str, list, tuple],
#     dst_path: Union[str, os.PathLike]
# ) -> None:
#     """ Writes unzipped file buffers to disk. """
#     [stream2file(row[1].bsheets,
#                  os.path.join(get_dst_path(dst_path),
#                        os.path.basename(row[1].filename).lower()))
#      for row in vals.iterrows() if row[1].src_names in
#      tqdm(filter_lst_inc(to_xtrct, vals.src_names),
#           "extracting archive")]

# def main():
#     if __name__ == __main__:
#         save_archv(vals, to_xtrct, dst_path)
