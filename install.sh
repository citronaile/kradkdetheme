#!/bin/bash

# Target local directory for KDE Plasma
SHARE_DIR="$HOME/.local/share"

echo "🎨 Installing com.citronaile.krad KDE Theme..."

# Create directories if they don't exist
mkdir -p "$SHARE_DIR/aurorae/themes"
mkdir -p "$SHARE_DIR/color-schemes"
mkdir -p "$SHARE_DIR/icons"
mkdir -p "$SHARE_DIR/plasma/desktoptheme"
mkdir -p "$SHARE_DIR/plasma/look-and-feel"

# Copy components to their respective system paths
cp -r aurorae/* "$SHARE_DIR/aurorae/themes/" 2>/dev/null
cp -r color-schemes/* "$SHARE_DIR/color-schemes/" 2>/dev/null
cp -r icons/* "$SHARE_DIR/icons/" 2>/dev/null
cp -r plasma/desktoptheme/* "$SHARE_DIR/plasma/desktoptheme/" 2>/dev/null
cp -r look-and-feel/* "$SHARE_DIR/plasma/look-and-feel/" 2>/dev/null

echo "✅ Done! Open System Settings > Colors & Themes > Global Themes to apply."
