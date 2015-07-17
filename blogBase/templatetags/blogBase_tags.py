from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import AsTag
from django import template
from blogBase.models import Comment

register = template.Library()

class Dummy(AsTag):
    name = 'getcomments'
    options = Options(
        'for',
        Argument('post', resolve=True, required=False),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context, post):
        return Comment.objects.filter(post_id= post.id)

register.tag(Dummy)
