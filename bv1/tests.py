from django.test import TestCase
from django.urls import reverse
from .models import SignUP

class TestimonialFormTests(TestCase):
    def test_get_testimonial_page(self):
        response = self.client.get(reverse('testimonial_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bv1/testimonial.html')

    def test_post_valid_email(self):
        response = self.client.post(reverse('testimonial_url'), {
            'email': 'test@example.com'
        })
        # Redirect bo'lishi kerak, shuning uchun 302
        self.assertEqual(response.status_code, 302)
        self.assertEqual(SignUP.objects.count(), 1)
        self.assertEqual(SignUP.objects.first().email, 'test@example.com')

    def test_post_invalid_email(self):
        response = self.client.post(reverse('testimonial_url'), {
            'email': ''
        })
        self.assertEqual(response.status_code, 200)  # Form xato bo‘lsa sahifa qayta render bo‘ladi
        self.assertContains(response, 'This field is required.')  # Error matni formdan olinadi
        self.assertEqual(SignUP.objects.count(), 0)  # DBga hech narsa saqlanmasligi kerak
