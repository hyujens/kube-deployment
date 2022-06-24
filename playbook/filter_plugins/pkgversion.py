from ansible import errors

def shorten_kubelet_version(version):
    if version[0] is not 'v':
        raise errors.AnsibleFilterError(f'kubelet version may get changed. {version} is not recognizable ...')

    return version[1:version.rindex('.')]

def shorten_version(version, app):
    if app is 'kubelet':
        return shorten_kubelet_version(version)
    else:
        raise errors.AnsibleFilterError(f'No implementation of shortening {app} version ...')

class FilterModule(object):
    def filters(self):
        return {'shorten_version': shorten_version}