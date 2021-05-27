#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/jinja2/")
def ciscoios():
    groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]
    #qparms = {}
    #i=0
    #for plist in groups:
     #  qparms[f'ip{i}'] = plist["ip"]
     #  qparms[f'fqdn{str(i)}'] = plist["fqdn"]
     #  qparms[f'hostname{str(i)}'] = plist["hostname"]
     #  i += 1
   # qparms['count'] = i-1
    try:

        # render template and save as baseIOS.conf
        return render_template("jinja2Challenge.html", groups = groups)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

