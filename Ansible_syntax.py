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


@app.route("/modules/<module>")
def produce_module_page(module):
    print(module)
    module_object = db.modules.find_one({"_id": ObjectId(module)})
    module_parameters = '<li>Synopsis - {}</li>'.format(module_object['Synopsis'])
    for param in module_object['Parameters']:
        module_parameters += '<li>param - {}</li>'.format(param)
    return render_template('module_form.html',
                           module_parameters=module_parameters,
                           module_name=module_object['Name'])
# {Name:"", Synopsis:"", Parameters:{Name:"", Comment:"", Data_type:"", Required:true\false, Options:{}, Default_option:""}}


@app.route("/desperate_times_call_for_desperate_housewives", methods=['POST'])
def generate_YAML_code():
    request.json
    return "---"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
