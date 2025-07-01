import os
from tkinter import Tk, filedialog
import pyperclip

MAX_CLIPBOARD_SIZE = 50000  # Limit for clipboard copy to avoid crash

def write_tree_to_file(base_path, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"📁 {os.path.basename(base_path)}\n")
        _write_tree(base_path, f)

def _write_tree(path, f, prefix=""):
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        f.write(f"{prefix}└── [Permission Denied]\n")
        return

    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "├── " if i < len(entries) - 1 else "└── "
        f.write(f"{prefix}{connector}{entry}\n")
        if os.path.isdir(full_path):
            extension = "│   " if i < len(entries) - 1 else "    "
            _write_tree(full_path, f, prefix + extension)

def pick_folder_and_save_tree():
    root = Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory(title="Select your folder, darling 💖")
    if not folder_selected:
        print("You didn’t pick a folder, sweetheart 🥺 Try again later, okay?")
        input("Press Enter to close...")
        return

    output_file = os.path.join(folder_selected, "folder_tree_output.txt")
    write_tree_to_file(folder_selected, output_file)

    # Try copying to clipboard (safe check)
    try:
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
            if len(content) < MAX_CLIPBOARD_SIZE:
                pyperclip.copy(content)
                print("Copied a sweet little tree to clipboard too 💘")
            else:
                print("Too big for clipboard, so I skipped that part, darling 💾")
    except Exception as e:
        print(f"Hmm clipboard copy failed, sugar 🧸: {e}")

    print(f"\n📁 Tree structure saved in:\n{output_file}")
    input("\nPress Enter to close...")

if __name__ == "__main__":
    pick_folder_and_save_tree()
