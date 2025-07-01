import subprocess
import sys

def install(package):
    try:
        __import__(package)
        print(f"✅ Already installed: {package}")
    except ImportError:
        print(f"📦 Installing: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    print("🩷 Let’s get you set up, babe~\n")
    install("pyperclip")
    print("\n✨ All done, sweetie! You're ready to run the main script 💖")
    input("\n⏳ Press Enter to close this little magic window 💋")
