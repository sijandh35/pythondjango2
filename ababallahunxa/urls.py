'''    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    '''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('travello.urls')),
    path('admin/', admin.site.urls),
    path('', include('Accounts.urls')),
    path('',include('core.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


