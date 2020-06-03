# re module
import re

# accesses pertinent files
cleanNames = open(r"CleanNames.csv", "w+")
invalidNames = open(r"InvalidNames.csv", "w+")
dirtyNames = open(r"DirtyNames.csv", "r")

# converts dirtyNames csv to a list
dirtyNames = re.split(r",", dirtyNames.read())

# sorts and formats each name in dirtyNames list
for name in dirtyNames:

    # invalid name
    if not re.search(r"[^a-zA-Z-]", name) == None:

        # writes name to InvalidNames.csv
        invalidNames.write(name + "\n")

    # valid name with a hyphen
    elif "-" in name:

        # splits the name into parts around the hyphen
        name = re.split(r"-", name)

        # formats each part around the hyphen
        for part in name:
            # determines the index of the part in the name list
            index = name.index(part)

            # all characters are set to lowercase
            part = part.lower()

            # first letter is capitalized
            part = part.capitalize()

            # replaces unformatted part with formatted part
            name.remove(name[index])
            name.insert(index, part)

        # parts are joined into a string with a hyphen as the separator
        name = "-".join(name)

        # writes name to CleanNames.csv
        cleanNames.write(name + "\n")

    # valid name without a hyphen
    else:

        # all characters are set to lowercase
        name = name.lower()

        # first letter is capitalized
        name = name.capitalize()

        # writes name to CleanNames.csv
        cleanNames.write(name + "\n")
