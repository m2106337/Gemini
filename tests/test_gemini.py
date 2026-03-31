import subprocess
import sys
import os


def run_cmd(args):
    root = os.path.dirname(__file__)
    script = os.path.join(root, "..", "gemini.py")
    proc = subprocess.run([sys.executable, script] + args, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def test_init():
    code, out, err = run_cmd(["/init"])
    assert code == 0
    assert "Project state: initialized" in out
    assert err == ""


def test_gemini_no_arg():
    code, out, err = run_cmd(["/gemini"])
    assert code == 0
    assert "Gemini active" in out


def test_gemini_summary():
    code, out, err = run_cmd(["/gemini", "summary"])
    assert code == 0
    assert "Gemini Summary" in out


def test_gemini_help():
    code, out, err = run_cmd(["/gemini", "help"])
    assert code == 0
    assert "Gemini CLI Help" in out
