import os
import argparse
import pathlib
from mistralai import Mistral
import getpass

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
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("MISTRAL_API_KEY environment variable not set.")
        api_key = getpass.getpass("Please enter your Mistral API Key: ")
        if not api_key:
            print("Error: No API key provided. Exiting.")
            exit(1)
        print("API Key received.")


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
            print(f"Error: 'docs' directory not found. Please create it and add your documents.")
            exit(1)
        files_to_process = get_processable_files(docs_dir)
        if not files_to_process:
            print(f"No processable files found in {docs_dir}.")
            return

    output_dir = pathlib.Path("output")
    output_dir.mkdir(exist_ok=True)

    # Initialize Mistral client using a context manager
    with Mistral(api_key=api_key) as mistral_client:
        print(f"Mistral client initialized. Using API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 8 else '****'}")

        for filepath in files_to_process:
            print(f"Processing file: {filepath}...")

            output_filename = f"{filepath.name}.md"
            output_filepath = output_dir / output_filename
            ocr_result_markdown = ""

            try:
                print(f"INFO: Uploading {filepath}...")
                uploaded_file = mistral_client.files.upload(
                    file={
                        "file_name": filepath.name,
                        "content": open(filepath, "rb"),
                    },
                    purpose="ocr"
                )
                print(f"Successfully uploaded. File ID: {uploaded_file.id}")

                print(f"INFO: Getting signed URL for {uploaded_file.id}...")
                signed_url_response = mistral_client.files.get_signed_url(file_id=uploaded_file.id)
                signed_url_url = signed_url_response.url
                print(f"Successfully got signed URL.") # No need to print the full URL

                print(f"INFO: Processing {filepath} via OCR API...")
                ocr_response = mistral_client.ocr.process(
                    model="mistral-ocr-latest",
                    document={
                        "type": "document_url",
                        "document_url": signed_url_url,
                    },
                    include_image_base64=False
                )
                
                if hasattr(ocr_response, 'pages') and isinstance(ocr_response.pages, list):
                    ocr_result_markdown = "\n\n".join([page.markdown for page in ocr_response.pages if hasattr(page, 'markdown')])
                else:
                    ocr_result_markdown = f"# OCR Error: Unexpected API response structure for {filepath.name}"
                    print(f"Error: Unexpected API response structure for {filepath.name}. Response: {ocr_response}")

                print(f"Successfully processed {filepath}.")

            except mistralai.exceptions.MistralAPIException as e:
                print(f"A Mistral API error occurred while processing {filepath}: {e}")
                ocr_result_markdown = f"# API Error processing {filepath.name}\n\nAn API error occurred: {e}"
            except Exception as e:
                print(f"An unexpected error occurred while processing {filepath}: {e}")
                ocr_result_markdown = f"# Error processing {filepath.name}\n\nAn unexpected error occurred: {e}"

            try:
                with open(output_filepath, "w") as f:
                    f.write(ocr_result_markdown)
                print(f"Output saved to: {output_filepath}")
            except IOError as e:
                print(f"Error writing output file {output_filepath}: {e}")

if __name__ == "__main__":
    main()
