
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, SavedItems
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    items= Product.objects.all()
    context={'items':items}
    return render(request,'store/home.html',context)

def add(request):
    if request.method == 'POST':
        name= request.POST['name']        
        quantity= request.POST['qty']        
        status= request.POST['status']        
        date= request.POST['date']  

        if len(name)<2 :
            messages.error(request,"Please fill the form correctly")
        else :
            messages.success(request," Item has been added successfully ")
        product = Product(item_name=name,item_quantity=quantity,item_status=status,pub_date=date)
        product.save()
    return render(request,'store/add.html')

def updateView(request,myid):
    item= Product.objects.filter(item_id=myid).first()
    context={'item':item}
    return render(request,'store/updateView.html',context)

def update(request,myid):
    if request.method == 'POST':
        item= Product.objects.filter(item_id=myid).first()
        name= request.POST['name']        
        quantity= request.POST['qty']        
        status= request.POST['status']        
        date= request.POST['date'] 
        item.item_name= name
        item.item_quantity=quantity
        item.item_status= status
        item.pub_date=date
        item.save()
        return redirect('home')
    
def deleted(request,myid):
    item=Product.objects.filter(item_id=myid).first()
    item.delete()
    return redirect('home')

def query(request):
    if request.method== 'POST':
        rdate= request.POST['query']
        items=Product.objects.filter(pub_date=rdate)
        if items.count()==0:
            messages.error(request,"No search results found. Please refine your query")
            return render(request,'store/query.html')
        else :
            context={'items':items}
            messages.success(request,"Your Search Results are : ")
            return render(request,'store/query.html',context)

def saveItem(request,myid):
    item= Product.objects.filter(item_id=myid).first()
    flag= item.is_saved
    if flag== True:
        messages.error(request,"This item is already added in Saved Items List. Try to add something New !")
        return redirect('home')
    else:
        item.is_saved= True
        item.save()
        product= SavedItems(item_name=item.item_name,item_quantity=item.item_quantity,item_status=item.item_status,pub_date=item.pub_date)
        product.save()
        messages.success(request,"Selected item has been successfully added to your Saved Items List!")
        return redirect('home')
    
def displaySavedItems(request):
    sitems= SavedItems.objects.all()
    
    if sitems.count()==0:
        messages.error(request,"Your Saved Items List is Empty !")
        return render(request,'store/savedList.html')
    else:
        context= {'sitems':sitems}
        return render(request,'store/savedList.html',context)

def deleteSavedItems(request,myid):
    sitem=SavedItems.objects.filter(item_id=myid).first()
    sitem.delete()
    return redirect('displaySavedItems')
    
      
        

# Authentication APIs
def handleSignup(request):
    if request.method == "POST":
        #get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for eroneous inputs
        if len(username)>10:
            messages.error(request," Username must be under 10 character!")
            return redirect('home')
        if not username.isalnum():
            messages.error(request," Username should only contain alphanumeric characters!")
            return redirect('home')

        if(pass1 != pass2):
            messages.error(request,"Your password doesn't match!")
            return redirect('home')

        #create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Grocery Account has been successfully created!")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('home')


    return HttpResponse("404 - Not found")

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out!")
    return redirect('home')