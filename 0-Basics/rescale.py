import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# def changeRes(capture, width, height):
#     # Live Video
#     capture.set(3, width)
#     capture.set(4, height)


# Resize Photo
# resized_image = rescaleFrame(cv.imread('Resources/Photos/cat.jpg'))
# cv.imshow('Image', resized_image)
# cv.waitKey(0)

# Resize Videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, scale=0.2)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()
