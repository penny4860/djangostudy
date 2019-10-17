import numpy as np
import urllib
import cv2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .serializers import ResponseSerializer, ResponseInfo


# start off with defining a function to detect the URL requested which has the image for facial recognition
@csrf_exempt
def get_imgsize(request):

    ## between GET or POST, we go with Post request and check for https
    if request.method == "POST":
        
        img_file = request.POST.get("file", None)
        if img_file is not None:
            image = read_image(path=img_file)
        else: # URL is provided by the user
            url_provided = request.POST.get("url", None)
            if url_provided is None:
                serializer = ResponseSerializer(ResponseInfo())
                return JsonResponse(serializer.data)
            image = read_image(url = url_provided)
        h, w, _ = image.shape
        serializer = ResponseSerializer(ResponseInfo(height=h, width=w))
        return JsonResponse(serializer.data)
    elif request.method == "GET":
        serializer = ResponseSerializer(ResponseInfo())
        return JsonResponse(serializer.data)
        

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

