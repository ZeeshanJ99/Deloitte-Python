import requests
import json
from pprint import pprint
from postcode import PostCode

postcode_url = "https://api.postcodes.io/postcodes/"
postcode_request = requests.get(postcode_url + "B74BB")

# print(postcode_request, type(postcode_request))


#http status code - 200 means ok, 404 - page not found

# print(postcode_request.status_code == 200)
# print(postcode_request.headers, type(postcode_request.headers)) - contain metadata - data about the data e.g. date time, content type
# print(postcode_request.content, type(postcode_request)) binary string that contains data

# print(postcode_request.json())
# print(type(postcode_request.json()))
#
# pc = postcode_request.json()
# pprint(pc, sort_dicts=False)
# # print(pc["longitude"], pc["latitude"])


postcodes = {"postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]}
body = json.dumps(postcodes)
headers = {"Content-Type": "application/json"}

multi_pc_req = requests.post(postcode_url, headers=headers, data=body)
print(multi_pc_req)
multi_pc = multi_pc_req.json()["result"]
pprint(multi_pc, sort_dicts=False)


# print each postcode followed by its lat and long

for postcode in multi_pc:
    result = postcode["result"]
    pprint(f"""  Postcode:{result["postcode"]}
    Latitude: {result["latitude"]}
    Longitude: {result["longitude"]}
""")



for postcode in multi_pc:
    pc = PostCode(postcode["result"])
    print(pc)
    print(pc.get_location(en=True))

