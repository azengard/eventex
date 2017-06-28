from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Carlos Henrique',
            cpf='12345678901',
            email='carlos@henrique.net',
            phone='11-995373282'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.uniqueId))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf,
                    self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        invalid_route = '00000000-0000-0000-0000-000000000000'
        resp = self.client.get(r('subscriptions:detail', invalid_route))
        self.assertEqual(404, resp.status_code)