from __future__ import division, print_function, absolute_import

import argparse
import sys
import os
from folder_disguise.guid_list import GUIDList

__author__ = "Ali Masri"
__copyright__ = "Ali Masri"
__license__ = "MIT"


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="A folder disguise tool")
    parser.add_argument(
        '-f',
        dest="folder",
        help="the folder to be disguised/restore",
    )
    parser.add_argument(
        '-m',
        dest='mode',
        help="set the mode disguise/restore",
    )
    parser.add_argument(
        '-d',
        dest='disguise',
        help='the disguise number',
        nargs='?'
    )
    return parser.parse_args(args)


def main(folder, mode, disguise_num):
    if not os.path.isdir(folder):
        print('Directory not found')
        return
    if mode is None or mode not in ['d', 'r']:
        print('Must specify mode (d for disguise, r for restore)')
        return
    guids_list = GUIDList.read_guids()
    if mode == "d":
        if disguise_num is None:
            GUIDList.print_options(guids_list)
            while True:
                try:
                    disguise_num = int(input('Select a disguise number: ').strip())
                    if disguise_num < 0 or disguise_num >= len(guids_list):
                        raise Exception
                    break
                except Exception:
                    print('Incorrect number!')
                    pass
        os.rename(folder, folder + "." + guids_list[disguise_num][1])
        print('Folder disguised!')
    elif mode == "r":
        new_name = os.path.splitext(folder)[0]
        os.rename(folder, new_name)
        print('Folder restored!')


def run():
    args = parse_args(sys.argv[1:])
    mode = args.mode
    folder = args.folder
    disguise_num = args.disguise
    main(folder, mode, disguise_num)


if __name__ == "__main__":
    run()
