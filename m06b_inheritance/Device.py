class Device:
    def __init__(self, name, device_type, hostname, transport=None):
        self.name = name
        self.hostname = hostname
        self.device_type = device_type
        self.transport = transport

        self.mac = None
        self.ip  = None
        self.connection = None

        self.username = None
        self.password = None
        self.port = None

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def set_port(self, port): 
        self.port = port

    def connect(self):
        raise NotImplementedError("implement the connect() method")

    def get_facts(self):
        raise NotImplementedError("implement the get_facts() method")
    def disconnect(self):
        raise NotImplementedError("implement the disconnect() method")