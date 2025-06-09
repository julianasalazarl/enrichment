
# Seasonal Product Enrichment Tool

This is a Streamlit web application designed to automate the enrichment of missing product attributes based on naming patterns in product data.

## How it works

1. Upload an Excel file containing seasonal article data.
2. The app analyzes product names and fills in missing product line fields using predefined rules.
3. Download the enriched file with new data.

## Features

- No coding required: users interact through a web interface.
- Custom rules for enrichment based on product name patterns.
- Automatically generates a downloadable Excel file.

## How to run

1. Clone the repository or extract the zip file.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Input

An `.xlsx` file with at least a `Name` column and optionally a `PIM - Product Line (sportsub)` column.

## Output

An enriched `.xlsx` file with a new column `Enriched Product Line`.

---
Created with ❤️ using Python and Streamlit.
