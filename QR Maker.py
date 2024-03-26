import pyqrcode     #pip install pyqrcode

def create_qr_code(text, filename, scale): #define the qr creator



  qr_code = pyqrcode.create(text)

  try:
    qr_code.png(filename, scale=scale)
    print(f"QR code created and saved as: {filename}")
  except Exception as e:
    print(f"Error creating QR code: {e}")

#running the main program
if __name__ == "__main__":
  user_input = input("Enter Link or Text: ")
  create_qr_code(user_input, "example.png", 6)  #replace example with the file name to be stored as.

