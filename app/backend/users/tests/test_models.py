from django.test import TestCase
from users.models import CustomUser, Availability

class AvailabilityModelTests(TestCase):
    def setUp(self):
        # Create a sample user
        self.user = CustomUser.objects.create(username='test_user')

        # Create a sample availability
        self.availability = Availability.objects.create(
            user_id=self.user,
            year=2024,
            month=3,
            day=3,
            times={'10:00': '11:00', '12:00': '13:00'}
        )

    def test_availability_creation(self):
        # Test that availability is created with correct attributes
        self.assertEqual(self.availability.user_id, self.user)
        self.assertEqual(self.availability.year, 2024)
        self.assertEqual(self.availability.month, 3)
        self.assertEqual(self.availability.day, 3)
        self.assertEqual(self.availability.times, {'10:00': '11:00', '12:00': '13:00'})

    def test_availability_string_representation(self):
        # Test the availability string representation
        self.assertEqual(str(self.availability), 'test_user')

    def test_availability_user_relationship(self):
        # Test the relationship between availability and user
        self.assertEqual(self.availability.user_id, self.user)
