from datetime import datetime
import csv


def csvFileToJson(path):
    jsonArray = []
    with open(path, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)
        for row in csvReader: 
            jsonArray.append(row)
    return jsonArray


def printDateFromFile(path):
    jsonArray = csvFileToJson(path)
    for row in jsonArray:
        print(row['Date'])


printDateFromFile('shampoo_sales.csv')