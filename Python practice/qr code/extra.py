import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask


# QR Code with Custom Color Mask
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)
# Add data to QR Code
qr.add_data("https://www.facebook.com")
qr.make(fit=True)


# Generate QR with Color Gradient
img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=RadialGradiantColorMask(
        back_color=(0, 0, 255),      # Background color (Blue)
        center_color=(255, 0, 0),    # Center color (Red)
        edge_color=(0, 255, 0),      # Edge color (Green)
    ),
)

# Save QR
img.save("qrimg/gradient_qr.png")


