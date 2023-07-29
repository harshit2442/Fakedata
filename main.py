import datetime
import os

import pandas as pd
from faker import Faker

fake = Faker(locale='en_GB')


class FakeDataGenerator:
    data_type_generators = {
        'name': fake.name,
        'address': fake.address,
        'phone_number': fake.phone_number,
        'cell_phone': fake.cellphone_number,
        'postcode': fake.postcode,
        'country': fake.country,
        'SSN': fake.ssn,
        'Vat_ID': fake.vat_id,
        'DOB': lambda: fake.date_of_birth(minimum_age=18, maximum_age=100),
        'Male_name': lambda: fake.prefix_male() + ' ' + fake.first_name_male() + ' ' + fake.last_name_male(),
        'Female_name': lambda: fake.prefix_female() + ' ' + fake.first_name_female() + ' ' + fake.last_name_female(),
        'Safe_email': fake.safe_email,
        'Free_email': fake.free_email,
        'Swift_code_8_digit': fake.swift8,
        'Swift_code_11_digit': fake.swift11,
        'IBAN': fake.iban,
        'BBAN': fake.bban,
        'Car_lic_plate': fake.license_plate,
        'prefix_male': fake.prefix_male,
        'prefix_female': fake.prefix_female,
        'male_last_name': fake.last_name_male,
        'female_last_name': fake.last_name_female
    }

    def __init__(self, num_records, data_types, start_date=datetime.date(year=1980, month=1, day=1)):
        self.num_records = num_records
        self.data_types = data_types
        self.start_date = start_date

    def generate_fake_data(self, name_dropdown, address_dropdown, Vat_ID_dropdown, SSN_dropdown, phone_number_dropdown,
                           cell_phone_dropdown, male_name_dropdown, female_name_dropdown, safe_email_dropdown,
                           free_email_dropdown, swift_code_8_dropdown, swift_code_11_dropdown, IBAN_dropdown,
                           BBAN_dropdown, car_lic_plate_dropdown, country_dropdown, post_code, dob_dropdown):
        data = []
        for i in range(self.num_records):
            record = {}
            if name_dropdown == "Yes":
                record["name"] = self.data_type_generators["name"]()
            if Vat_ID_dropdown == "Yes":
                record["Vat ID"] = self.data_type_generators["Vat_ID"]()
            if SSN_dropdown == "Yes":
                record["SSN"] = self.data_type_generators["SSN"]()
            if phone_number_dropdown == "Yes":
                record["Phone number"] = self.data_type_generators["phone_number"]()
            if cell_phone_dropdown == "Yes":
                record["cell_phone"] = self.data_type_generators["cell_phone"]()
            if male_name_dropdown == "Yes":
                record["Male_name"] = self.data_type_generators["Male_name"]()
            if female_name_dropdown == "Yes":
                record["Female_name"] = self.data_type_generators["Female_name"]()
            if safe_email_dropdown == "Yes":
                record["Safe_email"] = self.data_type_generators["Safe_email"]()
            if free_email_dropdown == "Yes":
                record["Free_email"] = self.data_type_generators["Free_email"]()
            if swift_code_8_dropdown == "Yes":
                record["Swift_code_8_digit"] = self.data_type_generators["Swift_code_8_digit"]()
            if swift_code_11_dropdown == "Yes":
                record["Swift_code_11_digit"] = self.data_type_generators["Swift_code_11_digit"]()
            if IBAN_dropdown == "Yes":
                record["IBAN"] = self.data_type_generators["IBAN"]()
            if BBAN_dropdown == "Yes":
                record["BBAN"] = self.data_type_generators["BBAN"]()
            if car_lic_plate_dropdown == "Yes":
                record["Car_lic_plate"] = self.data_type_generators["Car_lic_plate"]()
            if address_dropdown == "Yes":
                record["address"] = self.data_type_generators["address"]()
            if country_dropdown == "Yes":
                record["country"] = self.data_type_generators["country"]()
            if post_code == "Yes":
                record["postcode"] = self.data_type_generators["postcode"]()
            if dob_dropdown == "Yes":
                record["DOB"] = self.data_type_generators["DOB"]()
            data.append(record)
        return data


def main():
    # Read input values from Excel file
    df = pd.read_excel('input_data.xlsx', sheet_name='Sheet1')
    print(df)

    # Extract input values
    num_records = int(df.iloc[2, 4])
    name_dropdown = df.iloc[3, 4]
    Vat_ID_dropdown = df.iloc[4, 4]
    SSN_dropdown = df.iloc[5, 4]
    phone_number_dropdown = df.iloc[6, 4]
    cell_phone_dropdown = df.iloc[7, 4]
    male_name_dropdown = df.iloc[8, 4]
    female_name_dropdown = df.iloc[9, 4]
    safe_email_dropdown = df.iloc[10, 4]
    free_email_dropdown = df.iloc[11, 4]
    swift_code_8_dropdown = df.iloc[12, 4]
    swift_code_11_dropdown = df.iloc[13, 4]
    IBAN_dropdown = df.iloc[14, 4]
    BBAN_dropdown = df.iloc[15, 4]
    car_lic_plate_dropdown = df.iloc[16, 4]
    address_dropdown = df.iloc[17, 4]
    country_dropdown = df.iloc[18, 4]
    post_code = df.iloc[19, 4]
    dob_dropdown = df.iloc[20, 4]

    # Generate fake data
    fake_data_generator = FakeDataGenerator(num_records,
                                            ['name', 'Vat_ID', 'SSN', 'phone_number', 'cell_phone', 'Male_name',
                                             'Female_name', 'Safe_email', 'Free_email', 'Swift_code_8_digit',
                                             'Swift_code_11_digit', 'IBAN', 'BBAN', 'Car_lic_plate', 'address',
                                             'country', 'postcode', 'DOB'])
    fake_data = fake_data_generator.generate_fake_data(name_dropdown, address_dropdown, Vat_ID_dropdown, SSN_dropdown,
                                                       phone_number_dropdown, cell_phone_dropdown, male_name_dropdown,
                                                       female_name_dropdown, safe_email_dropdown, free_email_dropdown,
                                                       swift_code_8_dropdown, swift_code_11_dropdown, IBAN_dropdown,
                                                       BBAN_dropdown, car_lic_plate_dropdown, country_dropdown,
                                                       post_code, dob_dropdown)
    df_fake = pd.DataFrame(fake_data)
    print(df_fake)

# Save fake data to Excel file in the outputfolder
    output_folder = "Output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_path = os.path.join(output_folder, "fake_data_" + fake.date_time_this_year().strftime("%Y%m%d_%H%M%S") + ".xlsx")
    with pd.ExcelWriter(file_path) as writer:
        df_fake.to_excel(writer, index=False)
    print("Data saved to", file_path)


if __name__ == '__main__':
    main()
