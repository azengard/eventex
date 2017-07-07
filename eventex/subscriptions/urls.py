from django.conf.urls import url

from eventex.subscriptions.views import new, detail


uuid_pattern = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<slug>{})/$'.format(uuid_pattern), detail, name='detail'),
]