"""Logic file.

This assembles the key_string and converts it into a QR-code."""

from datetime import datetime
import qrcode
import io

from data import N_CONST


def generate_qr_string(r_value: str) -> str:
    """
    Generates complete string for the QR.

    Args:
        r_value (str): Key-code for any given classroom.

    Returns:
        str: Complete formatted key-string for generating the QR.
    """
    # Get current date in format YYYYMMDD
    current_date = datetime.now().strftime("%Y%m%d")

    # Assemble key-string with pattern: IEST-YYYYMMDD-N_CONST-10.r_value
    qr_data_string = f"IEST-{current_date}-{N_CONST}-10.{r_value}"

    return qr_data_string


def create_qr_image(data_string: str):
    """
    GGenerates the QR code picture for the given key-string.

    Args:
        data_string (str): String to codify into the QR code.

    Returns:
        PIL.Image.Image: PIL (Pillow) picture object of the QR-code.
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )
    qr.add_data(data_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")  # Saves picture in buffer to png
    return buffer.getvalue()  # returns buffet


if __name__ == "__main__":
    print("For room 203, code is '3.1.26'\n")
    print("Key-string:")
    print(generate_qr_string("3.1.26"), '\n')
    print("...generating qr...")
    with open("test_qr.png", "wb") as f:
        f.write(create_qr_image(generate_qr_string("3.1.26")))
        print("QR saved to test_qr.png")
