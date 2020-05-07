from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView

from bookmark_app.models import Bookmark


class BookmarkList(ListView):
    model = Bookmark
    template_name = 'bookmark/list.html'


class AddBookmark(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'bookmark/add.html', {})

    def post(self, request):
        title = request.POST.get('title')
        url = request.POST.get('url')

        Bookmark.objects.create(
            title=title,
            url=url
        )

        return redirect('/')


class EditBookmark(View):
    def get(self, request, *args, **kwargs):

        link = Bookmark.objects.get(id=kwargs['bookmark'])
        return render(request, 'bookmark/edit.html', {'link': link})

    def post(self, request, *args, **kwargs):
        link = Bookmark.objects.get(id=kwargs['bookmark'])
        link.title = request.POST.get('title')
        link.url = request.POST.get('url')
        link.save()

        return redirect('/')


class DeleteBookmark(View):
    def get(self, request, *args, **kwargs):

        link = Bookmark.objects.get(id=kwargs['bookmark'])
        return render(request, 'bookmark/delete.html', {'link': link})

    def post(self, request, *args, **kwargs):
        link = Bookmark.objects.get(id=kwargs['bookmark'])
        link.delete()

        return redirect('/')

