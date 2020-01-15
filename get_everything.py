#!/bin/python3
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
db = MongoClient().test


def process_module(module_name, module_url):
    module_info = {"Name": module_name}
    url = f'https://docs.ansible.com/ansible/latest/modules/{module_url}'
    url_html = requests.get(url).text
    soup = BeautifulSoup(url_html, "html.parser")
    parameters = soup.find(id="parameters").find("table", border=0).find_all("tr")
    synopsis = str(soup.find(id="synopsis").find(class_="simple"))
    module_info["Synopsis"] = synopsis
    parameters_info = []
    for p in parameters[1:]:
        current_parameter_info = {}
        cells = list(p.find_all("td"))
        actual_parameter = cells[0].get_text().strip().split("\n")
        p_name = actual_parameter[0]
        current_parameter_info['Name'] = p_name
        atts = actual_parameter[-1].split('/')
        data_type, is_required = atts[0], len(atts) > 1
        current_parameter_info['Data_type'] = data_type
        current_parameter_info['Required'] = is_required
        choices = cells[1].findAll('li')
        if choices:
            cts = []
            default_c = "hmm"
            for c in choices:
                ct = c.get_text()
                if "←" in ct:
                    ct = ct.replace("←", "").strip()
                    default_c = ct
                cts.append(ct)
                current_parameter_info['Options'] = cts
                current_parameter_info['Default_option'] = default_c
        comments = str(cells[2])
        current_parameter_info['Comments'] = comments
        parameters_info.append(current_parameter_info)
    module_info['Parameters'] = parameters_info
    return module_info
# {Name:"", Synopsis:"", Parameters:[{Name:"", Comments:"", Data_type:"", Required:true\false, Options:[""], Default_option:""}]}


all_modules = 'https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html'
all_modules_html = requests.get(all_modules).text
all_modules_soup = BeautifulSoup(all_modules_html, "html.parser")
modules = all_modules_soup.find(id="all-modules").find(class_='simple').findAll('a')
i=0
for m in modules:
    db.modules.insert_one(process_module(m.text, m['href']))
    i += 1
    if i > 1:
        break
