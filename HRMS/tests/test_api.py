import unittest
from app import create_app, db
from app.models import Employee, Candidate

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_employee(self):
        response = self.client.post('/employees', json={
            'name': 'John Doe',
            'position': 'Software Engineer',
            'salary': 70000,
            'performance_score': 4.5
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Employee added successfully!', response.get_json()['message'])

    def test_get_employees(self):
        self.client.post('/employees', json={
            'name': 'John Doe',
            'position': 'Software Engineer',
            'salary': 70000,
            'performance_score': 4.5
        })
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

if __name__ == '__main__':
    unittest.main()
