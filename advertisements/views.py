from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from models import Users, Posts, Types, Userpost, Messages
from django.core.files.storage import FileSystemStorage
from django.db.models import ProtectedError
import json

def index(request):
    try:
        posts = Posts.objects.all().order_by('-id')[:5]
        return render(request, 'advertisements/index.html',{'posts':posts})
    except Posts.DoesNotExist:
        print('Invalid Data')

def home(request):
    return render(request, 'advertisements/home.html')

def contact(request):
    
    if request.POST:
        try:
            message = Messages(name=request.POST.get('name', None),email=request.POST.get('email', None),message=request.POST.get('message', None),subject=request.POST.get('subject', None))
            message.save()
            return render(request, 'advertisements/contact.html',{"success":True})
        except Messages.DoesNotExist:
            return render(request, 'advertisements/contact.html',{"error":True})
    else:
        return render(request, 'advertisements/contact.html')

def login(request):
    response = HttpResponse("hello")
    if request.POST:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        try:
            user = Users.objects.get(email__iexact=email,password__iexact=password)
            request.session['user_id'] = user.id
            request.session['user_type'] = user.usertype
            request.session['address'] = user.address
            if request.POST.get('remember', None):
                response.set_cookie('email', email)
                response.set_cookie('password', password)
                response.set_cookie('remember', 1)
            else:
                response.delete_cookie('email')
                response.delete_cookie('password')
                response.delete_cookie('remember')
            request.session['email'] = email
            return HttpResponseRedirect("/")
        except Users.DoesNotExist:
            return render(request, 'advertisements/index.html',{"error": "Invalid Email Id or Password."})
    else:
        return render(request, 'advertisements/index.html')

def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return HttpResponseRedirect("/")

def register(request):
    userData = request.POST
    user = Users(firstname=userData['firstname'],lastname=userData['lastname'],email=userData['email'],password=userData['password'],gender=userData['gender'],usertype=userData['usertype'],address=userData['address'])
    user.save()
    return HttpResponseRedirect("/")
    
def checkuser(request):
    email = request.GET.get('email', None)
    user_exists = Users.objects.filter(email__iexact=email).exists()
    if user_exists == False:
        return HttpResponse('true')
    else:
        return HttpResponse('false')

def post(request):
    if 'user_id' in request.session:
        posts = Posts.objects.filter(created_by__id = request.session['user_id'])
        return render(request, 'advertisements/post.html',{'posts':posts})
    else:
        return render(request, 'advertisements/index.html')

def deletepost(request):
    if 'user_id' in request.session:
        post_id = request.GET.get('id', None)
        try:
            Posts.objects.filter(pk = post_id).delete()
            Userpost.objects.filter(post = post_id).delete()
            return HttpResponse('true')
        except ProtectedError:
            return HttpResponse('false')
    else:
        return render(request, 'advertisements/index.html')

def addpost(request):
    if 'user_id' in request.session:
        types = Types.objects.all()
        if request.POST:
            user = Users.objects.get(pk=request.session['user_id'])
            job_type = Types.objects.get(pk=request.POST.get('job_type', None))
            post = Posts(title=request.POST.get('title', None),description=request.POST.get('description', None),address=request.POST.get('address', None),created_by=user,job_type=job_type,organization=request.POST.get('organization', None),hourly_rate=request.POST.get('hourly_rate', None))
            post.save()
            return HttpResponseRedirect("/post/")
        return render(request, 'advertisements/addpost.html',{"types":types})
    else:
        return render(request, 'advertisements/index.html')

def updatepost(request, post_id):
    if 'user_id' in request.session:
        types = Types.objects.all()
        post = Posts.objects.get(pk = post_id)
        if request.POST:
            job_type = Types.objects.get(pk=request.POST.get('job_type', None))
            post.title = request.POST.get('title', None)
            post.description = request.POST.get('description', None)
            post.address = request.POST.get('address', None)
            post.job_type = job_type
            post.hourly_rate = request.POST.get('hourly_rate', None)
            post.organization = request.POST.get('organization', None)
            post.save()
            return HttpResponseRedirect("/post/")
        return render(request, 'advertisements/updatepost.html',{"types":types,"post":post})
    else:
        return render(request, 'advertisements/index.html')

def viewpost(request, post_id):
    if 'user_id' in request.session:
        post = Posts.objects.get(pk = post_id)
        userpost = Userpost.objects.filter(post=post)
        return render(request, 'advertisements/viewpost.html',{"post":post,'userpost':userpost})
    else:
        return render(request, 'advertisements/index.html')

def profile(request):
    if 'user_id' in request.session:
        user = Users.objects.get(pk=request.session['user_id'])
        return render(request, 'advertisements/profile.html',{'user':user})
    else:
        return render(request, 'advertisements/index.html')

def update(request):
    if 'user_id' in request.session:
        user = Users.objects.get(pk = request.session['user_id'])
        if request.POST:
            uploaded_file_url = ''
            if request.FILES:
                pic = request.FILES['pic']
                fs = FileSystemStorage()
                filename = fs.save('static/upload/'+pic.name, pic)
                uploaded_file_url = fs.url(filename)
                user.uploadedImage = uploaded_file_url
            user.firstname = request.POST.get('firstname', None)
            user.lastname = request.POST.get('lastname', None)
            user.gender = request.POST.get('gender', None)
            user.address = request.POST.get('address', None)
            user.save()
            if request.POST.get('password', None) != '':
                user.password = request.POST.get('password', None)
            return render(request, 'advertisements/profile.html',{'user':user})
        return render(request, 'advertisements/update.html',{'user':user})
    else:
        return render(request, 'advertisements/index.html')

def search(request):
    try:
        term = request.GET.get('term', None)
        posts = Posts.objects.filter(title__icontains=term).order_by('-id')
        updatedData = {}
        records = []
        for post in posts:
            records.append(post.title)
        updatedData = json.dumps(records)
        return HttpResponse(updatedData, content_type='application/json')
    except Posts.DoesNotExist:
        print('Invalid Data')

def searchjob(request):
    try:
        search = request.GET.get('search', '')
        type_id = request.GET.get('type', '')
        if type_id:
            getType = Types.objects.get(pk = type_id)
            posts = Posts.objects.filter(job_type=getType,title__icontains=search).order_by('-id')
        else:
            posts = Posts.objects.filter(title__icontains=search).order_by('-id')
        types = Types.objects.all()
        return render(request, 'advertisements/search.html',{'posts':posts,'types':types,'search':search})
    except Posts.DoesNotExist:
        print('Invalid Data')
    
def getpost(request, post_id):
    try:
        already = 'false'
        post = Posts.objects.get(pk = post_id)
        if 'user_id' in request.session:
            user = Users.objects.get(pk = request.session['user_id'])
            userpost = Userpost.objects.filter(post=post,user=user).exists()
            if userpost:
                already = 'true'
        if request.POST:
            uploaded_file_url = ''
            if request.FILES:
                resume = request.FILES['resume']
                fs = FileSystemStorage()
                filename = fs.save('static/resume/'+resume.name, resume)
                uploaded_file_url = fs.url(filename)
            addPost = Userpost(cover_letter=request.POST.get('cover_letter', None), post=post, user=user, resume=uploaded_file_url)
            addPost.save()
            return render(request, 'advertisements/index.html',{"success": "You Have Successfully Applied to Job."})
        return render(request, 'advertisements/getpost.html',{"post":post,"already":already})
    except Posts.DoesNotExist:
        return render(request, 'advertisements/index.html')