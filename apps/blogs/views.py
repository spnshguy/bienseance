from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View

from apps.blogs.models import Blog


class BlogList(View):
    def get(self, request):
        today = now()
        blogs = Blog.objects.translated(publication_date__lte=today).filter(is_active=True).order_by('-translations__publication_date')
        paginator = Paginator(blogs, 6)
        page = request.GET.get('page')

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        index = blogs.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 2 if index <= max_index - 2 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        return render(request, 'blogs/list.html', dict(
            blogs=blogs,
            page_range=page_range
        ))


class BlogSingle(View):
    def get(self, request, slug):
        today = now()
        blog = Blog.objects.translated(slug=slug).first()
        related_blogs = Blog.objects.translated(publication_date__lte=today).exclude(id=blog.id).filter(is_active=True)[:3]

        return render(request, 'blogs/single.html', {
            'blog': blog,
            'related_blogs': related_blogs,
        })
