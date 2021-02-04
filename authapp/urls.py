from django.urls import path

from authapp.views import UserRegisterView, UserAccountUpdateView, UserAccountStatisticView, UserAccountMyArticles

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('account/', UserAccountStatisticView.as_view(), name='user_statistic'),
    path('account/update/', UserAccountUpdateView.as_view(), name='user_update_data'),
    path('account/articles/', UserAccountMyArticles.as_view(), name='user_articles'),
]
