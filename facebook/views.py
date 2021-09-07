from django.shortcuts import render, redirect
from facebook.models import Article, Page, Comment

# Create your views here.
def page_new(request):
    if request.method == 'POST':
        if request.POST['master'] != '' and request.POST['name'] != '' and request.POST['category'] != '' and request.POST['content'] != '':
            new_page = Page.objects.create(
                master = request.POST['master'],
                name = request.POST['name'],
                category = request.POST['category'],
                text = request.POST['content']
            )
            return redirect('/pages/')
    return render(request, 'new.html')

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')
    
    return render(request, 'remove_page.html', {'new_page': page})

def edit_page(request, pk):
    page =  Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.category = request.POST['category']
        page.text = request.POST['content']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'new_page' : page})



def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = request.POST['content'] + ' - 추신 : 감사힙니다.',
                password = request.POST['password']
            )
        return redirect(f'/feed/{ new_article.pk }')
    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail/')

    return render(request, 'remove_feed.html', {'feed': article })

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')

    return render(request, 'edit_feed.html', {'feed': article })


def newsfeed(request):
    article = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles' : article})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{ article.pk }')
    return render(request, 'detail_feed.html', {'feed' : article})


def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages' : pages})


def play(request):
    return  render(request, 'play.html')


count = 0
def play2(request):
    choidogeun = '최도근'
    age = 20
    global count # 바깥영역의 변수를 사용할 떄 global
    count += 1 # 접속할 때마다 방문자 1 증가

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일 작성']
    return render(request, 'play2.html', {'name' : choidogeun, 'diary': diary, 'cnt' : count , 'age' : status})


def profile(request):
    return render(request, 'profile.html')

event_count = 0
def event(request):
    global event_count
    event_count += 1

    if event_count == 7:
        status = '당첨!'
    else:
        status = '꽝...'
        
    return render(request, 'event.html', {'cnt': event_count, 'event': status})



def fail(request):
    return render(request, 'fail.html')


def help(request):
    return render(request, 'help.html')


def warn(request):
    return render(request, 'warn.html')