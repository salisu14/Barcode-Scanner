import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
lastCode = ""

while True:

    _, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale

    barcodes = decode(gray)    

    # For every barcode found
    for barcode in barcodes:
        # Get barcode coordinates
        (x,y,w,h) = barcode.rect
        # Draw a rectangle around it
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        # Get the data
        barcodeType = barcode.type
        barcodeData = barcode.data.decode("utf-8")
        # Draw the data over the rectangle
        dataText = f"Data: {barcodeData}"
        dataType = f"Type: {barcodeType}"
        cv2.putText(frame, dataText, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        cv2.putText(frame, dataType, (x,y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

        # Update lastCode if necessary
        if barcodeData != lastCode:
            lastCode = barcodeData
            print("READ: " + barcodeData)

    cv2.imshow("original", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()