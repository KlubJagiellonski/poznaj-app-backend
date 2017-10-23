from django.views.generic import TemplateView


class TeamView(TemplateView):
    template_name = 'mobile/team.html'


class PartnersView(TemplateView):
    template_name = 'mobile/partners.html'
