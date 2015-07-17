import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from blog import settings
from models import Post, Comment
from forms import PostForm, CommentForm
from registration.backends.simple.views import RegistrationView as SimpleRegistrationView

class RegistrationView(SimpleRegistrationView):
    def get_success_url(self, request, user):
        return (settings.LOGIN_REDIRECT_URL, (), {})

class PostsListView(ListView):
    model = Post

def view_post(request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(request.path)
        return render_to_response('blogBase/post_detail.html',
                                  {
                                      'post': post,
                                      'form': form,
                                  },
                                  context_instance=RequestContext(request))

        # if request.method == 'POST':
        #     comment_text = request.POST.get('comment')
        #     response_data = {}
        #
        #     comment = Comment(author=request.user, post=post, content=comment_text)
        #     comment.save()
        #
        #     response_data['result'] = 'Create post successful!'
        #     response_data['postpk'] = comment.pk
        #     response_data['text'] = comment.content
        #     response_data['author'] = comment.author.username
        #
        #     return HttpResponse(
        #         json.dumps(response_data),
        #         content_type="application/json"
        #     )
        # else:
        #     return HttpResponse(
        #         json.dumps({"nothing to see": "this isn't happening"}),
        #         content_type="application/json"
        #     )
        #


# @user_passes_test((lambda u: u.is_superuser), login_url="/blog/", redirect_field_name=None)
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('blogBase/add_post.html',
                              { 'form': form },
                              context_instance=RequestContext(request))
def user_view(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('blogBase/user_view.html',
                                  {
                                      'user': user,
                                  },
                                  context_instance=RequestContext(request))