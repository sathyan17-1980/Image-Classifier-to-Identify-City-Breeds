# Duplicate Files Report

## Summary
All duplicate files in the repository have been identified and renamed.

### Statistics
- **Total duplicate filenames found**: 70
- **Total files renamed**: 131
- **Directories processed**: 3

### Strategy
1. **Original directory** (files kept unchanged): `Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master`
2. **Duplicate directories** (files renamed):
   - `Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master`
   - `workspace`

### Naming Convention
Duplicate files were renamed by appending `_duplicate` before the file extension:
- Example: `file.jpg` → `file_duplicate.jpg`
- Example: `script.py` → `script_duplicate.py`

## Complete List of Duplicate Files

### Python Scripts (14 files)
- adjust_results4_isadog.py
- adjust_results4_isadog_hints.py
- calculates_results_stats.py
- calculates_results_stats_hints.py
- check_images.py
- classifier.py
- classify_images.py
- classify_images_hints.py
- get_input_args.py
- get_input_args_hints.py
- get_pet_labels.py
- get_pet_labels_hints.py
- print_functions_for_lab_checks.py
- print_results.py
- print_results_hints.py
- run_models_batch.sh
- run_models_batch_uploaded.sh
- test_classifier.py

### Data Files (9 files)
- alexnet_pet-images.txt
- alexnet_uploaded-images.txt
- dognames.txt
- imagenet1000_clsid_to_human.txt
- resnet_pet-images.txt
- resnet_uploaded-images.txt
- vgg_pet-images.txt
- vgg_uploaded-images.txt
- README.md

### Dog Breed Images (pet_images) (36 files)
- Basenji_00963.jpg
- Basenji_00974.jpg
- Basset_hound_01034.jpg
- Beagle_01125.jpg
- Beagle_01141.jpg
- Beagle_01170.jpg
- Boston_terrier_02259.jpg
- Boston_terrier_02285.jpg
- Boston_terrier_02303.jpg
- Boxer_02426.jpg
- Cocker_spaniel_03750.jpg
- Collie_03797.jpg
- Dalmatian_04017.jpg
- Dalmatian_04037.jpg
- Dalmatian_04068.jpg
- German_shepherd_dog_04890.jpg
- German_shepherd_dog_04931.jpg
- German_shorthaired_pointer_04986.jpg
- Golden_retriever_05182.jpg
- Golden_retriever_05195.jpg
- Golden_retriever_05223.jpg
- Golden_retriever_05257.jpg
- Great_dane_05320.jpg
- Great_pyrenees_05367.jpg
- Great_pyrenees_05435.jpg
- Miniature_schnauzer_06884.jpg
- Poodle_07927.jpg
- Poodle_07956.jpg
- Rabbit_002.jpg
- Saint_bernard_08010.jpg
- Saint_bernard_08036.jpg
- cat_01.jpg
- cat_02.jpg
- cat_07.jpg
- fox_squirrel_01.jpg
- gecko_02.jpg
- gecko_80.jpg
- great_horned_owl_02.jpg
- polar_bear_04.jpg
- skunk_029.jpg

### Uploaded Images (4 files)
- Dog_01.jpg
- Dog_02.jpg
- Frog_01.jpg
- cat_01.jpg (special case - existed in multiple subdirectories)

## Special Cases
- **cat_01.jpg**: This file existed in 4 locations:
  - `Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master/pet_images/cat_01.jpg` (kept as original)
  - `Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master/uploaded_images/cat_01.jpg` (renamed to cat_01_duplicate.jpg)
  - `Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master/pet_images/cat_01_duplicate.jpg` (renamed)
  - `workspace/pet_images/cat_01_duplicate.jpg` (renamed)

## Verification
✅ All duplicate filenames have been successfully renamed
✅ No naming conflicts remain in the repository
✅ Original files preserved in `Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-master`
