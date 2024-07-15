from django.views.generic import TemplateView




# Create Home Class

class HomeView(TemplateView):
    template_name = 'home.html'
