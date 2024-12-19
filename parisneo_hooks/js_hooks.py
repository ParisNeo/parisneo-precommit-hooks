import argparse
import subprocess
from typing import Sequence

def js_style_check(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    # Run prettier
    subprocess.run(['prettier', '--write', *args.filenames])
    
    # Run eslint
    result = subprocess.run(['eslint', '--fix', *args.filenames])
    
    return result.returncode
