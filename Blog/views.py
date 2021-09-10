from operator import attrgetter
from django.db.models import Q
from django.shortcuts import render
from Dashboard.models import Blog, User


# Create your views here.


def blog(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    blogs = sorted(blogsearch(query), key=attrgetter('created_at'), reverse=True)
    context['blogs'] = blogs
    return render(request, "Blog/blog.html", context)


def blogdetails(request, bid):
    context = Blog.objects.get(id=bid)
    Ge = context.Genre
    context2 = Blog.objects.filter(Genre=Ge).exclude(id=bid)
    both = {'related': context2, 'details': context}
    return render(request, "Blog/blog-details.html", both)


def blogsearch(query=None):
    queryset = []
    queries = query.split(", ")
    for q in queries:
        posts = Blog.objects.filter(
            Q(Title__icontains=q) |
            Q(Description__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))
