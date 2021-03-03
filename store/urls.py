
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add',views.add,name='add'),
    path('updateView/<int:myid>',views.updateView,name='updateView'),
    path('update/<int:myid>',views.update,name='update'),
    path('deleted/<int:myid>',views.deleted,name='delete'),
    path('query',views.query,name='query'),
    path('saveit/<int:myid>',views.saveItem,name='saveItem'),
    path('displaysaved',views.displaySavedItems,name='displaySavedItems'),
    path('deletesaved/<int:myid>',views.deleteSavedItems,name='deleteSavedItems'),
    path('login',views.handleLogin,name='handleLogin'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('logout',views.handleLogout,name='handleLogout')
]