# file: console.py
"""
Minimal interactive Python console.

- Persistent state across commands
- Graceful exit handling
- Safe exception reporting
"""

import code
import sys


def start_console() -> None:
    banner = (
        "Code Copilot Python Console\n"
        f"Python {sys.version.split()[0]}\n"
        "Type exit() or Ctrl-D to quit.\n"
    )

    console = code.InteractiveConsole(locals={})
    console.interact(banner=banner)


if __name__ == "__main__":
    start_console()
