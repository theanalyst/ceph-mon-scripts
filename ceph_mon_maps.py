import boto
import boto.s3.connection

from sh import ceph
from datetime import datetime


def get_monmap(mapfile):
    status = ceph("mon", "getmap", o=mapfile)
    return status.exit_code == 0

if __name__ == "__main__":
    mapfile = "map" + datetime.now().isoformat()
    access = 'some access'  # replace with argparse & cfgparse
    secret = 'some secret'
    host = 's3.amazonaws.com'
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
