
def default_template_dict(request, output = {}, title = ""):
  from djangostrap import settings
  output.update({
    "settings": settings,
    "request": request,
    "title": title,
    })
  return output
