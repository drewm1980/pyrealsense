import ctypes
import sys
import os
from pathlib import Path

if sys.platform in ('linux','linux2'):
    soname = 'librealsense.so'
    search_paths = [
        '.', '/usr/local/lib', '/usr/local/lib/x86_64-linux-gnu', '/usr/lib'
    ]
elif sys.platform == 'darwin':
    soname = 'librealsense.dylib'
else:
    assert False, 'Please add library search paths for your platform to importlib.py'

file_path = None
for path in search_paths:
    if (Path(path) / soname).is_file():
        file_path = Path(path) / soname
        break
assert file_path is not None, "Could not find the library file " + soname + 'in any of the directories '+str(search_paths)

## import C lib
lrs = rsutilwrapper = ctypes.CDLL(str(file_path))
