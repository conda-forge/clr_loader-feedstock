try:
    from importlib.resources import files as resources_files
except ImportError:
    from importlib_resources import files as resources_files
import json
import os
import sys
import tempfile

import clr_loader


# Check if DLLs exist
base_path = resources_files('clr_loader') / 'ffi' / 'dlls'
for arch in ['amd64', 'x86']:
    for ext in ['dll', 'pdb']:
        if not (base_path / arch / f'ClrLoader.{ext}').exists():
            raise FileNotFoundError(f'DLL ffi/dlls/{arch}/ClrLoader.{ext} not found in package.')

# Try to get different runtimes
if sys.platform == 'win32':
    clr_loader.get_netfx()
if sys.platform != 'win32':
    clr_loader.get_mono()
runtime_config = {
    'runtimeOptions': {
        'tfm': 'netcoreapp6.0',
        'framework': {
            'name': 'Microsoft.NETCore.App',
            'version': '6.0.0',
        },
    },
}
with tempfile.TemporaryDirectory() as tmpdir:
    runtime_config_file = os.path.join(tmpdir, 'runtime_config.json')
    with open(runtime_config_file, 'w') as file:
        file.write(json.dumps(runtime_config))
    clr_loader.get_coreclr(runtime_config_file)
