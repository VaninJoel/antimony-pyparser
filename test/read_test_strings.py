# Simple script for pulling out test strings from antimony test-data directory

import glob
import os


directory = r"D:\antimony\src\test\test-data"
additional_folders = ["constraints", "distributions", "fbc", "from-libsbml"]

files = glob.glob(os.path.join(directory, "*.txt"))

for f in additional_folders:
    folder = os.path.join(directory, f)
    assert os.path.isdir(folder)
    files += glob.glob(os.path.join(folder, "*.txt"))

# order by filesize
sizes = [os.path.getsize(f) for f in files]
files_and_sizes = dict(zip(files, sizes))
ordered_files = sorted(files_and_sizes, key=files_and_sizes.get)
# print(ordered_files)

s = ''
for filepath in ordered_files:
    filename = os.path.split(filepath)[1]
    variable_name = os.path.splitext(filename)[0]
    print(variable_name)
    with open(filepath) as f:
        test_data = f.read()

    s += f"# Original source: <antimony-root>/src/test/test-data/{variable_name}.txt\n"
    s += f"{variable_name} = \'\'\'{test_data}\'\'\'\n\n"
print(s)







