#Script will take a list of HubSpot Contact Vids and return a list of email addresses and for those contacts.
#I would advise limiting each group to no more than 1K contacts per request
#Will also write the entire returned JSON to a text file, stored in the same directory as this script

import requests

#enter hubspot api key and set content headers
HAPI = raw_input('Enter your HubSpot API Key: ')
user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
headers = {'Content-Type':'application/x-www-form-urlencoded','User-Agent':user_agent}

#input list of vids to get contact records
vidlist = input('Please input a properly formatted Python list of Vids. Example, enter [1234,2345,3456]: ')
vidlist2= []
for item in vidlist:
	item_str=str(item)
	vidlist2.append('vid='+item_str+'&')
vid_string = "".join(vidlist2)

#make request to the endpoint described at http://developers.hubspot.com/docs/methods/contacts/get_batch_by_vid
r = requests.get('http://api.hubapi.com/contacts/v1/contact/vids/batch/?portalId=203693'+'&'+vid_string+'property=email&'+'hapikey='+HAPI)

#print status of request
print r.status_code

#converts response JSON to Python Dictionary and then prints the email address values
contact_records = r.json()
for record in contact_records.values():
        print record['properties']['email']['value']

#Stores entire JSON response in a TXT file
with open('vids_of_restored_contacts.txt','wb') as fd:
    for chunk in r.iter_content(chunk_size=1):
        fd.write(chunk)

fd.close()
