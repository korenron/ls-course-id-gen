import json
import random


print("Enter the course level:")
#courseLevel = sys.argv[1]
courseLevel = input() 
print("\n Enter the protfolio:")
admProtfolio = input()
print("\n Enter the product:")
product = input()
print("\n Enter the course name:")
courseName = input()
productCode = 0
protfolioCode = 0
filenameToSave = "course_data.json"

# Open the file in read mode
with open("ADMProductTaxomony.json", "r") as f:
  # Read the content as a dictionary
  productTaxomony = json.load(f)
#print(productTaxomony["ALM"]["code"]) 
protfolioCode = productTaxomony[admProtfolio]["code"]
productCode = productTaxomony[admProtfolio][product]
print(protfolioCode)
print(productCode)


def generate_course_id():
  """Generates a 5-digit course ID consisting of 3 blocks.

  Each block is a random integer between productCode*10 and productCode*10+19, padded with zeros
  to ensure 2 digits
  Returns:
    A string representing the generated course ID.
  """
  block1 = courseLevel
  block2 = protfolioCode
  rangeforRandomstart = productCode*10
  rangeforRandomEnd = rangeforRandomstart+19
  block3 = str(random.randint(rangeforRandomstart, rangeforRandomEnd)).zfill(2)

  return f"{block1}{block2}{block3}"

# Generate and print course ID
course_id = generate_course_id()
#print("course_id is: " + str(course_id))

def value_exists_in_json(json_data, value):
  """
  Checks if a given value exists in a JSON object, including nested structures.

  Args:
      json_data: The JSON object to search (can be a dictionary, list, string, or integer).
      value: The value to search for.

  Returns:
      True if the value exists in the JSON object, False otherwise.
  """

  def check_value(data):
    if isinstance(data, dict):
      for val in data.values():
        if check_value(val) or val == value:
          return True
    elif isinstance(data, list):
      for item in data:
        if check_value(item) or item == value:
          return True
    return data == value  # Explicitly check for equality with the value

  return check_value(json_data)

def add_course_to_json(filename, course_info):
  """Adds new course information to a JSON file, preserving existing data.

  Args:
      filename: The path to the JSON file.
      course_info: A dictionary containing the new course information (key-value pairs).

  Returns:
      None
  """

  try:
    # Open the file in read mode to check if it exists
    with open(filename, "r") as f:
      data = json.load(f)
  except FileNotFoundError:
    # If the file doesn't exist, create a new dictionary with "courses" as an empty list
    data = {"courses": []}
 # Add the new course information to the "courses" list
  if "courses" in data:
    data["courses"].append(course_info)
  else:
    data["courses"] = [course_info]

 
  # Open the file in write mode and write the updated data with indentation
  with open(filename, "w") as f:
    json.dump(data, f, indent=4)

  print(f"New course added to {filename}!")


# Example usage with sample course data


try:
    # Open the file in read mode to check if it exists
    with open(filenameToSave, "r") as f:
        data = json.load(f)
        # Add a loop here - recursive 
        value = value_exists_in_json(data, course_id)
        #print("Result: " + str(result))
        while value:
          print("The course ID already exists")
          #generate new course id
          course_id = generate_course_id()
          value = value_exists_in_json(data, course_id)

        print("Loop finished (value is now False)") 
        course_info = {
          "course_id": course_id,
          "name": courseName 
        }
        print(course_info)
        add_course_to_json(filenameToSave, course_info)

        #if :
        #    print("The course ID already exists in the JSON data.")
        #else:
            # Add the new course information (since the ID doesn't exist)
        #    add_course_to_json(filenameToSave, course_info)
        
              
except FileNotFoundError:
    # If the file doesn't exist, create a new dictionary with "courses" as an empty list
    print("FileNotFoundError")

#add_course_to_json(filenameToSave, course_info)