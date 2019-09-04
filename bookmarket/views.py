from django.shortcuts import render

posts = [
    {
        'author': 'Me',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'September 3, 2019'
    },
    {
        'author': 'You',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'September 4, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'bookmarket/home.html', context)


def about(request):
    return render(request, 'bookmarket/about.html', {'title': 'About'})
