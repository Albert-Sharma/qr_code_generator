import qrcode
from PIL import Image

def generate_qr_codes_with_logo(urls, logo_path):
    """
    Generate QR codes with a center logo for each URL in the provided array
    
    Parameters:
    urls (list): List of URLs to encode in QR codes
    logo_path (str): Path to the logo image file
    """
    # Open the logo image
    logo = Image.open(logo_path)
    
    # Calculate logo size - must be smaller than QR code
    basewidth = 100  # Adjust this value to change logo size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    
    for index, url in enumerate(urls):
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Use high error correction
            box_size=10,
            border=4,
        )
        
        # Add data
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
        
        # Calculate position to paste logo
        pos = ((qr_image.size[0] - logo.size[0]) // 2,
               (qr_image.size[1] - logo.size[1]) // 2)
        
        # Create a white background for the logo
        logo_background = Image.new('RGBA', logo.size, 'white')
        logo_background.paste(logo, (0, 0), logo)
        
        # Paste the logo
        qr_image.paste(logo_background, pos)
        
        # Save the QR code
        filename = f"qr_code_with_logo_{index}.png"
        qr_image.save(filename)
        print(f"Generated QR code with logo for {url} saved as {filename}")

# Example usage
link_arr = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# Generate QR codes with logo
generate_qr_codes_with_logo(link_arr, "sav_logo.png")