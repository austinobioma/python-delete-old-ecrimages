import datetime
from unittest import TestCase

from ecr_lifecycle.ecr import ECR


class TestGetImageDate(TestCase):
    def test_get_date_image(self):
        image_date = datetime.datetime(2022, 1, 14, 12, 00, 00)
        expected_image_old = 90
        ecr_test = ECR("DEBUG")
        result = ecr_test.get_image_days(image_date)
        self.assertTrue(result > expected_image_old)
