This Python program generates unique course IDs based on a specific logic defined in a separate JSON file named ADMProductTaxomony
The generated ID is then stored in a separate JSON file named course_data.json for further use.

Features:

Leverages a customizable JSON file (ADMProductTaxomony.json) to define the course ID generation logic.
Produces unique course IDs based on the specified logic.
Saves the generated IDs in a well-structured JSON file (course_data.json).
Offers clear and concise error handling to ensure robustness.

**How to Use**

Prerequisites: Make sure you have Python installed on your machine.

**Run the Program** (example)
python .\main.py
    Enter the course level: 2
    Enter the protfolio: UFT
    Enter the product: UFTOne
    Enter the course name: UFTOne Essentials

**Sample Output**
The program will write to the course_data.json the generated course ID.

{
    "courses": [
       {
            "course_id": "15807",
            "name": "UFTOne Essentials OnDemand (2023)"
        }
    ]
}

**Contributing**
If you find a bug or have a suggestion, feel free to open an issue. Contributions are welcome!
