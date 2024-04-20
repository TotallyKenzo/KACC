"""idk pylink wants me to add a module docstring"""
import os
import sys
import time
import json

from tqdm import tqdm
from srctools import bsp

jsonFolder = os.path.join(os.getcwd(), 'Assets')
jsonassets = []


def init():
    """Searches asset folder for asset configs, and adds the file path to a list."""
    print("Searching for json files...")
    jsonlist = os.listdir(jsonFolder)
    pbar = tqdm(range(len(jsonlist)))
    for i in pbar:
        pbar.set_description(f"Indexing {jsonlist[i]}")
        time.sleep(.1)
        if '.json' in jsonlist[i]:
            jsonassets.append(os.path.join(jsonFolder, jsonlist[i]))
    time.sleep(.5)
    print(f"Found and indexed {len(jsonassets)} json files.")
    time.sleep(.2)
    print("Completed.")
    time.sleep(2)
    clear()
    start()


def start():
    """Starting UI to select a mode."""
    print(
        """Welcome to Kenzo's Awesome Credits Checker!
Select a mode:
[A] Add a new asset
[F] Find an asset in a map
[Q] Quit"""
    )
    mode = input()
    if mode in ["a", "f", "q"]:
        if mode == "a":
            pass
            # add()
            # TODO: Implement add function
        elif mode == "f":
            find()
        elif mode == "q":
            sys.exit()
    else:
        clear()
        start()


# def add():
# TODO: Implement add function

def find():
    """Searches for assets in a map."""
    mappath = input("Enter the name of the map: ")
    mapf = bsp.BSP(f"D:/Steam/steamapps/common/Portal 2/portal2/maps/{mappath}.bsp")
    paklist = mapf.pakfile.namelist()
    foundassets = search(paklist)
    print(f"Found {len(foundassets)} assets")
    # TODO: Add credits generator and declarer.


def search(paklist):
    """Searches for assets in asset configs and checks if they are in the map."""
    foundassets = []
    print("Searching for assets...")
    pbar = tqdm(range(len(jsonassets)))
    for i in pbar:
        pbar.set_description(f"Searching {jsonassets[i]}")
        with open(jsonassets[i], 'r', encoding="json") as f:
            json_obj = json.load(f)
            asset_paths = json_obj['assetPaths']
            for path in asset_paths:
                if path in paklist:
                    print(foundassets)
                    # TODO: Figure out how to check if the asset is already in the list
                    # FIXME: first item in jsonassets[i] not being appended to foundassets
                    if path not in foundassets:
                        print(f"Found {path}")
                        foundassets.append(jsonassets[i])
    return foundassets


def clear():
    """Natively clears the console."""
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    elif os.name == "java":
        os.system("clear")


init()
