import sys

import boto
import boto.s3.connection
import ConfigParser

from sh import ceph
from datetime import datetime



def get_monmap(mapfile):
    status = ceph("mon", "getmap", o=mapfile)
    return status.exit_code == 0



if __name__ == "__main__":
    configfile = sys.argv[1]
    mapfile = "map" + datetime.now().isoformat()
    config = ConfigParser.ConfigParser()
    config.read(configfile)
    access = config.get('credentials', 'access')
    secret = config.get('credentials', 'secret')
    host = config.get('credentials', 'host')

    conn = boto.connect_s3(
            aws_access_key_id=access,
            aws_secret_access_key=secret,
            host=host,
            calling_format=boto.s3.connection.OrdinaryCallingFormat(),
    )
    bucket = conn.create_bucket("sbsmonmaps")
    if get_monmap(mapfile):
        key = bucket.new_key(mapfile)
        key.set_contents_from_filename(mapfile)
