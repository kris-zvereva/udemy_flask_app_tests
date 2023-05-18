from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        # with - is a context manager block
        # test client that allows to make requests but doesn't run anything.
        # tests dont need to know they are test client (its in base_test)
        with self.app() as c:
            # c.get() makes a get request to the endpoint
            response = c.get('/')

            self.assertEqual(response.status_code, 200)
            # loads = load a string and convert it into a dictionary
            self.assertDictEqual(json.loads(response.get_data()),
                                 {'message': 'hello world'})
