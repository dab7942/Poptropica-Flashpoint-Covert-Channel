def get_json():
     while True:
          content = ""
          file1 = open("json_data", "r")
          count = 0
          file1.readline()
          file1.readline()
          content = file1.readline()
          file1.close()
          if '"Haunted": [2' in content:
               try:
                    return json.loads(content)
               except:
                    print(content)
                    return {}
          time.sleep(0.25)

def write_json(data_json):
     file2 = open("json_data", "w")
     file2.write("0\n")
     file2.write("json\n")
     file2.write(json.dumps(data_json))
     file2.close()


import json
import time

secret = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim. Volutpat est velit egestas dui id. Nibh mauris cursus mattis molestie a iaculis at. Elementum sagittis vitae et leo duis ut diam quam nulla. Tempus iaculis urna id volutpat lacus laoreet non curabitur. Aliquam purus sit amet luctus venenatis lectus magna fringilla. Auctor eu augue ut lectus arcu bibendum at varius vel. Gravida rutrum quisque non tellus orci ac auctor. Sed arcu non odio euismod lacinia at quis. Diam sit amet nisl suscipit adipiscing. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Suspendisse faucibus interdum posuere lorem. Sem et tortor consequat id porta nibh venenatis. Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat. Est ante in nibh mauris cursus mattis molestie a iaculis."
bytesecret = format(int.from_bytes(secret.encode(), 'big'), "b")
print(len(bytesecret))
data_json = get_json()
print(time.time())
#char = data_json['Char']
#data = char['data']
#inventory = data['inventory']
#island_keys = inventory.keys()
while True:
     data_json = get_json()
     char = data_json['Char']
     data = char['data']
     inventory = data['inventory']
     island_keys = inventory.keys()
     mel_num = 1001
     count = 0
     for island in island_keys:
          if island == "Haunted":
               if len(bytesecret) > 33:
                    inventory[island] = [1, 3]
               else:
                    inventory[island] = [1]
          elif island == "LegendarySwords":
               if len(bytesecret) > 33:
                    inventory[island] = [33]
               else:
                    inventory[island] = [len(bytesecret)]
          else:
               if bytesecret[count] == "1":
                    inventory[island] = [mel_num]
               else:
                    inventory[island] = []
               count += 1
               mel_num += 1
               if mel_num == 1027:
                    mel_num += 1
               if count == len(bytesecret):
                    break
     if len(bytesecret) < 34:
          data_json['Char']['data']['inventory']['Haunted'] = [1]
          data_json['Char']['data']['inventory']['LegendarySwords'] = [len(bytesecret)]
          write_json(data_json)
          break
     else:
          bytesecret = bytesecret[33:]
     write_json(data_json)
     time.sleep(0.25)

