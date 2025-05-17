import os
import random
import shutil
import pandas as pd
from pathlib import Path

train_sample_size = 1500
test_sample_size = 350

train_dir = Path("train")
test_dir = Path("test")
annotations_csv = Path("train.csv")
label_descriptions_file = Path("label_descriptions.json")

sandbox_dir = Path("sandbox")
sandbox_train_dir = sandbox_dir / "train_sample"
sandbox_test_dir = sandbox_dir / "test_sample"
filtered_annotations_file = sandbox_dir / "train_sample_annotations.csv"


sandbox_train_dir.mkdir(parents=True, exist_ok=True)
sandbox_test_dir.mkdir(parents=True, exist_ok=True)
sandbox_dir.mkdir(parents=True, exist_ok=True)


annotations_df = pd.read_csv(annotations_csv)
annotated_ids = set(annotations_df['ImageId'].str.strip().str.lower())
print(f"Total unique annotated ImageIds in CSV: {len(annotated_ids)}")

train_images = list(train_dir.glob("*"))
annotated_train_images = [img for img in train_images if img.stem.strip().lower() in annotated_ids]
print(f"Total training images with annotations: {len(annotated_train_images)}")


if len(annotated_train_images) < train_sample_size:
    print("Warning: Fewer annotated training images available than desired sample size.")
    sample_train_images = annotated_train_images
else:
    sample_train_images = random.sample(annotated_train_images, train_sample_size)
print(f"Sampled {len(sample_train_images)} training images with annotations.")


for img in sample_train_images:
    shutil.copy2(img, sandbox_train_dir / img.name)


test_images = list(test_dir.glob("*"))
if len(test_images) < test_sample_size:
    print("Warning: Fewer test images available than desired sample size.")
    sample_test_images = test_images
else:
    sample_test_images = random.sample(test_images, test_sample_size)
print(f"Sampled {len(sample_test_images)} test images.")


for img in sample_test_images:
    shutil.copy2(img, sandbox_test_dir / img.name)

sampled_train_ids = {img.stem.strip().lower() for img in sample_train_images}
filtered_annotations_df = annotations_df[
    annotations_df['ImageId'].str.strip().str.lower().isin(sampled_train_ids)
]
print(f"Number of annotation rows for sampled training images: {len(filtered_annotations_df)}")

filtered_annotations_df.to_csv(filtered_annotations_file, index=False)
print(f"Filtered annotations saved to {filtered_annotations_file}")

shutil.copy2(label_descriptions_file, sandbox_dir / label_descriptions_file.name)
print(f"Label descriptions file copied to {sandbox_dir / label_descriptions_file.name}")

print("Sandbox setup complete!")
