import csv
import requests
from bs4 import BeautifulSoup
# from xml.etree.ElementTree import parse
# import xml.etree.ElementTree

if __name__ == "__main__":
	# print("Hello World")

	# # req = requests.get("apphype.aspx")
	# # html = req.text

	f = open("apphype.aspx") 
	soup = BeautifulSoup(f)
	
	# e = xml.etree.ElementTree.parse('apphype.xml').getroot() #element instance 생성
	my_sales = soup.select(
		"string"
		)
	
	for sale in my_sales:
		print(sale.text)

	# tree = parse("apphype.xml")
	# note = tree.getroot()
	# print(note.get("string"))

	

	# for i in e.findall('string'):
	# 	print(i)