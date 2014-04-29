from django.core.context_processors import csrf
from utils.decorators import render_to



@render_to("index.html")
def index(request):
  output = csrf(request)
  output["title"] = "Index"
  return output