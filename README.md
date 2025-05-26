# OCR Pipeline with Mistral AI

This project provides a Python script (`ocr_pipeline.py`) to perform Optical Character Recognition (OCR) on documents (PDF, PNG, JPG) using the Mistral AI API (currently simulated). It processes input files and generates Markdown text as output.

## Installation

To install the necessary dependencies, navigate to the project's root directory in your terminal and run:

```bash
pip install -r requirements.txt
```

## Configuration

### Mistral API Key

This script requires a Mistral API key to interact with the Mistral AI services. You must set this key as an environment variable named `MISTRAL_API_KEY`.

**Crucial**: Without this key, the script will not be able to connect to the Mistral API when the actual API calls are implemented.

**Linux/macOS:**

You can set the environment variable in your terminal session like this:

```bash
export MISTRAL_API_KEY="YOUR_API_KEY_HERE"
```

To make it permanent, add this line to your shell's configuration file (e.g., `.bashrc`, `.zshrc`).

**Windows:**

You can set environment variables through the System Properties:
1. Search for "environment variables" in the Start Menu.
2. Click on "Edit the system environment variables".
3. In the System Properties window, click the "Environment Variables..." button.
4. In the Environment Variables window, you can add or modify `MISTRAL_API_KEY` under "User variables" or "System variables".
5. You might need to restart your terminal or system for the changes to take effect.

Replace `"YOUR_API_KEY_HERE"` with your actual Mistral API key.

## Usage

1.  **Place Input Documents**: Put your input files (supported formats: `.pdf`, `.png`, `.jpg`) into the `docs/` directory located in the project's root. If this directory does not exist, you should create it.

2.  **Run the Script**:
    *   **To process all documents in the `docs/` folder:**
        Open your terminal, navigate to the project's root directory, and run:
        ```bash
        python ocr_pipeline.py
        ```
    *   **To process a specific file:**
        You can specify a single file to process using the `--file` argument:
        ```bash
        python ocr_pipeline.py --file docs/your_document.pdf
        ```
        Replace `docs/your_document.pdf` with the actual path to your file.

3.  **Output**:
    The script will generate Markdown (`.md`) files in the `output/` directory. The output directory will be created if it doesn't exist. Each output file will have the original filename with `.md` appended.
    For example, if you process `docs/sample.pdf`, the output will be `output/sample.pdf.md`.

## Note on Current Implementation

The current version of `ocr_pipeline.py` **simulates** the API calls to Mistral AI and generates placeholder Markdown output. It does not perform real OCR operations yet.

To use this script with the actual Mistral OCR API, you will need to:

1.  Ensure you have a valid Mistral API key and have set the `MISTRAL_API_KEY` environment variable as described in the Configuration section.
2.  Modify the `ocr_pipeline.py` script to uncomment the sections responsible for actual API interaction and replace or fill in the simulation blocks with the real API call logic. Future updates may include command-line flags to switch between simulated and real modes.
