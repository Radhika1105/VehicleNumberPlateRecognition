import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations
import easyocr  # Import EasyOCR for text recognition

def detect_number_plate(image_path):
    """
    Function to detect a vehicle's number plate and extract text from it.
    :param image_path: Path to the input image
    """
    
    # Load the image
    image = cv2.imread(image_path)  # Read the image from the given path
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    
    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)  # Detect edges using Canny
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through contours to find a rectangular region
    plate = None  # Variable to store the number plate region
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Check for rectangular shape
            x, y, w, h = cv2.boundingRect(contour)
            plate = gray[y:y+h, x:x+w]  # Crop the potential number plate
            break  # Stop after finding the first rectangle
    
    if plate is None:
        print("No number plate detected.")
        return
    
    # Use EasyOCR to extract text
    reader = easyocr.Reader(['en'])  # Load the OCR model for English
    result = reader.readtext(plate)  # Extract text from the detected region
    
    # Print detected text
    for res in result:
        print("Detected Number Plate:", res[1])  # Display extracted text
    
    # Show the detected plate
    cv2.imshow('Number Plate', plate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_number_plate('car.jpg')  # Provide the path to the input image
