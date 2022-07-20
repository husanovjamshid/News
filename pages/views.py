from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Category, RightNews, CenterNews, Contact
import datetime
# Create your views here.

def index(request):
    cat = Category.objects.all()
    posts = RightNews.objects.all().order_by('-id')[:6]
    centerPost = CenterNews.objects.all().order_by('-view_count')[:6]

    cDate =  datetime.date.today()
    fDate = cDate.strftime("%b %d")



    return render(request, 'index.html', context={
        'cat':cat,
        'posts':posts,
        'cDate':cDate,
        'fDate':fDate,
        'centerPost':centerPost
    })

def single_blog(request, id):
    cDate = datetime.date.today()
    fDate = cDate.strftime("%b %d")

    try:
        posts = RightNews.objects.get(id=id)
    except:
        posts = CenterNews.objects.get(id=id)
    posts.view_count += 1
    posts.save()
    return render(request, 'single-blog.html', context={
        'posts': posts,
        'fDate':fDate,
        # 'centerPost':centerPost

    })


def category(request):
    cat = Category.objects.all()
    posts = RightNews.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # posts = CenterNews.objects.all()
    return render(request, 'categori.html', context={
        'cat': cat,
        'posts':posts
    })

def contact(request):
    contact = Contact()

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()


            messages.success(request, 'Xabaringiz muvaffaqqiyatli yetkazildi!!!')
        except:
            messages.error(request, 'Xabaringiz yuborilmadi iltimos ma`lumotlarni to`liq kiriting!!!')


    return render(request, 'contact.html',
                  context={

                  }
                  )


def blog(request):
    posts = RightNews.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    cat = Category.objects.all()

    return render(request, 'blog.html', context={
        'posts': posts,
        'cat': cat,
    })
