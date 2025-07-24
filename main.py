# main.py
from converter_json_csv import convert_json_to_csv
from app import process_csv

if __name__ == "__main__":
    # Input JSON path
    input_json = "New Text Document.json"  # Change path as needed
    intermediate_csv = "raw_text_batch.csv"
    output_csv = "ad_extraction_results.csv"

    print("🔄 Step 1: Converting JSON to CSV...")
    convert_json_to_csv(input_json, intermediate_csv)

    print("🔄 Step 2: Running LLM extraction on CSV...")
    process_csv(intermediate_csv, output_csv)

    print("✅ All steps completed successfully!")
