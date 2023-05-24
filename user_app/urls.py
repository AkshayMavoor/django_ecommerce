from django.urls import path
from .views import Dashboard, Error403,Error404,Manage_user, UpdateUser , Profile



urlpatterns = [
    # path('', Login.as_view(), name="login"),
    # path('register/', Register.as_view(), name="register"),
    # path('register/', home_view, name="register"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('manage_user/', Manage_user.as_view(), name="manage_user"),
    path('update_user/<int:id>/', UpdateUser.as_view(), name="update_user"),
    path('404/', Error404.as_view(), name="404"),
    path('403/', Error403.as_view(), name="403"),
    path('profile/' , Profile.as_view(), name="profile"),
    
    # path("logout/", LogoutView.as_view(), name="logout")
]