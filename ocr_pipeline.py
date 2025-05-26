import os
import argparse
import pathlib
import mistralai # Added import as per requirement

# Placeholder for Mistral client initialization
# mistral_client = None

def get_processable_files(directory: pathlib.Path) -> list[pathlib.Path]:
    """
    Returns a list of files in the given directory with extensions .pdf, .png, or .jpg (case-insensitive).
    """
    supported_extensions = [".pdf", ".png", ".jpg"]
    processable_files = []
    for item in directory.iterdir():
        if item.is_file() and item.suffix.lower() in supported_extensions:
            processable_files.append(item)
    return processable_files

def main():
    """
    Main logic for the OCR pipeline script.
    """
    # Read Mistral API key
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        exit(1)

    # Initialize Mistral client
    # IMPORTANT: Uncomment the following line to use the actual Mistral API
    # mistral_client = mistralai.MistralClient(api_key=api_key)
    # For now, we'll print a message indicating it would be initialized.
    # When switching to actual API calls, ensure mistral_client is properly initialized above.
    print(f"Mistral client would be initialized if 'mistral_client = ...' line was uncommented. Using API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 4 else ''}")

    parser = argparse.ArgumentParser(description="OCR Pipeline Script")
    parser.add_argument("--file", type=pathlib.Path, help="Path to a single file to process.")
    args = parser.parse_args()

    files_to_process = []
    if args.file:
        if not args.file.exists():
            print(f"Error: File not found: {args.file}")
            exit(1)
        if args.file.suffix.lower() not in [".pdf", ".png", ".jpg"]:
            print(f"Error: Unsupported file type: {args.file}. Supported types are .pdf, .png, .jpg")
            exit(1)
        files_to_process.append(args.file)
    else:
        docs_dir = pathlib.Path("docs")
        if not docs_dir.is_dir():
            print(f"Error: 'docs' directory not found.")
            # Attempt to create it if it doesn't exist, as per later requirement for 'output'
            # For now, let's assume it should exist for input files
            exit(1)
        files_to_process = get_processable_files(docs_dir)
        if not files_to_process:
            print(f"No processable files found in {docs_dir}.")
            return # Exit gracefully if no files to process

    # Create output directory
    output_dir = pathlib.Path("output")
    output_dir.mkdir(exist_ok=True)

    for filepath in files_to_process:
        print(f"Processing file: {filepath}...")

        output_filename = f"{filepath.name}.md"
        output_filepath = output_dir / output_filename

        ocr_result_markdown = "" # Initialize variable

        # --- SIMULATED API CALLS ---
        # The following block simulates API interaction to avoid costs during development/testing.
        # To use the actual Mistral OCR API:
        # 1. Ensure your MISTRAL_API_KEY environment variable is correctly set.
        # 2. Ensure the `mistral_client = mistralai.MistralClient(api_key=api_key)` line earlier in this script is uncommented.
        # 3. Comment out or remove this simulation block below.
        # 4. Uncomment the 'ACTUAL API CALLS' block further down.

        print(f"Simulating: Uploading {filepath}...")
        # Simulate creating a dummy signed_url for the file
        signed_url_url = f"simulated_signed_url_for_{filepath.name}" 
        print(f"Simulating: Getting signed URL: {signed_url_url}")
        print(f"Simulating: Processing {filepath} via OCR API...")
        ocr_result_markdown = f"# OCR Output for {filepath.name}\n\nThis is simulated OCR text."
        # --- END OF SIMULATED API CALLS ---

        # --- ACTUAL API CALLS ---
        # # Uncomment the block below to use the real Mistral OCR API.
        # # Ensure your MISTRAL_API_KEY is set and the mistral_client is initialized earlier in this script.
        # try:
        #     print(f"INFO: Attempting actual API call for {filepath}. Ensure 'mistral_client' is initialized.")
        #     # Example: client = mistral_client # Assuming mistral_client is initialized globally or passed
        #
        #     print(f"Uploading {filepath}...")
        #     # Note: Ensure 'mistral_client' is the initialized MistralClient instance
        #     uploaded_file = mistral_client.files.upload(
        #         file={
        #             "file_name": filepath.name,
        #             "content": open(filepath, "rb"), # Read file in binary mode
        #         },
        #         purpose="ocr" # Set the purpose for OCR processing
        #     )
        #     print(f"Successfully uploaded. File ID: {uploaded_file.id}")
        #
        #     print(f"Getting signed URL for {uploaded_file.id}...")
        #     signed_url_response = mistral_client.files.get_signed_url(file_id=uploaded_file.id)
        #     signed_url_url = signed_url_response.url
        #     print(f"Successfully got signed URL: {signed_url_url}")
        #
        #     print(f"Processing {filepath} via OCR API...")
        #     ocr_response = mistral_client.ocr.process(
        #         model="mistral-ocr-latest", # Or your preferred OCR model
        #         document={
        #             "type": "document_url", # Using URL-based processing after upload
        #             "document_url": signed_url_url,
        #         },
        #         include_image_base64=False # Set to True if you need inline images in markdown
        #     )
        #     
        #     # Process the response:
        #     # The exact structure of ocr_response might vary.
        #     # This example assumes ocr_response.pages is a list of page objects,
        #     # and each page object has a 'markdown' attribute.
        #     # Adjust based on the actual API response structure from Mistral AI.
        #     if hasattr(ocr_response, 'pages') and isinstance(ocr_response.pages, list):
        #         ocr_result_markdown = "\n\n".join([page.markdown for page in ocr_response.pages if hasattr(page, 'markdown')])
        #     else:
        #         # Fallback or error handling if the response structure is not as expected
        #         ocr_result_markdown = f"# OCR Error: Unexpected API response structure for {filepath.name}"
        #         print(f"Error: Unexpected API response structure for {filepath.name}. Response: {ocr_response}")
        #
        #     print(f"Successfully processed {filepath}.")
        #
        # except mistralai.exceptions.MistralAPIException as e:
        #     print(f"A Mistral API error occurred while processing {filepath}: {e}")
        #     ocr_result_markdown = f"# API Error processing {filepath.name}\n\nAn API error occurred: {e}"
        # except Exception as e: # Catch other potential errors (e.g., file I/O)
        #     print(f"An unexpected error occurred while processing {filepath}: {e}")
        #     ocr_result_markdown = f"# Error processing {filepath.name}\n\nAn unexpected error occurred: {e}"
        # --- END OF ACTUAL API CALLS ---

        try:
            with open(output_filepath, "w") as f:
                f.write(ocr_result_markdown) # Use ocr_result_markdown here
            print(f"Output saved to: {output_filepath}")
        except IOError as e:
            print(f"Error writing output file {output_filepath}: {e}")

if __name__ == "__main__":
    main()
