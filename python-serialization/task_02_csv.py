#!/usr/bin/python3
import csv 
import json


def convert_csv_to_json(csv_filename, json_filename):
    """ Convert CSV file to JSON file """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
        
        return True
    except Exception as e:
        return False
    
