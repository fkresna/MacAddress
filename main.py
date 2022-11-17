import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("api_key")
parser.add_argument("mac_address")

def get_response_from_mac_address(api_key, mac_address):
    response = requests.get("https://api.macaddress.io/v1?apiKey=" + api_key + "&output=json&search=" + mac_address)
    if response.json().get('error') and response.json()['error'] is not None:
        print(response.json()['error'])
    else:
        print("This mac address " + mac_address + " belong to the company " + response.json()['vendorDetails']['companyName'])

if __name__ == '__main__':
    args = parser.parse_args()
    if args.api_key is None:
        print("Please enter API key")
    elif args.mac_address is None:
        print("Please enter mac address")
    else:
        get_response_from_mac_address(args.api_key, args.mac_address)

