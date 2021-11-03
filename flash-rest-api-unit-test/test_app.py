try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/fo')
        status_code = response.status_code

        self.assertEqual(status_code, 200)

    # check if content type is application/json
    def test_index_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/fo')

        self.assertEqual(response.content_type, "application/json")

    # check for data return
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/fo")

        self.assertTrue(b"Message" in response.data)


if __name__ == '__main__':
    unittest.main()
