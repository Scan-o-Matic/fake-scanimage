# Fake Scanner

This is a docker image that is used to create a fake scanner daemon.
Instead of trying to scan with a scanner, this deamon will simply use
existing images from past experiments.

## Installation

This repository is used to automatically build a docker image.
You can use docker to run the daemon like this:

```
docker run \
  -e SCANOMATICD_APIROOT='https://scanomatic.example.com/api' \
  -e SCANOMATICD_APIUSERNAME=<username> \
  -e SCANOMATICD_APIPASSWORD=<password> \
  -e SCANOMATICD_SCANNERID=<arbitrary-id> \
  scanomatic/fake-scanner
```

## Using more/different images

To limit its size, the (docker) image only comes with three (scanned) images. If you want to use
more or use a different set of images, you need to add them to the docker
container:

```
docker run \
  ... \
  -v /path/to/the/images:/srv/scans \
  scanomatic/fake-scanner
```
