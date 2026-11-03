#!/usr/bin/python
# Copyright: Jihyun Nam
# Version: 1.0

import sys
import argparse
from pathlib import Path

IGNORE_DIRS = {".git", "__pycache__", ".venv", "venv", "ENV", ".idea", ".vscode", "build", "dist"}


def _should_ignore(path: Path) -> bool:
    if path.name in IGNORE_DIRS or path.name.endswith(".egg-info"):
        return True
    return False


def print_tree(
    directory: Path,
    current_level: int = 0,
    dirs_only: bool = False,
    show_all: bool = False,
):
    """
    Recursively prints a directory tree structure.
    """
    # Print the current directory
    indent = " " * 4 * current_level
    display_name = directory.name or str(directory)
    print(f"{indent}{display_name}/")

    try:
        # Use iterdir for more efficient path processing
        for path in sorted(directory.iterdir()):
            if not show_all and _should_ignore(path):
                continue
            if path.is_dir():
                # Recurse into directories
                print_tree(path, current_level + 1, dirs_only, show_all)
            elif not dirs_only and path.is_file():
                # Print files if dirs_only is False
                sub_indent = " " * 4 * (current_level + 1)
                print(f"{sub_indent}{path.name}")
    except PermissionError:
        print(f"{' ' * 4 * (current_level + 1)}[Permission Denied]")


def main():
    parser = argparse.ArgumentParser(
        description="A professional directory tree view utility for OpenPipe."
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=".",
        help="Target directory path to display (default: current directory)",
    )
    parser.add_argument(
        "-d",
        "--dirs-only",
        action="store_true",
        help="Display directories only, hide files",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Show all files and directories, including hidden/cache directories",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="OpenPipe Treeview 1.0"
    )

    args = parser.parse_args()

    target_path = Path(args.path).resolve()

    if not target_path.exists():
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"Error: '{args.path}' is not a directory.")
        sys.exit(1)

    print_tree(target_path, dirs_only=args.dirs_only, show_all=args.all)
    return 0


if __name__ == "__main__":
    sys.exit(main())
