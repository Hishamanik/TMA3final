import os
import json
from TMA3.settings import BASE_DIR

# TODO: Replace with model interaction in P4
def loadDummyData():
    p = os.path.join(BASE_DIR, 'part3/static/dummy.json')
    with open(p) as f:
        return json.loads(f.read())

def get_computers():
    data = loadDummyData()
    return data['computers']

def get_computer(id):
    data = loadDummyData()
    computers = data['computers']
    for computer in computers:
        if computer['id'] == id:
            return computer

def get_components():
    data = loadDummyData()
    return data['components']

def get_component(id):
    data = loadDummyData()
    for component in data['components']:
        if component['id'] == id:
            return component

def get_components_for_computer(id):
    computer = get_computer(id)
    all_components = get_components()
    components = {}
    for key in all_components.keys():
        for component in all_components[key]:
            if component['id'] == computer['components'][key]:
                components[key] = component
    return components

def get_component_details(components):
    all_components = get_components()
    component_details = {}
    for key in components.keys():
        for candidate in all_components[key]:
            if candidate['id'] == components[key]:
                component_details[key] = candidate
    
    return component_details

if __name__ == '__main__':
    # print(get_computers())
    # print(get_components())
    # print(get_component(2))
    print(get_components_for_computer(6))
    # pass