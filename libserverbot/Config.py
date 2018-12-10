

class Config():

    def __init__(self):
        self.name = None
        self.token = None
        self.authorized_users = []

        self.available_cmd = []
        self.commands = []
        self.disks = []
        self.available_slaves = []
        self.slaves = []


    def set(self, config):

        self.token = config['telegram']['token']
        self.name = config['server']['name']
        
        for uid, username in config.items('telegram:authorized_users'):
            self.authorized_users.append(username)

        for cid, cmd in config.items('server:cmd'):
            self.available_cmd.append(cid)
            self.commands.append({'name': cid, 'cmd': cmd})

        for did, path in config.items('server:disks'):
            self.disks.append({'name': did, 'path': path})

        for mid, mac in config.items('wakeonlan'):
            self.available_slaves.append(mid)
            self.slaves.append({'name': mid, 'mac': mac})

    def get_mac(self, name):

        for slave in self.slaves:
            if slave['name'] == name:
                return slave['mac']


    def get_cmd(self, name):

        for command in self.commands:
            if command['name'] == name:
                return command['cmd']