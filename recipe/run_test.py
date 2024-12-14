import sys
from importlib.resources import files

import clr_loader


# Check if DLLs exist
base_path = files('clr_loader') / 'ffi' / 'dlls'
for arch in ['amd64', 'x86']:
    for ext in ['dll', 'pdb']:
        if not (base_path / arch / f'ClrLoader.{ext}').exists():
            raise FileNotFoundError(f'DLL ffi/dlls/{arch}/ClrLoader.{ext} not found in package.')

# Try to get different runtimes
if sys.platform == 'win32':
    clr_loader.get_netfx()
if sys.platform != 'win32':
    clr_loader.get_mono()
clr_loader.get_coreclr()
