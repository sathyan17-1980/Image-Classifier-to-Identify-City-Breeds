#!/usr/bin/env python3
import os
from collections import defaultdict
from pathlib import Path

# Define the base directory
base_dir = "/home/user/Image-Classifier-to-Identify-City-Breeds"

# Directories to check
directories = [
    "Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master",
    "Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master",
    "workspace"
]

# Dictionary to store files by their basename
files_by_name = defaultdict(list)

# Find all files (excluding .git directory)
for directory in directories:
    dir_path = os.path.join(base_dir, directory)
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            # Skip __pycache__ directories
            if '__pycache__' in root:
                continue
            for file in files:
                full_path = os.path.join(root, file)
                files_by_name[file].append(full_path)

# Find duplicates (files that exist in multiple locations)
duplicates = {name: paths for name, paths in files_by_name.items() if len(paths) > 1}

print(f"Found {len(duplicates)} duplicate filenames:\n")

# Sort duplicates by name
for name in sorted(duplicates.keys()):
    paths = duplicates[name]
    print(f"\n{name}:")
    for path in sorted(paths):
        # Show relative path
        rel_path = path.replace(base_dir + "/", "")
        print(f"  - {rel_path}")
