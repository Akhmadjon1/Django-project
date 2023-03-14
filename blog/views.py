from django.shortcuts import render

posts = [
    {
        'author': 'Akhmadjon',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'march 15, 2023'
    },
    {
        'author': 'Aki',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'march 16, 2023'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
