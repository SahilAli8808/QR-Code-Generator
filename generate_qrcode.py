import csv
import qrcode
import webbrowser

# Path to the CSV file
csv_file = 'coordinates.csv'

# Read latitude and longitude data from the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if present
    for row in csv_reader:
        latitude, longitude = row

        # Create a Google Maps URL with the latitude and longitude
        map_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

        # Generate QR code with the Google Maps URL
        qr_code = qrcode.QRCode()
        qr_code.add_data(map_url)
        qr_code.make()

        # Save the QR code as an image file
        qr_code_image = qr_code.make_image()
        qr_code_image.save(f"qr_code_{latitude}_{longitude}.png")

        # Open the generated QR code in the default image viewer
        qr_code_image.show()

        # Open the Google Maps URL in a web browser
        webbrowser.open(map_url)
