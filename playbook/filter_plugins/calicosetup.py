from ansible import errors
from ansible.parsing.yaml.objects import AnsibleUnicode
import yaml

def set_calico_cidr(config, ips):
    try:
        if type(ips) is not str:
            if type(ips) is AnsibleUnicode:
                ips = str(ips)
            else:
                raise errors.AnsibleFilterError(f'incorrect type passed: {type(ips)}')
        content = list(yaml.safe_load_all(config))
        # For the sake of quickly setting up cidr, roughly assign value based on known content structure
        content[0]['spec']['calicoNetwork']['ipPools'][0]['cidr'] = ips
        return yaml.dump_all(content)
    except Exception as e:
        raise errors.AnsibleFilterError(e)

class FilterModule(object):
    def filters(self):
        return {
            "set_calico_cidr": set_calico_cidr
        }