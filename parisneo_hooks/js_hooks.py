import argparse
import subprocess
import shutil
from typing import Sequence


def check_node_dependencies():
    if not (shutil.which('eslint') and shutil.which('prettier')):
        raise RuntimeError(
            "eslint and/or prettier not found. Please install them globally using:"
            "\nnpm install -g eslint prettier"
        )


def js_style_check(argv: Sequence[str] | None = None) -> int:
    try:
        check_node_dependencies()
    except RuntimeError as e:
        print(str(e))
        return 1

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    if not args.filenames:
        return 0

    # Run prettier
    try:
        subprocess.run(['prettier', '--write', *args.filenames], check=True)
    except subprocess.CalledProcessError:
        return 1
    
    # Run eslint
    try:
        subprocess.run(['eslint', '--fix', *args.filenames], check=True)
    except subprocess.CalledProcessError:
        return 1
    
    return 0
