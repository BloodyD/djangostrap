# coding=utf-8
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from djangostrap import settings
from utils import default_template_dict


#Source: http://lincolnloop.com/blog/2008/may/10/getting-requestcontext-your-templates/
def render_to(template_name, title = ""):
  def renderer(func):
    def wrapper(request, *args, **kw):
      output = func(request, *args, **kw)
      if not isinstance(output, dict): return output

      return render_to_response(
        template_name,
        default_template_dict(request, output, title),
        context_instance=RequestContext(request))
    return wrapper
  return renderer
