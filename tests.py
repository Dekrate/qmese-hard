import unittest
from datetime import date, timedelta
from main import UM


class TestUserManagerB(unittest.TestCase):

    def setUp(self):
        self.m = UM()
        # Add test users with updated dates for 2025
        self.m.au("John Smith", "john@example.com", "1990-05-15")  # 34-35 years - adult
        self.m.au("Anna Johnson", "anna@example.com", "2010-08-20")  # 14-15 years - child
        self.m.au("Peter Wilson", "peter@example.com", "1955-12-01")  # 69-70 years - senior
        self.m.au("Maria Brown", "maria@example.com", "2015-03-10")  # 9-10 years - child

    def test_ca_adult(self):
        """Test age calculation for adult"""
        age = self.m.ca("1990-05-15")
        expected_age = date.today().year - 1990
        if date.today() < date(date.today().year, 5, 15):
            expected_age -= 1
        self.assertEqual(age, expected_age)

    def test_ca_child(self):
        """Test age calculation for child"""
        age = self.m.ca("2010-03-10")
        expected_age = date.today().year - 2010
        if date.today() < date(date.today().year, 3, 10):
            expected_age -= 1
        self.assertEqual(age, expected_age)

    def test_ca_future_date(self):
        """Test age calculation for future date"""
        future_date = (date.today() + timedelta(days=365)).strftime("%Y-%m-%d")
        age = self.m.ca(future_date)
        self.assertEqual(age, 0)

    def test_gabd_child(self):
        """Test discount for child (0-17 years)"""
        discount = self.m.gabd("anna@example.com")
        self.assertEqual(discount, 20)

    def test_gabd_adult(self):
        """Test discount for adult (18-64 years)"""
        discount = self.m.gabd("john@example.com")
        self.assertEqual(discount, 0)

    def test_gabd_senior(self):
        """Test discount for senior (65+ years)"""
        discount = self.m.gabd("peter@example.com")
        self.assertEqual(discount, 15)

    def test_gabd_nonexistent_user(self):
        """Test discount for non-existent user"""
        discount = self.m.gabd("nonexistent@example.com")
        self.assertEqual(discount, 0)

    def test_gus_counts(self):
        """Test correct user counting"""
        stats = self.m.gus()

        # Check if all categories are present
        self.assertIn('child_count', stats)
        self.assertIn('adult_count', stats)
        self.assertIn('senior_count', stats)
        self.assertIn('active_count', stats)
        self.assertIn('total_count', stats)

        # Check sums
        total_calculated = stats['child_count'] + stats['adult_count'] + stats['senior_count']
        self.assertEqual(stats['total_count'], total_calculated)

    def test_gus_after_deactivation(self):
        """Test statistics after user deactivation"""
        self.m.du("john@example.com")
        stats = self.m.gus()

        # Should be 3 active users out of 4
        self.assertEqual(stats['active_count'], 3)
        self.assertEqual(stats['total_count'], 4)


if __name__ == '__main__':
    unittest.main()