
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, CustomLogoutView, RegisterPage, TaskReorder


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path("", TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]


# from django.urls import path
# from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, TaskReorder, RegisterPage, CustomLogoutView

# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('register/', RegisterPage.as_view(), name='register'),
#     path('', TaskList.as_view(), name='tasks'),
#     path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
#     path('task-create/', TaskCreate.as_view(), name='task-create'),
#     path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
#     path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
#     path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
#     path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),
# ]
