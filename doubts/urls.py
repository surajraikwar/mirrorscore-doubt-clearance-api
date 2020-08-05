from django.urls import path, include
from rest_framework import routers
from .views import index, ListQuestionsView

app_name='doubts'

router = routers.DefaultRouter()
router.register(r'questions', ListQuestionsView)

urlpatterns = [
    path('',index,name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''
urlpatterns = [
    path('',index,name='index'),
    path('questions/', ListQuestionsView.as_view(), name="questions")
]
'''
