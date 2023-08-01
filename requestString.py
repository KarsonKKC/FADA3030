import csv
import json


def deleteStuff(dictionary):
	for i in ["Category","Functional unit","Embodied Energy (MJ)","Embodied Water (L)","Embodied Greenhouse Gas Emissions (kgCO₂e)","More information",""]:
		del dictionary[i]
	return dictionary

with open(r"C:\Users\Karson\FADA3030\EPiC_Database_2019.csv","r", encoding="utf-8") as file:
	reader = csv.DictReader(file)
	reader = list(reader)

	reader = list(map(lambda x: deleteStuff(x), reader))

	# print(reader[68])
	# print(reader[74])

	jsonString = json.dumps(list(reader))
	
	requestString = '''Please select from following list of materials represented by dictionaries, which material you think represented here as a dictionary {requestDictionary} is most similar to.
	Don't include the question in your response. Don't include any explanations in your response. Please return only the selected dictionary.
	'''.format(**{"requestDictionary":json.dumps({"material":"Lysaght Trimdek - Night Sky", "commonUse":"Roof", "gptDescription":"As of my last update in September 2021, Lysaght Trimdek is a brand of roofing and wall cladding made by Lysaght, a well-known Australian steel building products manufacturer. \"Night Sky\" is a specific color option available for the Lysaght Trimdek product line. Lysaght Trimdek roofing and wall cladding are typically made from high-quality steel, specifically Colorbond® steel. Colorbond® steel is a coated steel product known for its durability, weather resistance, and aesthetic appeal. It is made from a combination of steel, zinc, and aluminum, which is then coated with a special paint system that provides color and additional protection against corrosion. The specific composition and manufacturing process of Colorbond® steel may vary slightly based on the region and local standards, so it's always a good idea to check with the manufacturer or their official documentation for the most up-to-date information. If you are inquiring about a more recent version of Lysaght Trimdek or any changes made to the product after September 2021, I recommend reaching out to Lysaght directly or visiting their official website for the most current information."})})

	requestString = requestString+"\n"+jsonString

	print(requestString)



