# VehicleNumberPlateRecognition

Explanation of Each Line:

Importing Libraries:
cv2 (OpenCV) for image processing.
numpy for handling numerical operations.
easyocr for Optical Character Recognition (OCR).

Function detect_number_plate(image_path):
Reads an image using cv2.imread().
Converts it to grayscale (cv2.cvtColor()).
Detects edges using the Canny Edge Detector (cv2.Canny()).

Finding Contours:
Extracts contours using cv2.findContours().
Loops through detected contours to find a rectangular shape.
If a rectangle is found, it extracts the number plate.

Text Recognition Using EasyOCR:
Uses easyocr.Reader(['en']) to initialize OCR.
reader.readtext(plate) extracts text from the cropped plate.

Displaying Output:
Prints detected text.
Displays the detected number plate using cv2.imshow().
