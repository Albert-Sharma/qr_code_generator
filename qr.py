import qrcode

# Array containing your URLs
link_arr = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

def generate_qr_codes(urls):
    """
    Generate QR codes for each URL in the provided array
    """
    for index, url in enumerate(urls):
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        filename = f"qr_code_{index}.png"
        img.save(filename)
        print(f"Generated QR code for {url} saved as {filename}")

# Generate QR codes for all URLs
generate_qr_codes(link_arr)