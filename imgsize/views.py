import numpy as np
import urllib
import cv2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# start off with defining a function to detect the URL requested which has the image for facial recognition
@csrf_exempt
def get_imgsize(request):
    #default value set to be false
    default = {"safely_executed": False} #because no detection yet

    ## between GET or POST, we go with Post request and check for https
    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            image = read_image(stream = request.FILES["image"])

        else: # URL is provided by the user
            url_provided = request.POST.get("url", None)
            if url_provided is None:
                default["error_value"] = "There is no URL Provided"
                return JsonResponse(default)
            image = read_image(url = url_provided)
        h, w, _ = image.shape
        default.update({"height": h, "width": w, "safely_executed": True })
    return JsonResponse(default)


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

