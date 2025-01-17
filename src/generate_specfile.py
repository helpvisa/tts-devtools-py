"""
tools for automatically generating a specfile from a given folder of scripts
"""

import os
import json


def generate_specfile_from_folder(folder, specfile_path):
    """
    given a folder, parse every script within and generate a specfile from the
    names of the scripts in the folder. intended to be used with the
    automatically-generated names when using 'get_lua_scripts' either from
    a terminal or the gui.

    name format is:
    guid-object_name.[lua/xml]
    ^    ^
    |    |
    |    name saved in specfile
    guid saved in specfile

    the single '-' splits these two, and the file extension determines if it is
    stored in the 'script' (lua) or 'ui' (xml) key.

    this function is ignorant of subdirectories.
    """
    entries = []
    try:
        # gather files in given directory
        for name in os.listdir(folder):
            # get absolute path
            abs_path = os.path.abspath(folder)
            # open file
            parse_filename = name.split("-")
            obj_guid = -1
            # this may be global, in which case guid is not in filename
            if len(parse_filename) > 1:
                obj_guid = parse_filename[0]
                obj_name = parse_filename[1]
            else:
                obj_name = parse_filename[0]
            split_extension = obj_name.split(".")
            obj_name = split_extension[0]  # strip extension
            # we use length of list because some filenames (like vim swapfiles)
            # may have multiple extensions
            type = split_extension[len(split_extension) - 1]
            obj_name = obj_name.replace("_", " ")
            # does an entry already exist for this item?
            entry_does_not_exist = True
            for entry in entries:
                if obj_guid == entry["guid"]:  # we already made an entry
                    entry_does_not_exist = False
                    if type == "lua":
                        entry["script"] = os.path.join(abs_path, name)
                    else:
                        entry["ui"] = os.path.join(abs_path, name)
                    break
            # create a new dict entry
            if entry_does_not_exist:
                new_entry = {
                    "name": obj_name,
                    "guid": obj_guid
                }
                if type == "lua":
                    new_entry["script"] = os.path.join(abs_path, name)
                else:
                    new_entry["ui"] = os.path.join(abs_path, name)
                entries.append(new_entry)
        # parse and save objects to disk
        new_specfile = json.dumps(entries)
        with open(specfile_path, mode="w", encoding="utf-8") as spec:
            spec.write(new_specfile)
    except OSError as err:
        print("Error accessing file: ", err)
