import sys

def main():
    if len(sys.argv) < 2:
        print("Gemini active")
        return 0
    
    cmd = sys.argv[1]
    
    if cmd == "/init":
        print("Project state: initialized")
        return 0
    elif cmd == "/gemini":
        if len(sys.argv) > 2:
            subcommand = sys.argv[2]
            if subcommand == "summary":
                print("Gemini Summary")
                return 0
            elif subcommand == "help":
                print("Gemini CLI Help")
                return 0
        print("Gemini active")
        return 0
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
