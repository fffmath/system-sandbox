from django.urls.base import reverse_lazy
from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import *

from . import views
from .forms import MyPasswordResetForm

urlpatterns = [
    path('', views.index, name='index'),
    path('login',
        LoginView.as_view(
            template_name='polls/login.html',
            redirect_authenticated_user=True
        ), 
        name='login'),
    path('logout',
        LogoutView.as_view(
            template_name='polls/logout.html'),
        name='logout'),
    path('userlist', views.StudentListView.as_view(), name='userlist'),
    url(r'^register/$', views.register, name='register'),
    url(r'^editprofile/$', views.edit_profile_view, name='editprofile'),
    url(r'^editresume/$', views.edit_resume_view, name='editresume'),
    path('anounce/index/', views.AnounceListView.as_view(), name='anounce_index'),
    path('anounce/latest<int:num>/', views.AnounceLatestListView, name='anounce_list'),
    path('anounce/<int:pk>/', views.AnounceDetailView, name='anounce_detail'),
    #密码重置链接
    url(
        r'^password_reset/$', 
        PasswordResetView.as_view(
            form_class=MyPasswordResetForm,
            template_name = 'polls/passwdreset.html',
            email_template_name = 'polls/password_reset_email.html',
            subject_template_name = 'polls/password_reset_subject.txt',
            success_url = reverse_lazy('password_reset_done')
        ),
        name='password_reset'
    ),
    #密码重置邮件发送完成后的页面
    url(
        r'^password_reset/done/$', 
        PasswordResetDoneView.as_view(template_name='polls/password_reset_done.html'), 
        name='password_reset_done'
    ),
    #用户通过邮箱打开的重置密码页面
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$', 
        PasswordResetConfirmView.as_view(
            template_name='polls/password_reset_confirm.html',
            success_url = reverse_lazy('password_reset_complete')
        ),
        name='password_reset_confirm',
    ),
    #密码重置完成后跳转的页面
    url(
        r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='polls/password_reset_complete.html'), 
        name='password_reset_complete'
    ),
]
