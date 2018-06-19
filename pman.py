import podman as p


class PodmanRemote(object):
    def __init__(self):
        self.args = None
        self._address = None
        self._client = None
        self._local_path = None

    def set_args(self, args, address):
        self.args = args

    @property
    def address(self):
        return self._address

    @property
    def local_path(self):
        return self.local_path

    @property
    def client(self):
        if self._client is None:
            self._client = p.Client(self._address)
        return self._client

    @address.setter
    def address(self, address):
        self.address =  address

    @local_path.setter
    def local_path(self, path):
        self._local_path = path
