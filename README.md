# 🧠 Ad Information Extraction using DeepSeek-R1-Distill-Qwen-1.5B

This project extracts **Brand**, **Product**, and **Category** from raw OCR advertisement text using **LLM-based reasoning**. The pipeline uses the **DeepSeek-R1-Distill-Qwen-1.5B** model from Hugging Face for advanced reasoning and accurate text understanding.

---

##  Features
✔ Handles **noisy OCR ad text** effectively  
✔ Extracts **Brand**, **Product**, and **Category** with custom rules  
✔ Processes **batch data from CSV** and outputs structured results  
✔ Ready for **deployment and scaling**  

---

##  Folder Structure
```
ad_extraction_project/
│── main.py # Core script for inference
│── raw_text_batch.csv # Input file with raw ad texts
│── ad_extraction_results.csv # Output file with extracted info
│── prompts/
│ └── ad_extraction_prompt.txt # Prompt template
│── README.md # Project documentation
│── requirements.txt # Dependencies

```
---

##  Technologies Used
- **Model:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`
- **Libraries:**  
  - `transformers` (Hugging Face)
  - `torch`
  - `pandas`
  

---

## 🚀 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/devatroneoptimus/ad-extraction-llm.git
   cd ad-extraction-llm
### 2. ✅ Set up Python and Virtual Environment


```bash
python3 -m venv env
source env/bin/activate     # On Mac/Linux
env\Scripts\activate        # On Windows
```

---

### 3. ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

---
### 4. ✅ Run the Application

```bash
python app.py
```

