import unittest
from fastapi.testclient import TestClient
from fastapi_app.app import app

class FastAPIAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_home_page(self):
        """Test the home page returns 200 and contains expected content."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sentiment Analysis', response.text)

    def test_predict_endpoint(self):
        """Test the predict endpoint with sample text."""
        response = self.client.post('/predict', data={"text": "I love this movie! It was amazing!"})
        self.assertEqual(response.status_code, 200)
        # Check if response contains sentiment result
        self.assertIn('sentiment', response.text.lower())

    def test_predict_negative_sentiment(self):
        """Test prediction with negative sentiment text."""
        response = self.client.post('/predict', data={"text": "This is terrible and awful!"})
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        """Test the health check endpoint."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('model_version', data)

    def test_predict_with_empty_text(self):
        """Test prediction with empty text."""
        response = self.client.post('/predict', data={"text": ""})
        # Should still return 200 as the app processes it
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
