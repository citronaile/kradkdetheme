#!/usr/bin/env python3
import os

# Base directory for the krad plasma desktop theme
THEME_DIR = "/home/pierre/Documents/krad theme/plasma/desktoptheme/krad"
TARGET_FOLDERS = ["widgets", "dialogs", "opaque"]

# Dictionary mapping Orchis colors (Keys) -> Your krad colors (Values)
# Note: Hex codes are evaluated in lowercase to guarantee exact matching.
COLOR_MAP = {
    # 1. Background Swaps
    "#242932": "#1a1625",  # Base Orchis Dark grey panel background -> krad Window Background
    "#2d333f": "#221d30",  # Lighter Orchis element background -> krad Alternate Background
    "#1d212a": "#120e1a",  # Extra dark Orchis background -> krad View Background

    # 2. Accent/Highlight Swaps (Orchis signature blues/teals -> krad purples)
    "#0c7cd5": "#7a49d6",  # Primary Orchis Blue accent -> krad Normal Selection Accent
    "#3795e6": "#a880ff",  # Hover/Active Orchis Blue -> krad Active Text / Hover Accent
    "#0b66b1": "#5b31ab",  # Deep Orchis Blue -> krad Alternate Selection Background
}

def replace_colors_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    # Perform a case-insensitive replacement for each hex color pair
    for old_hex, new_hex in COLOR_MAP.items():
        # Match variations like #242932, #242932, or #242932
        content = content.replace(old_hex.lower(), new_hex.lower())
        content = content.replace(old_hex.upper(), new_hex.lower())

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[✓] Replaced hardcoded colors in: {os.path.basename(file_path)}")
        return True
    return False

def main():
    print("🎨 Starting automated hardcoded color replacement for 'krad' SVGs...")

    modified_count = 0
    total_svgs = 0

    for folder in TARGET_FOLDERS:
        target_path = os.path.join(THEME_DIR, folder)
        if not os.path.exists(target_path):
            continue

        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith('.svg'):
                    total_svgs += 1
                    full_path = os.path.join(root, file)
                    if replace_colors_in_file(full_path):
                        modified_count += 1

    print(f"\n✅ Done! Checked {total_svgs} SVG assets. Hardcoded colors updated in {modified_count} files.")

if __name__ == "__main__":
    main()
