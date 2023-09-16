import qrcode

# Function to generate a QR code
def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file
    qr_img.save(file_name)

if __name__ == "__main__":
    data = input("Enter the data for the QR code: ")
    file_name = input("Enter the filename for the QR code image (e.g., my_qr_code.png): ")

    generate_qr_code(data, file_name)
    print(f"QR code saved as '{file_name}'")
