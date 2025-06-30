import pandas as pd

# Load sales file
sales_df = pd.read_csv('Cste FK.csv')
sales_df['SKU'] = sales_df['SKU'].astype(str).str.strip().str.lower()

# Extract unique SKUs
unique_skus = sales_df['SKU'].dropna().unique()

# Create a mapping template Excel
mapping_template = pd.DataFrame({'sku': unique_skus, 'msku': ''})
mapping_template.to_excel('mapping_template.xlsx', index=False)

print("✅ mapping_template.xlsx created. Open it, fill 'msku' values, and save.")
