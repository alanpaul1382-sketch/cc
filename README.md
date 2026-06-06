# How to generate the PPTX

1. Create a Python virtualenv and install requirements:

   python -m venv venv
   source venv/bin/activate   # (Linux/macOS)
   venv\Scripts\activate    # (Windows)
   pip install -r requirements.txt

2. Run the generator script:

   python generate_presentation.py

This will produce Haidilao_SmartTable_MarketingPlan.pptx at the repo root.

Notes:
- The script uses placeholder assets. Replace assets in assets/haidilao/ with actual brand files to include them in the presentation.
- If you want me to commit the final PPTX directly, run the script locally and commit the generated file, or grant me direct file upload permissions.
