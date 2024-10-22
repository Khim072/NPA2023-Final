import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback65070072"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070072",
            "description": "Loopback interface 65070072",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.72.1",
                        "netmask": "255.255.255.0"
                    }
                ]
       
            }
        }
    } 

    resp = requests.put(
        api_url,
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False
    )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback 65070072 is created successfully."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
    )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Loopback 65070072 deleted successfully."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    # Define the YANG JSON data to enable the interface with correct structure
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070072",  # Correct name format
            "description": "Configured by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True  # This sets the interface to "up" (no shutdown)
        }
    }

    # Use the PUT method to apply the configuration
    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
    )

    # Check if the request was successful (status code 2xx)
    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070072 is enabled successfully."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        print('Response:', resp.text)  # This will help you see the error details
        return f"Cannot enable: Interface Loopback65070072. Status Code: {resp.status_code}"



def disable():
    # Define the YANG JSON data to disable the interface
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070072",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False  # This sets the interface to "down" (shutdown)
        }
    }

    # Use the PUT method to apply the configuration
    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
    )

    # Check if the request was successful (status code 2xx)
    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070072 is shutdowned successfully."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        print('Response:', resp.text)  # This helps to see details of the error
        return f"Cannot shutdown: Interface Loopback65070072. Status Code: {resp.status_code}"



def status():
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070072"

    resp = requests.get(
        api_url_status,
        auth=basicauth,
        headers={
            "Accept": "application/yang-data+json"
        },
        verify=False
    )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface Loopback65070072 is up and operational."
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface Loopback65070072 is administratively down and not operational."
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "Interface Loopback65070072 not found."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
