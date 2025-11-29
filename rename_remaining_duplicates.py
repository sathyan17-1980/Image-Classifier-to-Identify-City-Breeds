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

# Directory to keep as original (exact match)
original_dir_path = os.path.join(base_dir, "Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master")

# Dictionary to store files by their basename
files_by_name = defaultdict(list)

# Find all files (excluding .git directory and __pycache__)
for directory in directories:
    dir_path = os.path.join(base_dir, directory)
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            # Skip __pycache__ directories
            if '__pycache__' in root:
                continue
            for file in files:
                # Skip files we created
                if file in ['find_duplicates.py', 'rename_duplicates.py', 'rename_remaining_duplicates.py']:
                    continue
                full_path = os.path.join(root, file)
                files_by_name[file].append(full_path)

# Find duplicates (files that exist in multiple locations)
duplicates = {name: paths for name, paths in files_by_name.items() if len(paths) > 1}

print(f"Found {len(duplicates)} duplicate filenames\n")

# Track renames
renames = []

# Process each duplicate
for name, paths in sorted(duplicates.items()):
    # Skip files already renamed
    if '_duplicate' in name:
        continue

    # Separate the filename and extension
    name_parts = name.rsplit('.', 1)
    if len(name_parts) == 2:
        base_name, extension = name_parts
        new_name = f"{base_name}_duplicate.{extension}"
    else:
        # No extension
        new_name = f"{name}_duplicate"

    for path in paths:
        # Use exact path comparison to identify original directory
        # Check if path starts with the original directory path
        rel_path = os.path.relpath(path, base_dir)
        if rel_path.startswith("Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master/"):
            continue

        # Rename files in other directories
        new_path = os.path.join(os.path.dirname(path), new_name)
        renames.append((path, new_path))

print(f"Will rename {len(renames)} files:\n")
for old_path, new_path in renames[:10]:  # Show first 10
    rel_old = old_path.replace(base_dir + "/", "")
    rel_new = new_path.replace(base_dir + "/", "")
    print(f"  {rel_old}")
    print(f"    -> {rel_new}")

if len(renames) > 10:
    print(f"\n  ... and {len(renames) - 10} more files")

print("\nProceeding with renames...")
renamed_count = 0
for old_path, new_path in renames:
    try:
        os.rename(old_path, new_path)
        renamed_count += 1
    except Exception as e:
        print(f"Error renaming {old_path}: {e}")

print(f"\n✓ Successfully renamed {renamed_count} duplicate files!")
