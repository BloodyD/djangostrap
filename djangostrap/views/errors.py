from django import http
from django.template import Context, RequestContext, loader
from django.views.decorators.csrf import requires_csrf_token

from utils import default_template_dict

def handler(template_name, context, response_cls):
  return response_cls(loader.get_template(template_name).render(context))

@requires_csrf_token
def handler400(request):
  return handler(
      "400.html",
      Context(default_template_dict(request)),
      http.HttpResponseBadRequest)

@requires_csrf_token
def handler403(request):
  return handler(
      "403.html",
      RequestContext(request, default_template_dict(request)),
      http.HttpResponseForbidden)

@requires_csrf_token
def handler404(request):
  return handler(
      "404.html",
      RequestContext(request, default_template_dict(request)),
      http.HttpResponseNotFound)


@requires_csrf_token
def handler500(request):
  return handler(
      "500.html",
      Context(default_template_dict(request)),
      http.HttpResponseServerError)
