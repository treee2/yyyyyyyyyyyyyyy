from django.test import TestCase

# Create your tests here.
class SimpleTestCase(TestCase):
    # Тестируем простые страницы приложения
    def test_home_page(self):
        # Проверяем, что главная страница доступна
        response = self.client.get('/')
        # Проверяем, что статус ответа 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        # Проверяем, что страница "О нас" доступна
        response = self.client.get('/about/') 
        self.assertEqual(response.status_code, 200)
        
