from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get("//")
        self.assertEqual(response.status_code, 200)

    def test_url_avaiolable_by_name(self):
        response = self.client.get(reverse("home_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse("home_view"))
        self.assertContains(response, """<h1>
        Hello To You
    </h1>""")
