* Monitor Map tool

This is a simple tool to extract monitor maps from ceph and upload
them to a configured object store. The script needs to be triggerred
by a cronjob at a frequency of daily or weekly

* Usage

Credentials need to be stored in a config file. The script needs to be
invoked as

```
./ceph_mon_maps.py path/to/config/file
```

The config file is a simple file having s3 credentials as variables in
the below format

```
[credentials]
access='access_key'
secret='secret'
host='s3host'
```

