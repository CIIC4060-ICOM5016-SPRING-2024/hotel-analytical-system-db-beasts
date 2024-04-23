import matplotlib.pyplot as plt
import requests
import json


def see_leastrooms():
    flask_url = "http://127.0.0.1:5000/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/least/rooms"
    data = {'eid': 3}
    response = requests.post(flask_url, json=data)
    return response


items = see_leastrooms()
datas = items.json()['Least_Rooms']

# ** x axis values
x = [str(x['cname']) for x in datas]
# ** y axis values
y = [int(y['total rooms']) for y in datas]

# ** creating the bar plot
plt.bar(x, y, color='black')

plt.ylim(0, max(y) + min(y))

# ** naming the x-axis
plt.xlabel('x - axis = Chains')
# ** naming the y-axis
plt.ylabel('y - axis = Total Rooms')

# ** giving a title to my graph
plt.title('Top 3 chain with the least rooms')

# ** Tight layout to avoid overlap
plt.tight_layout()

# ** function to show the plot
plt.show()

# ** See data
json_str = json.dumps(datas, indent=2)
lines = json_str.split('\n')
for line in lines:
    print(line)

