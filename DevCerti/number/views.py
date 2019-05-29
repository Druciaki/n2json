from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse

from number.models import CertiNumber
import re

class Numberify(TemplateView):

    def get(self, request, **kwargs):
        data = request.path
        data = re.sub("\D", "", data)
        value = CertiNumber(data).get_string_portuguese(kwargs.get('sign'))
        return JsonResponse({'extenso':value})
        