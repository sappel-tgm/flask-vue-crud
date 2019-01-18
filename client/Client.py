import requests
import json

if __name__ == "__main__":
    getInput = requests.get("http://localhost:8080/ping")
    data = json.loads(getInput.text)
    if data != None:
      print(data)
    else:
      print("Data Null")
