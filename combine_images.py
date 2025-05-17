import os
import shutil
import sys

# --- Configuration ---
SOURCE_DIRS = ["sandbox/train_sample", "indofashionsandbox/train_sand"]
TARGET_DIR = "combined_images"
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")  # Define valid extensions
# --- End Configuration ---


def count_images(directory):
    """Counts the number of image files (jpg, jpeg, png) in a directory."""
    count = 0
    if not os.path.isdir(directory):
        return 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(VALID_EXTENSIONS):
            count += 1
    return count


def combine_images(source_dirs, target_dir):
    """Copies image files (jpg, jpeg, png) from source directories to a target directory."""

    if not os.path.exists(target_dir):
        print(f"Creating target directory: {target_dir}")
        os.makedirs(target_dir)
    else:
        print(f"Target directory already exists: {target_dir}")

    copied_count = 0
    skipped_count = 0
    error_count = 0

    for source_dir in source_dirs:
        if not os.path.isdir(source_dir):
            print(
                f"Warning: Source directory not found: {source_dir}. Skipping.")
            continue

        print(f"Processing source directory: {source_dir}")
        for filename in os.listdir(source_dir):
            if filename.lower().endswith(VALID_EXTENSIONS):
                source_path = os.path.join(source_dir, filename)
                target_path = os.path.join(target_dir, filename)

                try:
                    if not os.path.exists(target_path):
                        # copy2 preserves metadata
                        shutil.copy2(source_path, target_path)
                        copied_count += 1
                    else:
                        skipped_count += 1
                except Exception as e:
                    print(f"Error copying {filename} from {source_dir}: {e}")
                    error_count += 1

    print("\n--- Summary ---")
    print(f"Target Directory: {os.path.abspath(target_dir)}")
    print(f"Images Copied: {copied_count}")
    print(f"Images Skipped (already exist): {skipped_count}")
    print(f"Errors: {error_count}")
    if error_count > 0:
        print("Please check the error messages above.")
    print("---------------")


if __name__ == "__main__":
    # Basic check if source dirs exist before starting
    sources_ok = True
    print("--- Source Directory Counts ---")
    total_source_images = 0
    for src in SOURCE_DIRS:
        if not os.path.isdir(src):
            print(
                f"Error: Source directory '{src}' not found.", file=sys.stderr)
            sources_ok = False
        else:
            img_count = count_images(src)
            print(f"- '{src}': {img_count} image files {VALID_EXTENSIONS}")
            total_source_images += img_count
    print(f"Total images in source directories: {total_source_images}")
    print("-----------------------------")

    if not sources_ok:
        print("Aborting due to missing source directories.", file=sys.stderr)
        sys.exit(1)

    combine_images(SOURCE_DIRS, TARGET_DIR)
    print("Image combination process finished.")
