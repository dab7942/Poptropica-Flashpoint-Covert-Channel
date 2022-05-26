def get_json(first):
     while True:
          content = ""
          file1 = open("json_data", "r")
          count = 0
          file1.readline()
          file1.readline()
          content = file1.readline()
          file1.close()
          if '"Haunted": [1' in content or first:
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

data_json = get_json(True)
data_json['Char']['data']['inventory']['Haunted'] = [2]
write_json(data_json)
time.sleep(0.25)
secret = ""
while True:
     data_json = get_json(False)
     this_batch = ""
     char = data_json['Char']
     data = char['data']
     inventory = data['inventory']
     island_keys = inventory.keys()
     total = inventory["LegendarySwords"][0]
     count = 1
     end = True
     for island in island_keys:
          if island == "Haunted":
               if 3 in inventory[island]:
                    end = False
                    inventory[island] = [2]
               else:
                    inventory[island] = []
          elif island == "LegendarySwords":
               continue
          else:
               mel_num = 1000 + count
               invt = inventory[island]
               if mel_num in invt:
                    this_batch += "1"
               else:
                    this_batch += "0"
               count += 1
               if count == 27:
                    count += 1
               if len(this_batch) == total:
                    secret += this_batch
                    break
     write_json(data_json)
     if end:
          print(time.time())
          break
     time.sleep(0.25)
partial = int(secret, 2)
true_secret = partial.to_bytes((partial.bit_length() + 7) // 8, 'big').decode()
print(true_secret)

