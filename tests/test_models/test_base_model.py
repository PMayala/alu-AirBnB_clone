#!/usr/bin/python3
"""test for Base Model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_init(self):
        """Test if the instance is created"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_uuid(self):
        """Test if a unique id is generated"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_datetime(self):
        """Test if the created_at and updated_at attributes are datetime objects"""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """Test if the updated_at attribute is updated after save() is called"""
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict(self):
        """Test if the to_dict method returns a dictionary with the correct keys and values"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
