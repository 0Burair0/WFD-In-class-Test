#Burair - B00138007
#Web Development Framework - H3037
#Test Spec 2025 - Part A

# A2 - Class with initialisation attributes
class StaffRecord:
    def __init__(self, name_value, dob_value, sex_value, staff_code, home_address):
        self.name = name_value
        self.DoB = dob_value
        self.sex = sex_value
        self.staffID = staff_code
        self.address = home_address

    # A3 - Method to print all initialisation attributes
    def show_staff_details(self):
        print("Name:", self.name)
        print("Date of Birth:", self.DoB)
        print("Sex:", self.sex)
        print("Staff ID:", self.staffID)
        print("Address:", self.address)

    # A4 - Update methods for each attribute with type checking
    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name

    def update_dob(self, new_dob):
        if isinstance(new_dob, str):
            self.DoB = new_dob

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex

    def update_staffid(self, new_id):
        if isinstance(new_id, str):
            self.staffID = new_id

    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address


# A5 - Child class with extra attributes
class TeachingStaffRecord(StaffRecord):
    def __init__(self, name_value, dob_value, sex_value, staff_code, home_address, department_area, teaching_subject):
        super().__init__(name_value, dob_value, sex_value, staff_code, home_address)
        self.department = department_area
        self.teaching_subject = teaching_subject

    # A6 - Method to print all attributes including inherited ones
    def display_teaching_staff_info(self):
        print("Name:", self.name)
        print("Date of Birth:", self.DoB)
        print("Sex:", self.sex)
        print("Staff ID:", self.staffID)
        print("Address:", self.address)
        print("Department:", self.department)
        print("Subject:", self.teaching_subject)

    # A7 - Update methods for extra child attributes with type checking
    def update_department(self, new_department):
        if isinstance(new_department, str):
            self.department = new_department

    def update_teaching_subject(self, new_subject):
        if isinstance(new_subject, str):
            self.teaching_subject = new_subject


# A8 - Creating instances of main and child classes
sample_staff = StaffRecord(
    "Burair Moosavi", "1990-02-12", "Male", "B0213424", "45 Willow Crescent Blanchardstown"
)

teaching_staff = TeachingStaffRecord(
    "Emma Kaur", "1985-07-19", "Female", "B0213807", "21 Oak Lane Sandyford", "Science Dept", "Physics"
)


# A9 - Calling the attribute printing methods
sample_staff.show_staff_details()
teaching_staff.display_teaching_staff_info()


# A10 - Updating 2 attributes from A4 and A7, then printing again
sample_staff.update_address("99 Elm Street")
sample_staff.update_dob("1991-03-22")

teaching_staff.update_department("Mathematics Dept")
teaching_staff.update_teaching_subject("Algebra")

print("\n--- After Updates ---\n")
sample_staff.show_staff_details()
teaching_staff.display_teaching_staff_info()
