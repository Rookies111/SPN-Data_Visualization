import requests
import json

url = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all"
response = requests.get(url).text
response_info = json.loads(response)
print(len(response_info))
print(response_info[1]["new_case"])

def allTimeData(key):
    allTimeData_list = []
    for i in range(len(response_info)):
        allTimeData_list.append(response_info[i][key])
    print("all time", key, allTimeData_list)

def weeklyData(week, key):
    weeklyData_list = []
    weeklyData_list.append(response_info[week][key])
    print("week", week ,key, response_info[week][key])

allTimeData("new_case")
allTimeData("new_recovered")
allTimeData("new_death")
print('')
week = 3
weeklyData(week, "new_case")
weeklyData(week, "new_recovered")
weeklyData(week, "new_death")

