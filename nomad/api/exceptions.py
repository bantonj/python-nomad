class BaseNomadException(Exception):
    """General Error occurred when interacting with nomad API"""
    def __init__(self, nomad_resp):
        if nomad_resp is not None:
            print("Nomad Status: {status}".format(
                status=nomad_resp.status_code))
            print("Nomad Response: {resp}".format(resp=nomad_resp.text))


class URLNotFoundNomadException(Exception):
    """The requeted URL given does not exist"""
    def __init__(self, nomad_resp):
        if nomad_resp is not None:
            print("Nomad Status: {status}".format(
                status=nomad_resp.status_code))
            print("Nomad Response: {resp}".format(resp=nomad_resp.text))
