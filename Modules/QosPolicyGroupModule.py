#============================================================
#
#
# Copyright (c) 2017 NetApp, Inc. All rights reserved.
# Specifications subject to change without notice.
#
# This sample code is provided AS IS, with no support or
# warranties of any kind, including but not limited to
# warranties of merchantability or fitness of any kind,
# expressed or implied.
#
# Min Python Version = python 2.7
#
#============================================================


#!/usr/bin/python

from ansible.module_utils.basic import *

import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")


def get():
    url_path        = "/api/2.0/ontap/"

    flag=0

    url_path+="qos-policy-groups"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if policy_group != None:
        if flag is 0:
            url_path+="?policy_group="+policy_group
            flag=1
        else:
            url_path+="&policy_group="+policy_group
    if pg_identifier != None:
        if flag is 0:
            url_path+="?pg_identifier="+pg_identifier
            flag=1
        else:
            url_path+="&pg_identifier="+pg_identifier
    if policy_group_class != None:
        if flag is 0:
            url_path+="?policy_group_class="+policy_group_class
            flag=1
        else:
            url_path+="&policy_group_class="+policy_group_class
    if max_throughput != None:
        if flag is 0:
            url_path+="?max_throughput="+max_throughput
            flag=1
        else:
            url_path+="&max_throughput="+max_throughput
    if sortBy != None:
        if flag is 0:
            url_path+="?sortBy="+sortBy
            flag=1
        else:
            url_path+="&sortBy="+sortBy
    if maxRecords != None:
        if flag is 0:
            url_path+="?maxRecords="+maxRecords
            flag=1
        else:
            url_path+="&maxRecords="+maxRecords
    if nextTag != None:
        if flag is 0:
            url_path+="?nextTag="+nextTag
            flag=1
        else:
            url_path+="&nextTag="+nextTag
    response=http_request_for_get(url_path)
    json_response=response.json()
    return json_response

def post():
    url_path        = "/api/2.0/ontap/"
    url_path+="qos-policy-groups"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (policy_group != None) & (policy_group != key):
        payload['policy_group']=policy_group
    if (pg_identifier != None) & (pg_identifier != key):
        payload['pg_identifier']=pg_identifier
    if (policy_group_class != None) & (policy_group_class != key):
        payload['policy_group_class']=policy_group_class
    if (max_throughput != None) & (max_throughput != key):
        payload['max_throughput']=max_throughput
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.headers
    return json_response

def put():
    url_path        = "/api/2.0/ontap/"
    url_path+="qos-policy-groups/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (policy_group != None) & (policy_group != key):
        payload['policy_group']=policy_group
    if (pg_identifier != None) & (pg_identifier != key):
        payload['pg_identifier']=pg_identifier
    if (policy_group_class != None) & (policy_group_class != key):
        payload['policy_group_class']=policy_group_class
    if (max_throughput != None) & (max_throughput != key):
        payload['max_throughput']=max_throughput
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path        = "/api/2.0/ontap/"
    url_path+="qos-policy-groups/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key for deletion"

def http_request_for_get(url_path,**payload):
	response = requests.get("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_put(url_path,**payload):
	response = requests.put("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_delete(url_path,**payload):
	response = requests.delete("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": ['get', 'put', 'post', 'delete'],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "cluster_key" : {"required": False, "type": "str"},
                "policy_group" : {"required": False, "type": "str"},
                "pg_identifier" : {"required": False, "type": "str"},
                "policy_group_class" : {"required": False, "type": "str"},
                "max_throughput" : {"required": False, "type": "str"},
                "sortBy" : {"required": False, "type": "str"},
                "maxRecords" : {"required": False, "type": "str"},
                "nextTag" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global key
        key = module.params["key"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global policy_group
        policy_group = module.params["policy_group"]
        global pg_identifier
        pg_identifier = module.params["pg_identifier"]
        global policy_group_class
        policy_group_class = module.params["policy_group_class"]
        global max_throughput
        max_throughput = module.params["max_throughput"]
        global sortBy
        sortBy = module.params["sortBy"]
        global maxRecords
        maxRecords = module.params["maxRecords"]
        global nextTag
        nextTag = module.params["nextTag"]

        global json_response

        # Actions
        if module.params["action"] == "get":
                result=get()
                module.exit_json(changed=False,meta=result)
        elif module.params["action"] == "put":
                result=put()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])


if __name__ == '__main__':
    main()