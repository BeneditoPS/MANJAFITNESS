from xhtml2pdf import pisa
from django.template.loader import render_to_string, get_template
from io import BytesIO
from django.http import HttpResponse

class GerarPDFMixin:
    def render_to_pdf(self, template_end, context_dict={}):
        template = get_template(template_end)
        html = template.render(context_dict)
        result = BytesIO()
  
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8"), result))
        return HttpResponse(result.getvalue(),
                                content_type = 'application/pdf')
  