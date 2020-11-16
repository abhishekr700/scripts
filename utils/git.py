import requests as r
import json

class Github:
    PAT = ""
    def __init__(self, PAT):
        self.PAT = PAT
        check = self.checkAccessToken(PAT)
        if check != False:
            raise RuntimeError("Github Auth Error")

    def checkAccessToken(self, PAT):
        res = r.get("https://api.github.com", headers = {
            "Authorization": "token {}".format(PAT)
        })
        # print(res)
        print(res.status_code)
        return res.status_code == '200'

    def addSSHKey(self, ssh_public_key):
        print("Adding KEY:", ssh_public_key)
        res = r.post("https://api.github.com/user/keys", headers = {
            "Authorization": "token {}".format(self.PAT),
            "Accept": "application/vnd.github.v3+json"
        }, data = json.dumps({
            "key": ssh_public_key
        }))
        # print(res)
        # print(res.json())
        # print({'code': res.status_code})
        # if res.status_code != 201:
        #     print("Key Could not be added")
        return res.status_code == 201

    def getSSHKeys(self):
        res = r.get("https://api.github.com/user/keys", headers = {
            "Authorization": "token {}".format(self.PAT)
        })
        print("getSSHKeys",res)
        print("getSSHKeys",res.json())

# git = Github(PAT)
# git.getSSHKeys()
# git.addSSHKey("""ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKbJpXSHoOBM0oJwjW5osopQp02LzDO1QwzpKfFbKVGO abhishekr700@gmail.com""")
# git = Github(PAT2)
# git.checkAccessToken(PAT)
# git.checkAccessToken(PAT2)