from flask import Flask, render_template, send_file, send_from_directory, request, jsonify
import subprocess
import os
import sys
from docx import Document
from fpdf import FPDF
from markupsafe import Markup

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the Möbius Strip page
@app.route('/view_paper')
def view_paper():
    return render_template('view_paper.html')

# Route for downloading the Word document
@app.route('/download_paper')
def download_paper():
    return send_from_directory('static/documents', 'Exploring_Möbius_Strip.docx', as_attachment=True)

# Helper function to read the content of each script file
def read_script_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {filename} not found."

# Route for viewing the code
@app.route("/code")
def view_code():
    return render_template(
        "code.html",
        script1_code=read_script_file("script1.py"),
        script2_code=read_script_file("script2.py"),
        script3_code=read_script_file("script3.py")
    )

# Route to run each script by its name
@app.route("/run_script/<script_name>")
def run_script(script_name):
    script_map = {
        "script1": "script1.py",
        "script2": "script2.py",
        "script3": "script3.py"
    }

    script_path = script_map.get(script_name)
    if script_path:
        try:
            result = subprocess.run(
    ["python", script_path],
    capture_output=True,
    text=True
)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)
    else:
        return "Script not found", 404


if __name__ == "__main__":
    app.run(debug=True)
