from django.core.context_processors import csrf
from utils.decorators import render_to



@render_to("index.html", "Index")
def index(request):
  output = csrf(request)
  output["title"] = "Index"
  return output



from .errors import *