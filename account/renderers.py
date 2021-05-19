import json
from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):

    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        email = data.get('email', None)
        name = data.get('name', None)

        return json.dumps(data)

