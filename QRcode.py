import qrcode
from PIL import Image

def generate_qr_code():
    # Get website link from user
    website_link = input("Enter the website link: ")
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(website_link)
    qr.make(fit=True)
    
    # Create QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    filename = "thelordsblessingFoundation.png"
    qr_image.save(filename)
    
    print(f"QR code generated and saved as {filename}")
    
    # Display QR code
    qr_image.show()

if __name__ == "__main__":
    generate_qr_code()
