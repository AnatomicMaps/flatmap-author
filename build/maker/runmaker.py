#===============================================================================

import os
from pathlib import Path
import sys

from mapmaker.__main__ import main

#===============================================================================

FLATMAP_OUTPUT = os.environ.get('FLATMAP_ROOT', '/flatmaps')

#===============================================================================

if __name__ == '__main__':
    set_output = False
    for n, arg in enumerate(sys.argv):
        if arg == '--output':
            if n < (len(sys.argv) - 1):
                sys.argv[n+1] = FLATMAP_OUTPUT
            else:
                sys.argv.append(FLATMAP_OUTPUT)
            set_output = True
            break
    if not set_output:
        sys.argv.append('--output')
        sys.argv.append(FLATMAP_OUTPUT)
    main()

#===============================================================================
