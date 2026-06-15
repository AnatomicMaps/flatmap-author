#===============================================================================

import logging
import os
from pathlib import Path
import subprocess
import sys

#===============================================================================

FLATMAP_SOURCE_DIR = os.environ.get('FLATMAP_SOURCE_DIR')
if FLATMAP_SOURCE_DIR is None:
    logging.error('FLATMAP_SOURCE_DIR is not set...')
    exit(1)
FLATMAP_SOURCE_DIR = Path(FLATMAP_SOURCE_DIR).resolve()

LOCAL_SOURCE_DIR = Path('/maker/sources/')

#===============================================================================

DOCKER_RUN_MAPMAKER = 'docker compose exec maker uv --quiet run python runmaker.py'.split()

#===============================================================================

if __name__ == '__main__':
    args = sys.argv[1:]
    for n, arg in enumerate(args):
        if arg == '--source':
            if n < (len(args) - 1):
                source_path = Path(args[n+1]).resolve()
                try:
                    local_path = LOCAL_SOURCE_DIR / source_path.relative_to(FLATMAP_SOURCE_DIR)
                except ValueError as e:
                    logging.error(e)
                    exit(1)
                args[n+1] = str(local_path)
                break
    subprocess.run(DOCKER_RUN_MAPMAKER + args)

#===============================================================================
