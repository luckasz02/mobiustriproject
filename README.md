# Möbius Strip Project

This project explores the fascinating properties of the Möbius strip through mathematics, programming, and visualization. The project demonstrates the topological and geometrical characteristics of the Möbius strip, offering an interactive experience with Python scripts and a web interface powered by Flask.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Description

The Möbius strip is a one-sided, non-orientable surface with unique properties. This project includes:

1. Mathematical analysis of the Möbius strip.
2. Interactive visualizations using Python and libraries like Matplotlib and Plotly.
3. Practical applications simulated using Flask, such as viewing the Möbius strip's real-world applications in materials science, physics, and art.

## Features

- **3D Visualization**: Generate and interact with the Möbius strip using Matplotlib and Plotly.
- **Mathematical Exploration**: Detailed exploration of the Euler characteristic, homology, and other mathematical concepts.
- **Code Execution**: Run Python scripts directly from the web interface.
- **Document Access**: View and download the project documentation on the Möbius strip.

## Installation

### Prerequisites

- Python 3.x
- Flask and other Python dependencies

### Install Dependencies

1. Clone the repository:

   https://github.com/luckasz02/mobiustriproject.git
   cd MobiusStripProj

2. Create a virtual environment and activate it:

   python -m venv .venv
   source .venv/bin/activate # On Windows, use .venv\Scripts\activate

3. Install required packages:

   pip install -r requirements.txt

## Usage

1. **Run the Flask server**:

   python app.py

2. **Access the Web Interface**:
   Open your browser and go to `http://127.0.0.1:5000`.

3. **Available Pages**:
   - **Home**: Introduction to the Möbius strip project.
   - **View Paper**: Embedded PDF document on the Möbius strip.
   - **Code Display**: View and execute Python scripts for visualizations and mathematical calculations.

## Project Structure

- **app.py**: Main Flask application file to serve the web interface and handle routes.
- **static/**: Folder containing CSS for styling.
- **templates/**: HTML templates for various pages (e.g., `index.html`, `view_paper.html`, `code.html`).
- **documents/**: Contains the PDF documentation on the Möbius strip.
- **scripts**: Python scripts for visualizations and calculations.
  - `script1.py`: Generates a basic 3D model of the Möbius strip using Matplotlib.
  - `script2.py`: Interactive 3D Möbius strip visualization with Plotly.
  - `script3.py`: Computes the Euler characteristic of a triangulated surface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Sample Code Execution

To run a specific Python script, go to the "View Code" page on the web interface, and click "Run Script" for the desired file. The output will be displayed on the same page.

### Future Enhancements

- Add more advanced simulations and visualizations.
- Explore deeper mathematical properties like knot theory in relation to the Möbius strip.

## Acknowledgments

Created by Luca Dumitru as part of a project to explore the mathematical beauty and real-world applications of the Möbius strip.
