import subprocess
import sys

def run_pylint():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pylint", "original_code.py", "--exit-zero"],
            capture_output=True,
            text=True
        )
        print("=== PYLINT ANALYSIS ===")
        print(result.stdout)
    except Exception as e:
        print("Pylint not installed. Run: pip install pylint")
        print(e)

def run_flake8():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "flake8", "original_code.py"],
            capture_output=True,
            text=True
        )
        print("\n=== FLAKE8 ANALYSIS ===")
        print(result.stdout)
    except Exception as e:
        print("Flake8 not installed. Run: pip install flake8")
        print(e)

def run_bandit():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "bandit", "original_code.py", "-r"],
            capture_output=True,
            text=True
        )
        print("\n=== BANDIT SECURITY ANALYSIS ===")
        print(result.stdout)
    except Exception as e:
        print("Bandit not installed. Run: pip install bandit")
        print(e)

if __name__ == "__main__":
    run_pylint()
    run_flake8()
    run_bandit()