

exceptions = dict()
def getInvalidEnvVarParamaterException(envVarName):
  if envVarName not in exceptions:
    exceptions[envVarName] = InvalidEnvVarParamaterExecption(envVarName)
  return exceptions[envVarName]

class InvalidEnvVarParamaterExecption(Exception):
  def __init__(self, envVarName):
    message = 'Invalid value for ' + envVarName
    super(InvalidEnvVarParamaterExecption, self).__init__(message)

class GlobalParamatersClass():
  LOGINEP_MODE = None
  LOGINEP_VERSION = None
  LOGINEP_LDAP_TIMEOUT = None
  LOGINEP_LDAP_HOST = None
  LOGINEP_LDAP_PORT = None
  LOGINEP_LDAP_CONSUMERCLIENTID_PREFIX = None
  LOGINEP_USER_BASE_DN = None
  LOGINEP_USER_ATTRIBUTE = None
  LOGINEP_GROUP_BASE_DN = None
  LOGINEP_GROUP_ATTRIBUTE = None
  LOGINEP_GROUP_MEMBER_FIELD = None
  LOGINEP_KONG_ADMINAPI_URL = None
  LOGINEP_SYNCACL = None
  LOGINEP_JWT_TOKEN_TIMEOUT = None
  LOGINEP_PORT = None
  LOGINEP_URL = None


  #Read environment variable or raise an exception if it is missing and there is no default
  def readFromEnviroment(self, env, envVarName, defaultValue, acceptableValues, nullValueAllowed=False):
    try:
      val = env[envVarName]
      if (acceptableValues != None):
        if (val not in acceptableValues):
          raise getInvalidEnvVarParamaterException(envVarName)
      if not nullValueAllowed:
        if val == '':
          raise getInvalidEnvVarParamaterException(envVarName)
      return val
    except KeyError:
      if (defaultValue == None):
        raise getInvalidEnvVarParamaterException(envVarName)
      return defaultValue

  def __init__(self, env):
    self.LOGINEP_MODE = self.readFromEnviroment(env, 'LOGINEP_MODE', None, ['DEVELOPER','DOCKER'])
    self.LOGINEP_VERSION = self.readFromEnviroment(env, 'LOGINEP_VERSION', None, None)
    self.LOGINEP_LDAP_TIMEOUT = self.readFromEnviroment(env, 'LOGINEP_LDAP_TIMEOUT', None, None)
    self.LOGINEP_LDAP_HOST = self.readFromEnviroment(env, 'LOGINEP_LDAP_HOST', None, None)
    self.LOGINEP_LDAP_PORT = self.readFromEnviroment(env, 'LOGINEP_LDAP_PORT', None, None)
    self.LOGINEP_LDAP_CONSUMERCLIENTID_PREFIX = self.readFromEnviroment(env, 'LOGINEP_LDAP_CONSUMERCLIENTID_PREFIX', None, None)
    self.LOGINEP_USER_BASE_DN = self.readFromEnviroment(env, 'LOGINEP_USER_BASE_DN', None, None)
    self.LOGINEP_USER_ATTRIBUTE = self.readFromEnviroment(env, 'LOGINEP_USER_ATTRIBUTE', None, None)
    self.LOGINEP_GROUP_BASE_DN = self.readFromEnviroment(env, 'LOGINEP_GROUP_BASE_DN', None, None)
    self.LOGINEP_GROUP_ATTRIBUTE = self.readFromEnviroment(env, 'LOGINEP_GROUP_ATTRIBUTE', None, None)
    self.LOGINEP_GROUP_MEMBER_FIELD = self.readFromEnviroment(env, 'LOGINEP_GROUP_MEMBER_FIELD', None, None)
    self.LOGINEP_KONG_ADMINAPI_URL = self.readFromEnviroment(env, 'LOGINEP_KONG_ADMINAPI_URL', None, None, nullValueAllowed=True)
    self.LOGINEP_SYNCACL = self.readFromEnviroment(env, 'LOGINEP_SYNCACL', None, None, nullValueAllowed=True)
    self.LOGINEP_JWT_TOKEN_TIMEOUT = self.readFromEnviroment(env, 'LOGINEP_JWT_TOKEN_TIMEOUT', None, None)
    self.LOGINEP_URL = self.readFromEnviroment(env, 'LOGINEP_URL', None, None)
    LOGINEP_PORTSTR = self.readFromEnviroment(env, 'LOGINEP_PORT', '80', None)
    try:
      self.LOGINEP_PORT = int(LOGINEP_PORTSTR)
    except:
      raise Exception('LOGINEP_PORT must be an integer')

  def getStartupOutput(self):
    r = 'Starting kong_ldap_login_endpoint vertion:' + self.LOGINEP_VERSION + '\n'
    r += 'LOGINEP_MODE:' + self.LOGINEP_MODE + '\n'
    r += 'LOGINEP_LDAP_TIMEOUT:' + self.LOGINEP_LDAP_TIMEOUT + '\n'
    r += 'LOGINEP_LDAP_HOST:' + self.LOGINEP_LDAP_HOST + '\n'
    r += 'LOGINEP_LDAP_PORT:' + self.LOGINEP_LDAP_PORT + '\n'
    r += 'LOGINEP_LDAP_CONSUMERCLIENTID_PREFIX:' + self.LOGINEP_LDAP_CONSUMERCLIENTID_PREFIX + '\n'
    r += 'LOGINEP_USER_BASE_DN:' + self.LOGINEP_USER_BASE_DN + '\n'
    r += 'LOGINEP_USER_ATTRIBUTE:' + self.LOGINEP_USER_ATTRIBUTE + '\n'
    r += 'LOGINEP_GROUP_BASE_DN:' + self.LOGINEP_GROUP_BASE_DN + '\n'
    r += 'LOGINEP_GROUP_ATTRIBUTE:' + self.LOGINEP_GROUP_ATTRIBUTE + '\n'
    r += 'LOGINEP_GROUP_MEMBER_FIELD:' + self.LOGINEP_GROUP_MEMBER_FIELD + '\n'
    r += 'LOGINEP_KONG_ADMINAPI_URL:' + self.LOGINEP_KONG_ADMINAPI_URL + '\n'
    r += 'LOGINEP_SYNCACL:' + self.LOGINEP_SYNCACL + '\n'
    r += 'LOGINEP_JWT_TOKEN_TIMEOUT:' + self.LOGINEP_JWT_TOKEN_TIMEOUT + '\n'
    r += 'LOGINEP_URL:' + self.LOGINEP_URL + '\n'
    return r

  def getDeveloperMode(self):
    return (self.LOGINEP_MODE == 'DEVELOPER')