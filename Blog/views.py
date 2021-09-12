from operator import attrgetter
from django.db.models import Q
from django.shortcuts import render, redirect
from Dashboard.models import Blog, User
from Blog.models import Comment


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
    context3 = Blog.objects.order_by('Genre').distinct('Genre')
    context4 = Comment.objects.filter(Blog=bid)
    both = {'related': context2, 'details': context, 'cats': context3, 'comments': context4}

    if request.method == 'POST':
        if request.POST.get('names') and request.POST.get('comment'):
            savecomment = Comment()
            savecomment.Names = request.POST['names']
            savecomment.Feedback = request.POST['comment']
            savecomment.Blog = context
            savecomment.save()
            print('Comment sent successfully!')
        else:
            print('Something went wrong')
            return redirect('blog')
    return render(request, "Blog/blog-details.html", both)


def blogsearch(query=None):
    queryset = []
    queries = query.split(", ")
    for q in queries:
        posts = Blog.objects.filter(
            Q(Title__icontains=q) |
            Q(Description__icontains=q)|
            Q(Genre__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))
