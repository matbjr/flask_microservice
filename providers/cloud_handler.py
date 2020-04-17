from dropbox import dropbox
import json


def get_config_file(cloud_config):

    provider = cloud_config.get('cloud_host')
    filename = cloud_config.get('cloud_config_file')
    key = cloud_config.get('cloud_access_key')

    if provider == 'dropbox':
        dbx = dropbox.Dropbox(key)
        res = dbx.files_list_folder(path="")
        rv = {}
        for entry in res.entries:
            rv[entry.name] = entry
            # print(entry.name)

        md, res = dbx.files_download("/" + filename)
        data = res.content
        # print(len(data), 'bytes; md:', md)
        return json.loads(data)


if __name__ == '__main__':
    cloud_provider = {
        'cloud_host': 'dropbox',
        'cloud_config_file': 'config.json',
        'cloud_access_key': 'vDuiM-56ZzsAAAAAAAAHJGw5MRrhkkeJZ0AJhft11_SCePhuuP2XCVGY3pMGvLBn',
    }

    print(json.dumps(get_config_file(cloud_provider), indent=4))