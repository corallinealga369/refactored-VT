#! python3
import requests
import json
import io
import tarfile
from vtapikey import apikey

def url_report():
   url = 'https://www.virustotal.com/vtapi/v2/url/scan'
   url2=input("Input a url to scan. Include http://")
   params = {'apikey': apikey, 'url':url2}
   response = requests.post(url, data=params)
   print(response.json())
   jsonData=response.json()
   name=input("Please enter a prefix for url_report.txt :")
   with open(name+'_url_report.txt', 'w') as outfile:
     json.dump(jsonData, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)
   print("Your results were saved in the file "+name+"_url_report.txt .") 
   
def ip_report():
   ip=input("Input an IP address with this format: X.X.X.X ")
   url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
   params = {'apikey':apikey,'ip':ip}
   response = requests.get(url, params=params)
   print(response.json())
   jsonData=response.json()
   name=input("Please enter a prefix for ip_report.txt :")
   with open(name+'_ip_report.txt', 'w') as outfile:
     json.dump(jsonData, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)
   print("Your results were saved in the file "+name+"_ip_report.txt .")


def url_scan():
   url2=input("Input a url to scan. Include http://")
   url = 'https://www.virustotal.com/vtapi/v2/url/scan'
   params = {'apikey': apikey, 'url':url2}
   response = requests.post(url, data=params)
   print(response.json())
   jsonData=response.json()
   name=input("Please enter a prefix for url_scan.txt")
   with open(name+'_url_scan.txt', 'w') as outfile:
     json.dump(jsonData, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)
   print("Your results were saved in the file "+name+"_url_scan.txt .")


print('Welcome to the VT url/ip scan script.')
print('Enter a number 1-3 to choose an action.')
choice=input("Do you want a url report[1], ip report[2], or to scan a new url[3]? ")

if choice=='1':
    url_report()
elif choice=='2':
    ip_report()
elif choice=='3':
    url_scan()
else:
    print("You must enter the digits 1, 2 or 3 to make a choice.")
    print("Run the script again with correct input to use.")

