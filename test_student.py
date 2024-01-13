import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')
        

    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_alert_santa(self):
        print('test_email')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        print('test_alert_santa')       
        self.assertTrue(self.student.email, 'johndoe@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


    def  test_course_schedule_sucess(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            shedule = self.student.course_shedule()
            self.assertEqual(schedule, "Sucess")


    def  test_course_schedule_fail(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            
            shedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == '__main__':
    unittest.main()
