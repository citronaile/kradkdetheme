#!/usr/bin/env python3
import os
import re

# Paths to your krad theme asset directories
THEME_DIR = "/home/pierre/Documents/krad theme/plasma/desktoptheme/krad"
TARGET_FOLDERS = ["widgets", "dialogs"]

# The system color stylesheet template required by the KDE Plasma engine
SYSTEM_CSS_BLOCK = """  <style id="current-color-scheme" type="text/css">
    .color-scheme-window-background { color: #1a1625; }
    .color-scheme-window-text { color: #e4dff2; }
    .color-scheme-view-background { color: #120e1a; }
    .color-scheme-view-text { color: #e4dff2; }
    .color-scheme-button-background { color: #221d30; }
    .color-scheme-button-text { color: #e4dff2; }
    .color-scheme-selection-background { color: #7a49d6; }
    .color-scheme-selection-text { color: #ffffff; }
    .color-scheme-selection-hover-background { color: #a880ff; }
    .color-scheme-active-text { color: #a880ff; }
    .color-scheme-link-text { color: #ff9f1c; }
  </style>"""

def inject_system_hints(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if a stylesheet definition already exists to avoid duplication
    if 'id="current-color-scheme"' in content:
        print(f"[-] System hints already present in: {os.path.basename(file_path)}")
        return

    # Find the main opening <svg> tag to inject the style block right after it
    svg_tag_match = re.search(r'(<svg[^>]*>)', content)
    if svg_tag_match:
        tag = svg_tag_match.group(1)
        # Inject style block immediately beneath the opening tag
        updated_content = content.replace(tag, f"{tag}\n{SYSTEM_CSS_BLOCK}")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"[+] Successfully injected system palette hints into: {os.path.basename(file_path)}")
    else:
        print(f"[!] Warning: Could not find valid <svg> tag inside: {os.path.basename(file_path)}")

def main():
    print("🚀 Starting automated system palette hint configuration for 'krad' theme...")

    count = 0
    for folder in TARGET_FOLDERS:
        target_path = os.path.join(THEME_DIR, folder)
        if not os.path.exists(target_path):
            print(f"[!] Target directory not found: {target_path}, skipping.")
            continue

        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith('.svg'):
                    full_path = os.path.join(root, file)
                    inject_system_hints(full_path)
                    count += 1

    print(f"\n✅ Done! Processed {count} SVG assets. The layout engine will now map color classes to your krad palette.")

if __name__ == "__main__":
    main()
