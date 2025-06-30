import pandas as pd

# Load mapping file
mapping_df = pd.read_excel('WMS-04-02.xlsx', skiprows=2)
mapping_df['sku'] = mapping_df['sku'].astype(str).str.strip().str.lower()

# Load sales file
sales_df = pd.read_csv('Cste FK.csv')
sales_df['SKU'] = sales_df['SKU'].astype(str).str.strip().str.lower()

# Show top 10 SKU values from each
print("\n📦 Mapping SKUs:", mapping_df['sku'].dropna().unique()[:10])
print("🧾 Sales SKUs:", sales_df['SKU'].dropna().unique()[:10])

# Merge
merged_df = sales_df.merge(mapping_df, left_on='SKU', right_on='sku', how='left')

# Result
print("\nTotal Rows:", len(merged_df))
print("Mapped SKUs:", merged_df['msku'].notnull().sum())
print("Missing SKUs:", merged_df['msku'].isnull().sum())
