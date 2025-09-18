import pandas as pd
import os, shutil

# Load metadata
df = pd.read_csv("data/chexchonet/metadata.csv")


# Chỉ lấy những ảnh có nhãn rõ ràng
df = df[(df['slvh'].isin([0,1])) & (df['dlv'].isin([0,1]))]

# Lấy 1000 ảnh ngẫu nhiên
subset_df = df.sample(n=1000, random_state=42)

# Save ra CSV để train multi-label
subset_df[['cxr_filename','slvh','dlv']].to_csv("data/Subset-Chexchonet/subset_labels.csv", index=False)

print("✅ Saved 1000-image subset with multi-labels")

for _, row in subset_df.iterrows():
    src_path = os.path.join("data/chexchonet/images", row['cxr_filename'])
    dst_path = os.path.join("data/Subset-Chexchonet/images", row['cxr_filename'])
    
    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    
    # Copy ảnh
    shutil.copy(src_path, dst_path)