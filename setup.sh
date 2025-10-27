#!/bin/bash
echo "Creating Python virtual environment..."
python3 -m venv pinyin_env

echo "Activating environment..."
source pinyin_env/bin/activate

echo "Installing pypinyin..."
pip install pypinyin

echo "Setup complete! Activate with: source pinyin_env/bin/activate"