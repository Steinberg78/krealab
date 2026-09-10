from django.test import TestCase

from .models import ContactRequest


class ContactRequestModelTest(TestCase):
    def test_contact_request_can_be_saved(self):
        lead = ContactRequest.objects.create(
            name='Awa Diop',
            email='awa@example.com',
            service='Création de site web',
            message='Je souhaite un site moderne.'
        )

        self.assertEqual(lead.name, 'Awa Diop')
        self.assertEqual(ContactRequest.objects.count(), 1)
