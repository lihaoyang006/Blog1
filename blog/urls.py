from django.conf.urls import url, include
from blog.views import index, show
from blog.admin import blog_admin

urlpatterns = [
    url(r'^index/', index),
    url(r'^show/(\d+)/', show),
    url(r'^admin/', include(blog_admin.urls)),
]