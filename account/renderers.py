import json
from rest_framework.renderers import JSONRenderer
from collections import OrderedDict


class UserJSONRenderer(JSONRenderer):

    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        email = data.get('email', None)
        name = data.get('name', None)

        # if email is not None and name is not None:
        #     finaldata.pop('email')
        #     finaldata.pop('name')
        #     return json.dumps(finaldata)

        return json.dumps(data)

