from django.utils.timezone import now as django_now
from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_render_time = django_now()
        print(f'we start rendering at {request.start_render_time}')
        # request.fake_context = dict(data='test')

    def process_response(self, request, response):
        finish_time = django_now()
        print(f'we finish rendering at {finish_time}')
        result = finish_time - request.start_render_time
        print(f'result {result.seconds}')
        return response
