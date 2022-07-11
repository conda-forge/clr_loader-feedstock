import json
import os
import sys
import tempfile

import clr_loader


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
