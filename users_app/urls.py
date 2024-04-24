from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('',views.listProfile,name='list'),
    path('update/<int:profile_id>', views.updateProfile, name='update'),
    path('details/<int:profile_id>', views.detailsView, name='details'),
path('deleteview/<int:profile_id>',views.deleteView,name='delete'),



path('workexperience/create/', views.create_work_experience, name='create_work_experience'),
    # path('workexperience/<int:workexperience_id>/', views.work_details_view, name='work_experience_details'),
    path('list_work/',views.list_work_experience, name='list_work'),



    path('create_education/', views.create_education, name='create_education'),
    path('list_edu/', views.list_education, name='list_edu'),

    path('project_list/', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),

    path('list_certificate/',views.certification_list, name='list_certificate')

]
