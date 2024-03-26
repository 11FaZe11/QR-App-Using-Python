import pyqrcode           #pip install pyqrcode

def create_qr_code(text, filename, scale):

    qr_code = pyqrcode.create(text)  # Create the QR code object

    try:
        if not filename.endswith(".png"):  # Check for .png extension
            filename += ".png"  # Add if missing
        qr_code.png(filename, scale=scale)  # Save the QR code as a PNG image
        print(f"QR code created and saved as: {filename}")
    except Exception as e:
        print(f"Error creating QR code: {e}")  # Provide a more informative error message

while True:  # Continuous loop for repeated QR code generation
    user_input = input("Enter Link or Text: ")
    filename = input("Enter the filename (include extension, e.g., my_qr_code.png): ")
    create_qr_code(user_input, filename, 6)

    choice = input("Would you like to create another QR code? (Enter 1 for yes, 0 to exit): ")
    if choice == "0":
        break  # Exit the loop if user enters 0

print("Exiting program.")
