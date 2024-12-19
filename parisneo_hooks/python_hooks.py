import argparse
import subprocess
from typing import Sequence

def python_style_check(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    # Run black
    subprocess.run(['black', *args.filenames])
    
    # Run isort
    subprocess.run(['isort', *args.filenames])
    
    # Run flake8
    result = subprocess.run(['flake8', *args.filenames])
    
    return result.returncode
