#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pybozocrack
----------------------------------

Tests for `pybozocrack` module.
"""

import unittest

from pybozocrack import pybozocrack


class TestPybozocrack(unittest.TestCase):
	
    def setUp(self):
        self.hash = "d0763edaa9d9bd2a9516280e9044d885"
        self.plaintext = "monkey"

        file = open('test', 'w')
        file.write('fcf1eed8596699624167416a1e7e122e\nbed128365216c019988915ed3add75fb')
        file.close()

        self.cracker = BozoCrack('test')


    def test_loaded_hashes(self):
        self.assertEqual(len(self.cracker.hashes), 2)

    def test_load_empty_cache(self):
        self.assertEqual(self.load_cache(), {})

    def test_dictionary_attack_known_hash(self):
        self.assertEqual(pybozocrack.dictionary_attack(self.hash, ['zebra', '123', self.plaintext]), self.plaintext)
		
    def test_dictionary_attack_invalid_hash(self):
        self.assertIsNone(pybozocrack.dictionary_attack(self.hash, ['zebra', '123']))
		
    def test_format_it(self):
        self.assertEqual(pybozocrack.format_it(self.hash, self.plaintext), "{}:{}".format(self.hash, self.plaintext))

    def test_crack_single_hash(self):
        self.assertEqual(pybozocrack.crack_single_hash(self.hash), self.plaintext)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
