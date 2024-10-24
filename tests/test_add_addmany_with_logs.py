import logging
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pysondb

class TestAddWithLogs(unittest.TestCase):
    def test_add_first_logs_entry(self):
        logger = logging.getLogger().setLevel(logging.WARNING)
        a = pysondb.getDb('test_logs.json', log=True)
        new_data = {"id": 10, "path": "value"}

        with self.assertLogs(logger, level='WARNING') as log:
            a.add(new_data)

        os.remove('test_logs.json')
        os.remove('test_logs.json.lock')
        self.assertIn(
            'The provided id field was replaced by the system-generated id',
            log.output[0]
        )

    def test_add_many_logs_entry(self):
        logger = logging.getLogger().setLevel(logging.WARNING)
        a = pysondb.getDb('test_logs.json', log=True)
        new_data = [{"id": 10, "path": "value"},{"id": 20, "path": "value"}]

        with self.assertLogs(logger, level='WARNING') as log:
            a.addMany(new_data)

        os.remove('test_logs.json')
        os.remove('test_logs.json.lock')
        self.assertIn(
            'The provided id field was replaced by the system-generated id',
            log.output[0]
        )

if __name__ == '__main__':
    unittest.main()