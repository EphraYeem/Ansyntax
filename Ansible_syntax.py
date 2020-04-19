#!/bin/python3
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, json
app = Flask(__name__)
db = MongoClient().test

SORTABLE_OBJECT_HEADER = '<div class="list-group-item"><span class="glyphicon glyphicon-resize-vertical" aria-hidden="true"></span>'
SORTABLE_OBJECT_FOOTER = '</div>'

SELECT_PARENT_HTML     = SORTABLE_OBJECT_HEADER + '{} <select id={} name="actual_form_attribute">'
SELECT_FOOTER_HTML     = '</select>' + SORTABLE_OBJECT_FOOTER
SELECT_OPTION_HTML     = '<option value={}>{}</option>'
DIV_TEXTBOX_HTML       = SORTABLE_OBJECT_HEADER + '{}<div id={} name="actual_form_attribute" contentEditable="true"></div>' + SORTABLE_OBJECT_FOOTER

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
        select_list = SELECT_PARENT_HTML.format(parameter['Name'], parameter['Name'])
        for op in parameter['Options']:
            select_list += SELECT_OPTION_HTML.format(op, op)
        select_list += SELECT_FOOTER_HTML
        return select_list
    else:
        return DIV_TEXTBOX_HTML.format(parameter['Name'], parameter['Name'])

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
    attribute_dict = request.get_json()
    module_id = attribute_dict.pop('site_url').split('/')[-1]
    print(module_id)
    for attribute, value in attribute_dict.items():
        print(attribute, value)
    return json.jsonify({'try': 'y33'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
