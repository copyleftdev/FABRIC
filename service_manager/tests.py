from django.test import TestCase

class FakeTest(TestCase):

    def test_fake_01(self):
        testv = 4
        self.assertEquals(testv,4)

    def test_fake_02(self):
        testv = 20
        self.assertEquals(testv,10)
