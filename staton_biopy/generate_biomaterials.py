import sys
import xml.etree.cElementTree as ET
from faker import Faker
import random


def create_biomaterials(num_biomats):
    fake = Faker()
    output_file = "biomaterials.xml"
    root = ET.Element("BioSampleSet")
    count = 0
    constant_property = fake.word()
    constant_value_1 = fake.word()
    constant_value_2 = fake.word()

    while count < int(num_biomats):
        accession = fake.word()
        biosample = ET.SubElement(root, "BioSample", submission_date=fake.date(), id=fake.word(), accession=accession)

        ET.SubElement(biosample, "IDs", db="BioSample", is_primary="1").text = accession
        ET.SubElement(biosample, "Description").text = fake.sentence()
        owner = ET.SubElement(biosample, "Owner")
        ET.SubElement(owner, "Name", ).text = fake.name()
        ET.SubElement(owner, "Address").text = fake.address()
        attributes = ET.SubElement(biosample, "Attributes")
        attribute_count = 0
        while attribute_count < 4:
            attribute_name = fake.word()
            ET.SubElement(attributes, "Attribute", attribute_name=attribute_name,
                          harmonized_name=attribute_name,
                          display_name=attribute_name).text = fake.word()
            attribute_count += 1

        this_constant_attr_text = constant_value_1
        if count % 2 == 0:
            this_constant_attr_text = constant_value_2
        ET.SubElement(attributes, "Attribute", attribute_name=constant_property,
                      harmonized_name=constant_property,
                      display_name=constant_property).text = this_constant_attr_text
        ET.SubElement(attributes, "Attribute", attribute_name=fake.word(),
                      ).text = str(random.randint(1, 101))

        count += 1

    tree = ET.ElementTree(root)
    tree.write(output_file)


if __name__ == "__main__":
    number_of_biomaterials = 1
    if sys.argv[1]:
        number_of_biomaterials = sys.argv[1]
    create_biomaterials(number_of_biomaterials)
