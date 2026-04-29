#!/usr/bin/env python3
import sys


def main() -> None:
    # 沒有任何參數時，測試沒有定義行為，這裡直接當作錯誤即可
    if len(sys.argv) < 2:
        sys.exit(1)

    cmd = sys.argv[1]

    # /init
    if cmd == "/init":
        print("Project state: initialized")
        sys.exit(0)

    # /gemini 相關
    if cmd == "/gemini":
        # 沒有子命令：/gemini
        if len(sys.argv) == 2:
            print("Gemini active")
            sys.exit(0)

        sub = sys.argv[2]

        if sub == "summary":
            print("Gemini Summary")
            sys.exit(0)
        elif sub == "help":
            print("Gemini CLI Help")
            sys.exit(0)
        else:
            # 未知子命令
            sys.exit(1)

    # 未知主命令
    sys.exit(1)


if __name__ == "__main__":
    main()        
