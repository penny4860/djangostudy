import numpy as np
import urllib
import cv2

from .serializers import ResponseSerializer, ResponseInfo
from rest_framework.response import Response


# start off with defining a function to detect the URL requested which has the image for facial recognition

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def get_imgsize(request):

    ## between GET or POST, we go with Post request and check for https
    if request.method == "POST":
        
        img_file = request.data["file"]
        if img_file is not None:
            image = read_image(path=img_file)
        else: # URL is provided by the user
            url_provided = request.data["url"]
            if url_provided is None:
                response_info = ResponseInfo()
            image = read_image(url = url_provided)
        h, w, _ = image.shape
        response_info = ResponseInfo(height=h, width=w)
    else:
        response_info = ResponseInfo()

    serializer = ResponseSerializer(response_info)
    return Response(serializer.data)
        

def read_image(path=None, stream=None, url=None):
    def to_img(data_temp):
        image = np.asarray(bytearray(data_temp), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
    if path is not None:
        image = cv2.imread(path)
    elif url is not None:
        response = urllib.request.urlopen(url)
        data_temp = response.read()
        image = to_img(data_temp)
    elif stream is not None:
        #implying image is now streaming
        data_temp = stream.read()
        image = to_img(data_temp)
    return image

