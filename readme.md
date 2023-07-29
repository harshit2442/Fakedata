# Fake Data Generator

The Fake Data Generator is a Python script that generates fake data based on the specified data types. It uses the `faker` library to produce realistic and random fake data for various fields.

## Getting Started

### Prerequisites

Before running the script, make sure you have the following installed:

- Python (>=3.6)
- `faker` library

You can install the required library using pip install -r requirements.txt


### Input Data

The input data for the script should be provided in an Excel file named `input_data.xlsx`. The script reads the input data from the "Sheet1" worksheet of the Excel file. The Excel file should have the following columns and corresponding data:

| Field Name        | Description                                   |
| ----------------- | --------------------------------------------- |
| num_records       | Number of fake records to generate (integer) |
| name_dropdown     | "Yes" to generate fake names, otherwise "No" |
| Vat_ID_dropdown   | "Yes" to generate fake VAT IDs, otherwise "No"|
| SSN_dropdown      | "Yes" to generate fake SSNs, otherwise "No"   |
| ... (other data types) |

**num_records**: Specify the number of fake records you want to generate. For example, if you want to create 100 fake records, enter the value "100" in the `num_records` cell.

### Supported Data Types

The script supports the following data types for generating fake data:

- Name: `name`
- Address: `address`
- Phone Number: `phone_number`
- Cell Phone Number: `cell_phone`
- Postcode: `postcode`
- Country: `country`
- Social Security Number (SSN): `SSN`
- Value Added Tax ID (VAT ID): `Vat_ID`
- Date of Birth (DOB): `DOB`
- Male Name: `Male_name`
- Female Name: `Female_name`
- Safe Email: `Safe_email`
- Free Email: `Free_email`
- Swift Code (8-digit): `Swift_code_8_digit`
- Swift Code (11-digit): `Swift_code_11_digit`
- International Bank Account Number (IBAN): `IBAN`
- Basic Bank Account Number (BBAN): `BBAN`
- Car License Plate: `Car_lic_plate`
- Male Prefix: `prefix_male`
- Female Prefix: `prefix_female`
- Male Last Name: `male_last_name`
- Female Last Name: `female_last_name`

### Locale

The script uses the `en_GB` locale from the `faker` library, which generates data with a British English context. The locale can be customized as per your preference. Refer to the `faker` library documentation for more information on locales and how to change them.

### Running the Script

To run the script, simply execute the Python script `fake_data_generator.py`. The script will read the input data from `input_data.xlsx`, generate the specified number of fake records, and save the output to a new Excel file in the `Output` folder.




### Output

The generated fake data will be saved in an Excel file with a name in the format `fake_data_YYYYMMDD_HHMMSS.xlsx`, where `YYYYMMDD` represents the current date and `HHMMSS` represents the current time when the data was generated. The output file will be stored in the `Output` folder.

## Customization

You can customize the data types and additional settings by modifying the `data_types` and `generate_fake_data` methods in the `FakeDataGenerator` class. Refer to the `faker` library documentation for more data types and customization options.

## Acknowledgments

- The script uses the `faker` library to generate fake data. More information about the library can be found at https://faker.readthedocs.io/.
- This script is provided as a starting point for generating fake data and can be further customized as per specific requirements.



