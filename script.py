import gspread
import os
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

JSON_GOOGLE_CREDS =json.loads(os.environ["JSON_GOOGLE_CREDS"])
PDF_FILE_PATH = "./my_report.pdf"
SPREADSHEET = "link_to_my_spreadsheet"
WORKSHEET = "my_worksheet_name"

logging.basicConfig(level=logging.INFO)

def main():
    gc = gspread.service_account_from_dict(JSON_GOOGLE_CREDS)
    worksheet = gc.open_by_url(SPREADSHEET).get_worksheet(WORKSHEET)

    c = canvas.Canvas(PDF_FILE_PATH, pagesize=letter)
    width, height = letter
    c.setPageSize((width, height))
    x, y = 50, height - 50

    for row in worksheet.get_all_values():
        for value in row:
            c.drawString(x, y, value)
            x += 50 
        y -= 15
        x = 50 
    c.showPage()
    c.save()
    logging(f'Export is completed. Look for the file here {PDF_FILE_PATH}')

if __name__ == "__main__":
    main()
