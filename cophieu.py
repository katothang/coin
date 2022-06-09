import requests
import json
from bs4 import BeautifulSoup
from flask import Flask
from flask import request as param

app = Flask(__name__)
@app.route('/daycophieu', methods=['GET'])
def dayCoPhieu():
    if param.args.get('keyword') is None or param.args.get('d') is None:
        return "{}";

    url = "https://www.cophieu68.vn/atbottom.php?keyword="+param.args.get('keyword')+"&d="+param.args.get('d')
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    bodyTable = soup.select(".td_bottom3")
    bodyTableArr = [];
    for x in bodyTable:
        bodyTableArr.append(x.text.strip())
    return json.dumps(bodyTableArr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
