"""gantt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from controll import views as control_views
from django.conf import settings
import os
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', control_views.index, name="index"),
    url(r'^projects/(?P<project_name>[^/]+)/$', control_views.show_projects, name="projects"),
    url(r'^add_project/$', control_views.add_project, name='add_project'),
    url(r'^getprojectdata/$', control_views.get_project_data,  name='get_project_data'),
    url(r'^saveproject/$', control_views.save_project, name='save_project'),

]
