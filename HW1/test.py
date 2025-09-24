# Verify that PLINK files exist at the specified location

import os

# Your data path
data_prefix = r"/home/vcm/BIOSTATS915_HighDimensionalStatisticsAndMachineLearning/HW1/hw-optionB-files/ADAPTmap_genotypeTOP_20160222_full"

print("=== VERIFYING FILE EXISTENCE ===")
print(f"Base path: {data_prefix}")

# Check each file individually
files_to_check = ['.bed', '.bim', '.fam']
file_status = {}

for ext in files_to_check:
    file_path = data_prefix + ext
    exists = os.path.exists(file_path)
    file_status[ext] = exists
    
    print(f"{ext} file: {file_path}")
    print(f"  Exists: {'✓ YES' if exists else '✗ NO'}")
    
    if exists:
        # Get file size
        size = os.path.getsize(file_path)
        print(f"  Size: {size:,} bytes ({size/1024/1024:.1f} MB)")
    print()

# Check directory
directory = os.path.dirname(data_prefix)
print(f"Directory: {directory}")
print(f"Directory exists: {'✓ YES' if os.path.exists(directory) else '✗ NO'}")

if os.path.exists(directory):
    print("\nFiles in directory:")
    try:
        files_in_dir = os.listdir(directory)
        for f in sorted(files_in_dir):
            if "ADAPTmap" in f or f.endswith(('.bed', '.bim', '.fam')):
                file_path = os.path.join(directory, f)
                size = os.path.getsize(file_path) if os.path.isfile(file_path) else 0
                print(f"  {f} ({size:,} bytes)")
    except PermissionError:
        print("  [Permission denied]")

# Summary
print("\n=== SUMMARY ===")
all_exist = all(file_status.values())
print(f"All required files present: {'✓ YES' if all_exist else '✗ NO'}")

if not all_exist:
    missing = [ext for ext, exists in file_status.items() if not exists]
    print(f"Missing files: {', '.join(missing)}")
    
    print("\nTroubleshooting suggestions:")
    print("1. Check if files have different names or extensions")
    print("2. Verify you have read permissions")
    print("3. Look for files with similar names in the directory")
    
    # Try to find similar files
    if os.path.exists(directory):
        print("\nLooking for similar files...")
        all_files = os.listdir(directory)
        for f in all_files:
            if "ADAPTmap" in f.lower() or "genotype" in f.lower():
                print(f"  Found: {f}")

# Test loading if all files exist
if all_exist:
    print("\n=== ATTEMPTING TO LOAD DATA ===")
    try:
        from pandas_plink import read_plink1_bin
        goat_data = read_plink1_bin(data_prefix+'.bed', verbose=False)
        print("✓ SUCCESS: Data loaded successfully!")
        print(f"Data type: {type(goat_data)}")
        print(f"Number of individuals: {goat_data.sample.shape[0]}")
        print(f"Number of SNPs: {goat_data.variant.shape[0]}")
    except Exception as e:
        print(f"✗ FAILED to load data: {e}")
        print("Even though files exist, there may be a format issue.")
else:
    print("\nCannot attempt to load data - missing files.")