#!/bin/python3
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request
app = Flask(__name__)
db = MongoClient().test


@app.route("/")
@app.route("/home")
def home():
    list_of_modules = ""
    modules_collection = db.modules
    for m in modules_collection.find():
        list_of_modules += "<li><a href=\"/modules/{}\">{}</a></li>".format(m['_id'],
                                                                            m['Name'])
    return render_template('Ansi.html', list_of_modules=list_of_modules)


def format_parameter(parameter):
    if 'Options' in parameter:
        select_list = '<div>{}<select name={} form="module_form">'.format(parameter['Name'], parameter['Name'])
        for op in parameter['Options']:
            select_list += '<option value={}>{}</option>'.format(op, op)
        select_list += '</select></div>'
        return select_list
    else:
        #select_list = '<div>{}<input type="search" name={}></input></div>'.format(parameter['Name'], parameter['Name'])
        #select_list = '<div>{}<textarea form ="module_form" name={}></textarea></div>'.format(parameter['Name'], parameter['Name'])
        #'<div>{}<div name={} class="form_attribute" contentEditable="true"></div></div>'.format(parameter['Name'], parameter['Name']) + \
        #'<textarea name={} style="display:none"></textarea>'.format(parameter['Name'])
        return '<div>{}<div name={} class="form_attribute" contentEditable="true"></div></div>'.format(parameter['Name'], parameter['Name'])

@app.route("/modules/<module>")
def produce_module_page(module):
    module_object = db.modules.find_one({"_id": ObjectId(module)})
    module_parameters = ''
    for param in module_object['Parameters']:
        module_parameters += format_parameter(param)
    return render_template('module_form.html',
                           module_parameters=module_parameters,
                           module_name=module_object['Name'],
                           synopsis=module_object['Synopsis'])
# {Name:"", Synopsis:"", Parameters:{Name:"", Comments:"", Data_type:"", Required:true\false, Options:{}, Default_option:""}}


@app.route("/desperate_times_call_for_desperate_housewives", methods=['POST'])
def generate_YAML_code():
    print("yee")
    request.json
    return "---"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
