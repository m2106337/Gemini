#!/usr/bin/env python3
"""Gemini CLI 工具（已中文化）

支援：
  - CLI（保持英文相容）
  - 簡易 GUI（使用 tkinter）: `python gemini.py --gui` 或 `-g`

示例：
  python gemini.py /init
  python gemini.py /gemini summary
  python gemini.py --gui
"""

import sys
import os

try:
    import tkinter as tk
    from tkinter.scrolledtext import ScrolledText
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False


def init_command():
    output = [
        "/init called",
        "Project state: initialized.",
        "專案狀態：已初始化（示範訊息）。"
    ]
    return "\n".join(output)


def gemini_summary():
    repo = os.path.abspath(os.path.dirname(__file__))
    files = [f for f in os.listdir(repo) if not f.startswith('.')]
    output = [
        "Gemini Summary:",
        f"- repository: {repo}",
        f"- files: {', '.join(files)}",
        "- status: scaffolded Gemini CLI with /init, /gemini summary, /gemini help",
        "簡短中文摘要：此為示範專案，包含 CLI 與可重用的 GitHub Action。"
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
        "  python gemini.py /gemini summary",
        "說明（中文）：",
        "  /init               初始化專案資源（可重複執行且不會重覆建立）。",
        "  /gemini             顯示 Gemini 狀態。",
        "  /gemini summary     列印專案摘要。",
        "  /gemini help        顯示此說明。"
    ]
    return "\n".join(output)


def run_cli(args):
    if not args:
        print("沒有提供指令。請使用 `/gemini help` 或 `--gui`。")
        return 1

    # GUI flags handled elsewhere
    if args[0] in ("--gui", "-g"):
        if not TK_AVAILABLE:
            print("tkinter 不可用，無法啟動 GUI。")
            return 2
        launch_gui()
        return 0

    command = args[0]

    if command == "/init":
        print(init_command())
        return 0

    if command == "/gemini":
        if len(args) == 1:
            print("Gemini active. Use `/gemini help` for commands.（中文：Gemini 已啟用，使用 `/gemini help` 查看指令。）")
            return 0

        sub = args[1]
        if sub == "summary":
            print(gemini_summary())
            return 0
        if sub == "help":
            print(gemini_help())
            return 0

        print(f"Unknown subcommand: {sub}. Use `/gemini help`.（未知子指令：{sub}）")
        return 2

    print(f"Unknown command: {command}. Use `/gemini help`.（未知指令：{command}）")
    return 2


def launch_gui():
    root = tk.Tk()
    root.title('Gemini 工具')
    root.geometry('640x360')

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    btn_frame = tk.Frame(frame)
    btn_frame.pack(fill=tk.X)

    text = ScrolledText(frame, wrap=tk.WORD, height=15)
    text.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

    def show(text_str):
        text.delete('1.0', tk.END)
        text.insert(tk.END, text_str)

    def on_init():
        show(init_command())

    def on_summary():
        show(gemini_summary())

    def on_help():
        show(gemini_help())

    btn_init = tk.Button(btn_frame, text='初始化', command=on_init)
    btn_init.pack(side=tk.LEFT, padx=4)

    btn_summary = tk.Button(btn_frame, text='摘要', command=on_summary)
    btn_summary.pack(side=tk.LEFT, padx=4)

    btn_help = tk.Button(btn_frame, text='說明', command=on_help)
    btn_help.pack(side=tk.LEFT, padx=4)

    lbl = tk.Label(btn_frame, text='— Gemini GUI（中文） —')
    lbl.pack(side=tk.RIGHT)

    root.mainloop()


def main(args):
    return run_cli(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
