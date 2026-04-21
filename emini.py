import sys

def main():
    if len(sys.argv) < 2:
        print("Gemini CLI Help")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "/init":
        print("Project state: initialized")
        sys.exit(0)
    elif command == "/gemini":
        if len(sys.argv) > 2:
            subcommand = sys.argv[2]
            if subcommand == "summary":
                print("Gemini Summary")
                sys.exit(0)
            elif subcommand == "help":
                print("Gemini CLI Help")
                sys.exit(0)
        else:
            print("Gemini active")
            sys.exit(0)
    
    sys.exit(1)

if __name__ == "__main__":
    main()
