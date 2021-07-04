from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class SentenceView(TemplateView):
    template_name = "sentence.html"


class WordView(TemplateView):
    template_name = "word.html"



