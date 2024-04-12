import json

# Load data from final_output.json
with open("license_output.json", "r") as json_file:
    data = json.load(json_file)

# Extract relevant details
document_info = data["document"]["inference"]["prediction"]

# Extract features
state = document_info["state"]["value"]
driver_license_id = document_info["driver_license_id"]["value"]
expiry_date = document_info["expiry_date"]["value"]
issued_date = document_info["issued_date"]["value"]
last_name = document_info["last_name"]["value"]
first_name = document_info["first_name"]["value"]
address = document_info["address"]["value"]
date_of_birth = document_info["date_of_birth"]["value"]
restrictions = document_info["restrictions"]["value"]
endorsements = document_info["endorsements"]["value"]
dl_class = document_info["dl_class"]["value"]
sex = document_info["sex"]["value"]
height = document_info["height"]["value"]
weight = document_info["weight"]["value"]
hair_color = document_info["hair_color"]["value"]
eye_color = document_info["eye_color"]["value"]
dd_number = document_info["dd_number"]["value"]

# Print extracted details
print("\nExtracted details from the document:\n\n")
print("State:", state)
print("Driver License ID:", driver_license_id)
print("Expiry Date:", expiry_date)
print("Date Of Issue:", issued_date)
print("Last Name:", last_name)
print("First Name:", first_name)
print("Address:", address)
print("Date Of Birth:", date_of_birth)
print("Restrictions:", restrictions)
print("Endorsements:", endorsements)
print("Driver License Class:", dl_class)
print("Sex:", sex)
print("Height:", height)
print("Weight:", weight)
print("Hair Color:", hair_color)
print("Eye Color:", eye_color)
print("Document Discriminator:", dd_number)
