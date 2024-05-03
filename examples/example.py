from invoice_pdfgen import PDFInvoiceGenerator
from pathlib import Path

# Define constants for directories and file paths
ASSETS_DIR = Path("./assets")
EXCEL_DOCS_DIR = ASSETS_DIR / "invoices"
OUTPUT_DIR = ASSETS_DIR / "invoices_PDF"
LOGO_PATH = ASSETS_DIR / "logo" / "python.png"


def generate_PDF_invoice(excel_filepath):
    """
    Generate a PDF invoice from an Excel file.

    Args:
        excel_filepath (Path): Path to the Excel file containing invoice data.
    """
    # Create an instance of PDFInvoiceGenerator
    generator = PDFInvoiceGenerator(excel_filepath=str(
        excel_filepath), logo_filepath=str(LOGO_PATH), output_directory=str(OUTPUT_DIR))

    # Generate the PDF invoice
    generator.generate()


def main():
    try:
        # Create the output directory if it doesn't exist
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Get a generator object of all Excel files paths in the specified directory
        excel_files = EXCEL_DOCS_DIR.glob("*.xlsx")

        # Iterate over each Excel file of this generator and generate a PDF invoice respectively
        for filepath in excel_files:
            generate_PDF_invoice(filepath)

        print("\n--- PDF invoices generated successfully ---\n")
    except Exception as e:
        print("\n--- Failure in generating PDF invoices: ---\n")
        print(f"\nError message: {e}\n")


if __name__ == "__main__":
    main()
