import ipinfo
from ipinfo.details import Details

class Requests:
    def __init__(self, *arg, **kwargs):
        pass

    @staticmethod
    def get_geography(token: str=None, ip: str=None) -> Details:
        try:
            ip_handler = ipinfo.getHandler(token)
            ip_details = ip_handler.getDetails(ip)
        except:
            raise Exception("failed to get geography")

        # ip_details.city    => 'Fullerton'
        # ip_details.country => 'US'
        # ip_details.loc     => '33.870404, -117.924282'
        return ip_details