import requests
from ast import literal_eval

class ldapClass():
  appObj = None
  def __init__(self, appObj):
    self.appObj = appObj

  falseReturn = { 'Authed': False, 'Groups': []}
  def verifyCredentials(self,username,password):
    if username is None:
      return self.falseReturn
    if password is None:
      return self.falseReturn
    username = username.strip()
    password = password.strip()
    if username == "":
      return self.falseReturn
    if password == "":
      return self.falseReturn

    req = requests.post(self.appObj.globalParamObject.LOGINEP_URL, data = {'username': username, 'password': password})
    resp = req.json()

    groups = ['Development']

    if req.status_code == 200 and resp['result'] == True:
      return { 'Authed': True, 'Groups': groups}
    else:
      return self.falseReturn