from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Hamza Majeed',
        'title': 'Tech Blog 1',
        'content': 'First post content',
        'date_posted': 'February 01, 2021'
    },
    {
        'author': 'Hamza Majeed',
        'title': 'Tech Blog 2',
        'content': 'Second post content',
        'date_posted': 'February 02, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})