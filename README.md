# OCR Pipeline with Mistral AI

This project provides a simple Python script (`ocr_pipeline.py`) to run Mistral OCR on all documents (PDF, PNG, JPG) found in the `docs/` directory. It processes these input files and generates Markdown text as output in the `output/` directory.

## Installation

To install the necessary dependencies, navigate to the project's root directory in your terminal and run:

```bash
pip install -r requirements.txt
```

## Configuration

### Mistral API Key

This script requires a Mistral API key to interact with the Mistral AI services. 

You can set this key as an environment variable named `MISTRAL_API_KEY`.

**Linux/macOS:**
```bash
export MISTRAL_API_KEY="YOUR_API_KEY_HERE"
```
To make it permanent, add this line to your shell's configuration file (e.g., `.bashrc`, `.zshrc`).

**Windows:**
Set `MISTRAL_API_KEY` via System Properties > Environment Variables.

Alternatively, if the `MISTRAL_API_KEY` environment variable is not found when the script runs, you will be prompted to enter it directly in the terminal.

Replace `"YOUR_API_KEY_HERE"` with your actual Mistral API key.

## Usage

1.  **Place Input Documents**: Put your input files (supported formats: `.pdf`, `.png`, `.jpg`) into the `docs/` directory. If this directory does not exist, create it.

2.  **Run the Script**:
    *   **To process all documents in the `docs/` folder:**
        Open your terminal, navigate to the project's root, and run:
        ```bash
        python ocr_pipeline.py
        ```
    *   **To process a specific file:**
        Use the `--file` argument:
        ```bash
        python ocr_pipeline.py --file docs/your_document.pdf
        ```

3.  **Output**:
    Markdown (`.md`) files will be generated in the `output/` directory (created if it doesn's exist). Each output file will have the original filename with `.md` appended (e.g., `docs/sample.pdf` becomes `output/sample.pdf.md`).
