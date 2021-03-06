"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from products.views import all_products2
from products.views import all_products
from products import urls as urls_products
from products.views import product_review, add_review
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static
from django.views.generic import RedirectView
from posts import urls as urls_posts
from posts.views import get_posts
from django.views.static import serve
from .settings import MEDIA_ROOT
from home.views import about
from contact.views import contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^products/', include('products.urls')),
    url(r"^products_list/$", all_products2, name="all_products2"),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^posts/', include('posts.urls')),
    url(r'^posts/', include(urls_posts)),
    url(r"^posts$", get_posts, name="get_posts"),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url('contact_page/', contact, name='contact'),
    url('about/', about, name='about'),
]

