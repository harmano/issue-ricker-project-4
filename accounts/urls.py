    
from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, home, cart, get_posts, post_detail, create_or_edit_post, features
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^home/', get_posts, name="home"),
    url(r'^cart/', cart, name="cart"),
    url(r'^getpost/', get_posts, name="get_posts"),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^features/', features, name="features"),
    
]