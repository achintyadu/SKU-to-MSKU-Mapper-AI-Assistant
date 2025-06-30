# 📦 SKU to MSKU Mapper + AI Assistant 🤖

This project is part of the **WMS Assignment** where we clean, map, and analyze sales data using Python.  
It includes a **Streamlit web app** that helps users map `SKU → MSKU`, and includes an **AI assistant** to ask questions in natural language.

---

## 🧠 Features

- ✅ Upload any sales CSV file (e.g. Flipkart)
- ✅ Automatically map SKUs to MSKUs using a mapping file
- ✅ Show total rows, mapped SKUs, missing SKUs
- ✅ Download cleaned sales file as CSV
- 🤖 Ask AI questions like:
  - “Which MSKU sold the most?”
  - “Show quantity sold by product”
  - “Top 5 products by revenue”

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** (for frontend GUI)
- **Pandas** (for data processing)
- **PandasAI** + **OpenAI API** (for AI assistant)
- **Baserow** (for relational DB visual demo)

---

## 📁 Project Structure

├── app.py # Streamlit app with AI
├── mapping_template.csv # SKU → MSKU master file
├── sales_with_msku.csv # Cleaned output
├── .env # API key (not committed)
├── .gitignore
