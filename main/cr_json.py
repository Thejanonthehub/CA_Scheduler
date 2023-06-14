#Creating output json file
def js(dic):
    import date_booking
    import json
    # Open a file in write mode
    with open('out.json', 'w') as outfile:
        # Write the JSON object to the file
        json.dump(dic, outfile)

