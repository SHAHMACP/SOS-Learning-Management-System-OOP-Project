# ============================================================
#           SOS - SCHOOL OF SKILLS
#         LEARNING MANAGEMENT SYSTEM (LMS)
#                  pdf_utils.py
# ============================================================
#
# Builds the downloadable PDFs:
#   - build_certificate_pdf : landscape A4 certificate + QR code
#   - build_receipt_pdf     : A5 fee receipt
#
# Only reportlab and Pillow are needed (the QR code comes from
# reportlab itself). Standard PDF fonts have no rupee sign, so
# amounts are printed as "Rs.".
# ============================================================

import base64
from functools import lru_cache
from io import BytesIO

from PIL import Image, ImageChops
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A5, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

from sos import Institution


SOS_RED = colors.HexColor("#A31F24")
SOS_RED_DARK = colors.HexColor("#7E1519")
SOS_TINT = colors.HexColor("#FBEAEA")
SOS_TEXT = colors.HexColor("#241414")
SOS_GREY = colors.HexColor("#6B5B5B")


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

@lru_cache(maxsize=None)
def get_logo_image(logo_path, max_px=700):
    """Logo as a white-background RGB image with the margins trimmed."""

    image = Image.open(logo_path).convert("RGBA")

    # Flatten any transparency onto white (otherwise it turns black)
    white = Image.new("RGBA", image.size, (255, 255, 255, 255))
    image = Image.alpha_composite(white, image).convert("RGB")

    white = Image.new("RGB", image.size, (255, 255, 255))
    diff = ImageChops.difference(image, white).convert("L")
    box = diff.point(lambda p: 255 if p > 20 else 0).getbbox()

    if box:
        image = image.crop(box)

    # Keep files small: a logo never needs more than this
    image.thumbnail((max_px, max_px))
    return image


@lru_cache(maxsize=None)
def logo_data_uri(logo_path, max_px=420):
    """Logo as a base64 data-URI, ready for an HTML <img src=...>."""

    buffer = BytesIO()
    get_logo_image(logo_path, max_px).save(buffer, format="PNG", optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return "data:image/png;base64," + encoded


def _load_logo(logo_path):
    """Logo prepared for reportlab: (ImageReader, (width, height))."""

    try:
        image = get_logo_image(logo_path)
        return ImageReader(image), image.size

    except Exception:
        return None, None


def _draw_logo(pdf, logo_path, center_x, top_y, max_w, max_h):
    """Draw the logo centred at center_x, hanging from top_y."""

    logo, size = _load_logo(logo_path)
    if logo is None:
        return

    scale = min(max_w / size[0], max_h / size[1])
    width, height = size[0] * scale, size[1] * scale

    pdf.drawImage(
        logo,
        center_x - width / 2,
        top_y - height,
        width=width,
        height=height,
        mask="auto"
    )


def _fit_font(text, font, size, max_width, min_size=10):
    """Shrink the font size until the text fits max_width."""

    while size > min_size and stringWidth(text, font, size) > max_width:
        size -= 1
    return size


def _draw_qr(pdf, data, x, y, size):
    widget = QrCodeWidget(data)
    left, bottom, right, top = widget.getBounds()

    drawing = Drawing(
        size,
        size,
        transform=[
            size / (right - left), 0,
            0, size / (top - bottom),
            0, 0
        ]
    )
    drawing.add(widget)
    renderPDF.draw(drawing, pdf, x, y)


def _money(amount):
    return f"Rs. {amount:,}"


# ------------------------------------------------------------
# Certificate
# ------------------------------------------------------------

def build_certificate_pdf(cert, logo_path):
    """Return the certificate as PDF bytes (landscape A4)."""

    buffer = BytesIO()
    width, height = landscape(A4)
    center = width / 2

    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    pdf.setTitle(f"Certificate - {cert.student_name}")
    pdf.setAuthor(Institution.institution_name)

    # ---------- Borders ----------
    pdf.setStrokeColor(SOS_RED)
    pdf.setLineWidth(8)
    pdf.rect(18, 18, width - 36, height - 36)

    pdf.setStrokeColor(SOS_RED_DARK)
    pdf.setLineWidth(1.2)
    pdf.rect(30, 30, width - 60, height - 60)

    pdf.setFillColor(SOS_RED)
    for corner_x in (30, width - 44):
        for corner_y in (30, height - 44):
            pdf.rect(corner_x, corner_y, 14, 14, stroke=0, fill=1)

    # ---------- Logo ----------
    _draw_logo(pdf, logo_path, center, height - 48, 220, 80)

    # ---------- Heading ----------
    pdf.setFillColor(SOS_RED)
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawCentredString(center, height - 180, "CERTIFICATE OF COMPLETION")

    pdf.setStrokeColor(SOS_RED)
    pdf.setLineWidth(2)
    pdf.line(center - 70, height - 194, center + 70, height - 194)

    # ---------- Body ----------
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawCentredString(center, height - 226, "This is to certify that")

    name = cert.student_name
    name_size = _fit_font(name, "Helvetica-Bold", 36, width - 200)
    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica-Bold", name_size)
    pdf.drawCentredString(center, height - 272, name)

    line_half = min(stringWidth(name, "Helvetica-Bold", name_size) / 2 + 30,
                    (width - 160) / 2)
    pdf.setStrokeColor(SOS_RED_DARK)
    pdf.setLineWidth(1)
    pdf.line(center - line_half, height - 282, center + line_half, height - 282)

    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawCentredString(
        center, height - 314, "has successfully completed the course"
    )

    course = cert.course_title
    course_size = _fit_font(course, "Helvetica-Bold", 26, width - 200)
    pdf.setFillColor(SOS_RED_DARK)
    pdf.setFont("Helvetica-Bold", course_size)
    pdf.drawCentredString(center, height - 350, course)

    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        center,
        height - 384,
        f"Grade: {cert.grade}     |     Attendance: {cert.attendance}%"
    )

    # ---------- Bottom row: date | QR | signatory ----------
    left_x = 170
    right_x = width - 170

    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(left_x, 122, str(cert.issue_date))
    pdf.setStrokeColor(SOS_TEXT)
    pdf.setLineWidth(0.8)
    pdf.line(left_x - 80, 114, left_x + 80, 114)
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(left_x, 100, "Date of Issue")

    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica-BoldOblique", 12)
    pdf.drawCentredString(right_x, 122, Institution.Founder.title())
    pdf.line(right_x - 80, 114, right_x + 80, 114)
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(right_x, 100, "Founder & Authorised Signatory")

    qr_size = 84
    _draw_qr(pdf, cert.cert_number, center - qr_size / 2, 76, qr_size)

    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(center, 64, f"Certificate No: {cert.cert_number}")
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica", 7.5)
    pdf.drawCentredString(
        center, 52,
        "Verify authenticity via 'Verify Certificate' in the SOS LMS."
    )

    pdf.showPage()
    pdf.save()

    return buffer.getvalue()


# ------------------------------------------------------------
# Fee receipt
# ------------------------------------------------------------

def build_receipt_pdf(payment, logo_path):
    """Return a fee receipt as PDF bytes (A5 portrait)."""

    buffer = BytesIO()
    width, height = A5
    center = width / 2

    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    pdf.setTitle(f"Receipt {payment.receipt_no}")
    pdf.setAuthor(Institution.institution_name)

    # ---------- Border ----------
    pdf.setStrokeColor(SOS_RED)
    pdf.setLineWidth(4)
    pdf.rect(14, 14, width - 28, height - 28)

    # ---------- Header ----------
    _draw_logo(pdf, logo_path, center, height - 30, 170, 58)

    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(center, height - 108, Institution.institution_name)
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica", 8.5)
    pdf.drawCentredString(
        center, height - 121,
        f"{Institution.location}  |  {Institution.contact_number}  |  "
        f"{Institution.email}"
    )

    pdf.setFillColor(SOS_RED)
    pdf.rect(30, height - 160, width - 60, 26, stroke=0, fill=1)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(center, height - 152, "FEE RECEIPT")

    # ---------- Details ----------
    rows = [
        ("Receipt No.", payment.receipt_no),
        ("Date", str(payment.payment_date)),
        ("Student ID", payment.student_id),
        ("Student Name", payment.student_name),
        ("Course", payment.course_title),
        ("Payment Mode", payment.mode),
    ]

    y = height - 195
    for label, value in rows:
        pdf.setFillColor(SOS_GREY)
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40, y, label)

        size = _fit_font(value, "Helvetica", 10.5, width - 200, min_size=7)
        pdf.setFillColor(SOS_TEXT)
        pdf.setFont("Helvetica", size)
        pdf.drawString(150, y, value)
        y -= 24

    # ---------- Amount box ----------
    pdf.setFillColor(SOS_TINT)
    pdf.setStrokeColor(SOS_RED)
    pdf.setLineWidth(1)
    pdf.rect(30, 196, width - 60, 66, stroke=1, fill=1)

    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(center, 246, "AMOUNT PAID")
    pdf.setFillColor(SOS_RED)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(center, 214, _money(payment.amount))

    # ---------- Balance ----------
    pdf.setFillColor(SOS_TEXT)
    pdf.setFont("Helvetica", 10.5)
    pdf.drawString(40, 172, "Balance due after this payment:")
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawRightString(width - 40, 172, _money(payment.balance_after))

    if payment.balance_after <= 0:
        status = "FEE FULLY PAID"
        status_color = colors.HexColor("#1B7F3B")
    else:
        status = "PARTIAL PAYMENT"
        status_color = SOS_RED_DARK

    pdf.setFillColor(status_color)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(40, 150, status)

    # ---------- Signature + footer ----------
    pdf.setStrokeColor(SOS_TEXT)
    pdf.setLineWidth(0.8)
    pdf.line(width - 190, 104, width - 40, 104)
    pdf.setFillColor(SOS_GREY)
    pdf.setFont("Helvetica", 9)
    pdf.drawCentredString(width - 115, 91, "Authorised Signatory")

    pdf.setFont("Helvetica-Oblique", 8)
    pdf.drawCentredString(
        center, 40, "This is a computer-generated receipt."
    )

    pdf.showPage()
    pdf.save()

    return buffer.getvalue()
