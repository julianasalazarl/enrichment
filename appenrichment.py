import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(page_title="Product Enrichment Tool")
st.title("Seasonal Product Enrichment Tool")
st.markdown("""
Upload your Excel file with the seasonal articles. This tool will automatically enrich missing fields based on name patterns
and provide a downloadable Excel file with the completed data.
""")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

def enrich_data(df):
    df = df.copy()
    
    # Create the new enriched column based on conditions
    df["Enriched Product Line"] = df.apply(lambda row: (
        "Agravic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic" in row.get("Name", '') else
        "Samba;60s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba 62" in row.get("Name", '') else
        "Superstar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superstar" in row.get("Name", '') else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in row.get("Name", '') else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in row.get("Name", '') else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in row.get("Name", '') else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in row.get("Name", '') else
        row.get("PIM - Product Line (sportsub)")
    ), axis=1)
    
    return df

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        enriched_df = enrich_data(df)

        # Show preview
        st.success("File processed successfully! Here's a preview:")
        st.dataframe(enriched_df.head())

        # Convert to Excel for download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            enriched_df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Download Enriched Excel",
            data=output.getvalue(),
            file_name="enriched_products.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"There was an error processing the file: {e}")

