# app.py

from flask import Flask, render_template, request
import pandas as pd
import os
import random

app = Flask(__name__)

# Load data from Excel file
def load_data_from_excel(file_path, output_folder='json_data'):
    try:
        os.makedirs(output_folder, exist_ok=True)
        excel_data = pd.ExcelFile(file_path)

        data_frames = {}
        for sheet_name in excel_data.sheet_names:
            df = excel_data.parse(sheet_name=sheet_name)
            json_file_path = os.path.join(output_folder, f"{sheet_name.lower()}.json")
            df.to_json(json_file_path, orient='records')
            data_frames[sheet_name] = df

        return data_frames

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Serve static files (CSS and JS)
app.static_folder = 'static'

# Load data frames from Excel file
file_path = 'Vocabulary.xlsx'  # Change this to the actual path
data_frames = load_data_from_excel(file_path)

# Define the route to render flashcards with a dynamic data type
@app.route('/', methods=['GET', 'POST'])
def flashcards():
    data_type = request.args.get('data_type', 'Adjectives')  # Default to 'Adjectives' if not provided
    flashcards_data = data_frames.get(data_type, pd.DataFrame()).to_dict(orient='records')
    random.shuffle(flashcards_data)
    return render_template('index.html', flashcards_data=flashcards_data)

if __name__ == '__main__':
    app.run(debug=True)
