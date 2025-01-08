import requests
from bs4 import BeautifulSoup as bs
import csv

def webscrape():
    URL = 'http://52.25.87.215/TCGAA/cancertype.php?cancertype=BRCA&pageSize=50&page='
    patient_dict = {}
    for i in range(1, 23):
        new_URL = URL + str(i)
        req = requests.get(new_URL)
        soup = bs(req.text, 'html.parser')
        table_data = soup.find_all('td')
        prev_td = ""
        prev_patient_id = ""
        for td in table_data:
            if "TCGA-" in td.text and "Clinical" not in td.text:
                prev_patient_id = td.text
            elif prev_td in ["Hispanic/Latino", "non-Hispanic/Latino", "Not Available"]:
                patient_dict[prev_patient_id] = td.text

            prev_td = td.text
    
    #print(patient_dict)
    print(len(patient_dict))
    return patient_dict
    


def main():
    patient_dict = webscrape()
    field_names= ['bcr_patient_barcode', 'genetic_ancestry']
    patient_dicts = []
    for key, value in patient_dict.items():
        single_patient = {'bcr_patient_barcode': key, 'genetic_ancestry': value}
        patient_dicts.append(single_patient)
    with open('ancestry.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(patient_dicts)
    
    
    print(patient_dict)


if __name__ == '__main__':
    main()