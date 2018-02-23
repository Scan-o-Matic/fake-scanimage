FROM scanomatic/scanner
COPY src/scanimage /usr/bin/
COPY src/data /srv/scans
ENV FAKE_SCANIMAGE_DATA=/srv/scans
