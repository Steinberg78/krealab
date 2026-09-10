from django.urls import path
from .views import (
    automation,
    community,
    contact,
    contenu,
    home,
    motion,
    publicite,
    site_web,
)

urlpatterns = [
    path('', home, name='home'),
    path('sites-web/', site_web, name='site_web'),
    path('community-management/', community, name='community'),
    path('motion-design/', motion, name='motion'),
    path('redaction-contenu/', contenu, name='contenu'),
    path('publicite-en-ligne/', publicite, name='publicite'),
    path('automatisation-workflow/', automation, name='automation'),
    path('contact/', contact, name='contact'),
]
