import vanilla


class Homepage(vanilla.TemplateView):
    template_name = 'pages/index.html'


class Rules(vanilla.TemplateView):
    template_name = 'pages/rules.html'


class Prizes(vanilla.TemplateView):
    template_name = 'pages/prizes.html'


class CodeOfConduct(vanilla.TemplateView):
    template_name = 'pages/coc.html'


class Error404(vanilla.TemplateView):
    template_name = '404.html'

    def render_to_response(self, context):
        response = super(Error404, self).render_to_response(context)
        response.status_code = 404
        response.reason_phrase = 'Not Found'
        return response


class Error500(vanilla.TemplateView):
    template_name = '500.html'

    def render_to_response(self, context):
        response = super(Error500, self).render_to_response(context)
        response.status_code = 500
        response.reason_phrase = 'Internal Server Error'
        return response
