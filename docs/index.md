# Invoice PDF Generator

Welcome to the documentation for the Invoice PDF Generator Python package! This document provides an overview of the package, installation instructions, usage examples, and other relevant information.

## Overview
The Invoice PDF Generator is a Python package designed to simplify the process of creating PDF invoices from Excel invoice data. With this package, you can quickly generate professional-looking invoices for your business needs.

## Installation
You can install the Invoice PDF Generator package via pip:

```bash
pip install invoice_pdfgen
```

## Usage
To use the Invoice PDF Generator package, follow these steps:

1. Import the `PDFInvoiceGenerator` class from the package.
2. Create an instance of the `PDFInvoiceGenerator` class, providing the paths to the Excel invoice file and the company logo.
3. Generate the PDF invoice using the `generate()` method.

```python
from invoice_pdfgen import PDFInvoiceGenerator

# Create an instance of PDFInvoiceGenerator
generator = PDFInvoiceGenerator(excel_filepath='invoice_data.xlsx', logo_filepath='company_logo.png')

# Generate the PDF invoice
generator.generate()
```

For more detailed usage instructions and examples, please refer to the [examples](../examples) directory.

## License
This project is licensed under the **MIT License**, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.
