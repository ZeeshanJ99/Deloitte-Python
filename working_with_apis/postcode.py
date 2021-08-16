import json

class PostCode:
    #postcode json dict = api_call.json()["result"]
    def __init__(self, postcode_json_dict):
        self.postcode = postcode_json_dict["postcode"]
        self.latitude = postcode_json_dict["latitude"]
        self.longitude = postcode_json_dict["longitude"]
        self.eastings = postcode_json_dict["eastings"]
        self.northings = postcode_json_dict["northings"]

    def get_location(self, en=False):
        if en:
            return self.eastings, self.northings
        else:
            return self.latitude, self.longitude


    def __repr__(self):
        return f"<PostCode({self.postcode})>"


    # postcode
# lat long eastings northings as attributes
# __repr__ so that postcode shows so when print, tells you what postcode is

