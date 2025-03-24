#Burair - B00138007
#Web Development Framework - H3037
#Test Spec 2025 - Part B


import unittest
from PartA import StaffRecord

# B2 - Test if an object is an instance of a class
class StaffTestingGroup(unittest.TestCase):

    def test_is_instance_of_staffrecord(self):
        staff = StaffRecord("Leo", "1988-03-12", "Male", "STF201", "Elm Street")
        self.assertIsInstance(staff, StaffRecord)  # should be StaffRecord

# B3 - Test if an object is NOT an instance of a class
    def test_is_not_instance_of_staffrecord(self):
        random_item = "Just a string"
        self.assertNotIsInstance(random_item, StaffRecord)  # not a StaffRecord

# B4 - Test if 2 objects are identical
    def test_objects_are_identical(self):
        staff1 = StaffRecord("Elena", "1993-09-05", "Female", "STF007", "Coastal Road")
        staff2 = staff1
        self.assertIs(staff1, staff2)  # same object reference

    def test_objects_are_not_identical(self):
        staff1 = StaffRecord("Elena", "1993-09-05", "Female", "STF007", "Coastal Road")
        staff2 = StaffRecord("Elena", "1993-09-05", "Female", "STF007", "Coastal Road")
        self.assertIsNot(staff1, staff2)  # different objects despite same data

# B5 - Test update methods from Part A4 (valid & invalid)
    def test_update_name_valid(self):
        staff = StaffRecord("Test Name", "2000-01-01", "Other", "STF000", "Unknown")
        staff.update_name("Updated Name")
        self.assertEqual(staff.name, "Updated Name")  # name should change

    def test_update_address_valid(self):
        staff = StaffRecord("Test Name", "2000-01-01", "Other", "STF000", "Unknown")
        staff.update_address("New Location")
        self.assertEqual(staff.address, "New Location")  # address should change

    def test_update_name_invalid_type(self):
        staff = StaffRecord("Anna", "1995-06-30", "Female", "STF111", "Hill Drive")
        staff.update_name(999)  # invalid type
        self.assertEqual(staff.name, "Anna")  # remains unchanged

    def test_update_address_invalid_type(self):
        staff = StaffRecord("Anna", "1995-06-30", "Female", "STF111", "Hill Drive")
        staff.update_address(["Street", "Place"])  # invalid type
        self.assertEqual(staff.address, "Hill Drive")  # remains unchanged

# B6 - Main function to run tests (B2-B5)
if __name__ == '__main__':
    unittest.main()
