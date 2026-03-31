#!/usr/bin/env python3
"""Gemini CLI tool.

Usage:
  python gemini.py /init
  python gemini.py /gemini
  python gemini.py /gemini summary
  python gemini.py /gemini help
"""

import sys


def init_command():
    output = [
        "/init called",
        "Project state: initialized.",
        "Implemented: dummy workspace init status."
    ]
    return "\n".join(output)


def gemini_summary():
    output = [
        "Gemini Summary:",
        "- repository: /workspaces/Gemini",
        "- files: README.md, gemini.py, tests/",
        "- status: scaffolded Gemini CLI with /init, /gemini summary, /gemini help"
    ]
    return "\n".join(output)


def gemini_help():
    output = [
        "Gemini CLI Help:",
        "  /init               Initialize workspace resources (idempotent).",
        "  /gemini             Show basic Gemini status.",
        "  /gemini summary     Print a repository summary.",
        "  /gemini help        Show this help message.",
        "Usage examples:",
        "  python gemini.py /init",
        "  python gemini.py /gemini summary"
    ]
    return "\n".join(output)


def main(args):
    if not args:
        print("No command provided. Use `/gemini help`.")
        return 1

    command = args[0]

    if command == "/init":
        print(init_command())
        return 0

    if command == "/gemini":
        if len(args) == 1:
            print("Gemini active. Use `/gemini help` for commands.")
            return 0

        sub = args[1]
        if sub == "summary":
            print(gemini_summary())
            return 0
        if sub == "help":
            print(gemini_help())
            return 0

        print(f"Unknown subcommand: {sub}. Use `/gemini help`.")
        return 2

    print(f"Unknown command: {command}. Use `/gemini help`.")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
