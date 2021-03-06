# Make good use of the cache
- Get the new package list with "apt-get update".
  - The package lists obtained by update will be reused in subsequent RUN.
- Use chache when maintainning Docker file
- After maintenance, write RUN together
  

# Create Dockerfile
```
FROM ubuntu:latest

# For example install the curl and nginx packages
RUN apt-get update && apt-get install -y \
    curl \
    nginx

```

- docker build
  - <details>
    <summary>Result</summary>

    ```
    >>> docker build .
    Sending build context to Docker daemon  37.89kB
    Step 1/2 : FROM ubuntu:latest
    ---> f643c72bc252
    Step 2/2 : RUN apt-get update && apt-get install -y     curl     nginx
    ---> Running in 7f5566ddec31
    Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
    Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [109 kB]
    Get:3 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [1167 B]
    Get:4 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [103 kB]
    Get:5 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [645 kB]
    Get:6 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
    Get:7 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [495 kB]
    Get:8 http://archive.ubuntu.com/ubuntu focal-backports InRelease [101 kB]
    Get:9 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]
    Get:10 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1275 kB]
    Get:11 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]
    Get:12 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
    Get:13 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [885 kB]
    Get:14 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [885 kB]
    Get:15 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [30.4 kB]
    Get:16 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [136 kB]
    Get:17 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [4250 B]
    Fetched 16.6 MB in 15s (1129 kB/s)
    Reading package lists...
    Reading package lists...
    Building dependency tree...
    Reading state information...
    The following additional packages will be installed:
    ca-certificates fontconfig-config fonts-dejavu-core iproute2 krb5-locales
    libasn1-8-heimdal libatm1 libbrotli1 libbsd0 libcap2 libcap2-bin libcurl4
    libelf1 libexpat1 libfontconfig1 libfreetype6 libgd3 libgssapi-krb5-2
    libgssapi3-heimdal libhcrypto4-heimdal libheimbase1-heimdal
    libheimntlm0-heimdal libhx509-5-heimdal libicu66 libjbig0 libjpeg-turbo8
    libjpeg8 libk5crypto3 libkeyutils1 libkrb5-26-heimdal libkrb5-3
    libkrb5support0 libldap-2.4-2 libldap-common libmnl0 libnghttp2-14
    libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
    libnginx-mod-mail libnginx-mod-stream libpam-cap libpng16-16 libpsl5
    libroken18-heimdal librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db
    libsqlite3-0 libssh-4 libssl1.1 libtiff5 libwebp6 libwind0-heimdal libx11-6
    libx11-data libxau6 libxcb1 libxdmcp6 libxml2 libxpm4 libxslt1.1
    libxtables12 nginx-common nginx-core openssl publicsuffix tzdata ucf
    Suggested packages:
    iproute2-doc libgd-tools krb5-doc krb5-user libsasl2-modules-gssapi-mit
    | libsasl2-modules-gssapi-heimdal libsasl2-modules-ldap libsasl2-modules-otp
    libsasl2-modules-sql fcgiwrap nginx-doc ssl-cert
    The following NEW packages will be installed:
    ca-certificates curl fontconfig-config fonts-dejavu-core iproute2
    krb5-locales libasn1-8-heimdal libatm1 libbrotli1 libbsd0 libcap2
    libcap2-bin libcurl4 libelf1 libexpat1 libfontconfig1 libfreetype6 libgd3
    libgssapi-krb5-2 libgssapi3-heimdal libhcrypto4-heimdal libheimbase1-heimdal
    libheimntlm0-heimdal libhx509-5-heimdal libicu66 libjbig0 libjpeg-turbo8
    libjpeg8 libk5crypto3 libkeyutils1 libkrb5-26-heimdal libkrb5-3
    libkrb5support0 libldap-2.4-2 libldap-common libmnl0 libnghttp2-14
    libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
    libnginx-mod-mail libnginx-mod-stream libpam-cap libpng16-16 libpsl5
    libroken18-heimdal librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db
    libsqlite3-0 libssh-4 libssl1.1 libtiff5 libwebp6 libwind0-heimdal libx11-6
    libx11-data libxau6 libxcb1 libxdmcp6 libxml2 libxpm4 libxslt1.1
    libxtables12 nginx nginx-common nginx-core openssl publicsuffix tzdata ucf
    0 upgraded, 71 newly installed, 0 to remove and 2 not upgraded.
    Need to get 19.9 MB of archives.
    After this operation, 73.4 MB of additional disk space will be used.
    Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libssl1.1 amd64 1.1.1f-1ubuntu2.1 [1319 kB]
    Get:2 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 openssl amd64 1.1.1f-1ubuntu2.1 [620 kB]
    Get:3 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 ca-certificates all 20201027ubuntu0.20.04.1 [153 kB]
    Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 libbsd0 amd64 0.10.0-1 [45.4 kB]
    Get:5 http://archive.ubuntu.com/ubuntu focal/main amd64 libcap2 amd64 1:2.32-1 [15.9 kB]
    Get:6 http://archive.ubuntu.com/ubuntu focal/main amd64 libelf1 amd64 0.176-1.1build1 [44.0 kB]
    Get:7 http://archive.ubuntu.com/ubuntu focal/main amd64 libmnl0 amd64 1.0.4-2 [12.3 kB]
    Get:8 http://archive.ubuntu.com/ubuntu focal/main amd64 libxtables12 amd64 1.8.4-3ubuntu2 [28.4 kB]
    Get:9 http://archive.ubuntu.com/ubuntu focal/main amd64 libcap2-bin amd64 1:2.32-1 [26.2 kB]
    Get:10 http://archive.ubuntu.com/ubuntu focal/main amd64 iproute2 amd64 5.5.0-1ubuntu1 [858 kB]
    Get:11 http://archive.ubuntu.com/ubuntu focal/main amd64 libatm1 amd64 1:2.5.1-4 [21.8 kB]
    Get:12 http://archive.ubuntu.com/ubuntu focal/main amd64 libexpat1 amd64 2.2.9-1build1 [73.3 kB]
    Get:13 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 tzdata all 2020d-0ubuntu0.20.04 [294 kB]
    Get:14 http://archive.ubuntu.com/ubuntu focal/main amd64 libicu66 amd64 66.1-2ubuntu2 [8520 kB]
    Get:15 http://archive.ubuntu.com/ubuntu focal/main amd64 libpam-cap amd64 1:2.32-1 [8352 B]
    Get:16 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libsqlite3-0 amd64 3.31.1-4ubuntu0.2 [549 kB]
    Get:17 http://archive.ubuntu.com/ubuntu focal/main amd64 libxml2 amd64 2.9.10+dfsg-5 [640 kB]
    Get:18 http://archive.ubuntu.com/ubuntu focal/main amd64 ucf all 3.0038+nmu1 [51.6 kB]
    Get:19 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 krb5-locales all 1.17-6ubuntu4.1 [11.4 kB]
    Get:20 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libkrb5support0 amd64 1.17-6ubuntu4.1 [30.9 kB]
    Get:21 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libk5crypto3 amd64 1.17-6ubuntu4.1 [79.9 kB]
    Get:22 http://archive.ubuntu.com/ubuntu focal/main amd64 libkeyutils1 amd64 1.6-6ubuntu1 [10.2 kB]
    Get:23 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libkrb5-3 amd64 1.17-6ubuntu4.1 [330 kB]
    Get:24 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libgssapi-krb5-2 amd64 1.17-6ubuntu4.1 [121 kB]
    Get:25 http://archive.ubuntu.com/ubuntu focal/main amd64 libpng16-16 amd64 1.6.37-2 [179 kB]
    Get:26 http://archive.ubuntu.com/ubuntu focal/main amd64 libpsl5 amd64 0.21.0-1ubuntu1 [51.5 kB]
    Get:27 http://archive.ubuntu.com/ubuntu focal/main amd64 libxau6 amd64 1:1.0.9-0ubuntu1 [7488 B]
    Get:28 http://archive.ubuntu.com/ubuntu focal/main amd64 libxdmcp6 amd64 1:1.1.3-0ubuntu1 [10.6 kB]
    Get:29 http://archive.ubuntu.com/ubuntu focal/main amd64 libxcb1 amd64 1.14-2 [44.7 kB]
    Get:30 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libx11-data all 2:1.6.9-2ubuntu1.1 [113 kB]
    Get:31 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libx11-6 amd64 2:1.6.9-2ubuntu1.1 [574 kB]
    Get:32 http://archive.ubuntu.com/ubuntu focal/main amd64 publicsuffix all 20200303.0012-1 [111 kB]
    Get:33 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libbrotli1 amd64 1.0.7-6ubuntu0.1 [267 kB]
    Get:34 http://archive.ubuntu.com/ubuntu focal/main amd64 libroken18-heimdal amd64 7.7.0+dfsg-1ubuntu1 [41.8 kB]
    Get:35 http://archive.ubuntu.com/ubuntu focal/main amd64 libasn1-8-heimdal amd64 7.7.0+dfsg-1ubuntu1 [181 kB]
    Get:36 http://archive.ubuntu.com/ubuntu focal/main amd64 libheimbase1-heimdal amd64 7.7.0+dfsg-1ubuntu1 [29.7 kB]
    Get:37 http://archive.ubuntu.com/ubuntu focal/main amd64 libhcrypto4-heimdal amd64 7.7.0+dfsg-1ubuntu1 [87.9 kB]
    Get:38 http://archive.ubuntu.com/ubuntu focal/main amd64 libwind0-heimdal amd64 7.7.0+dfsg-1ubuntu1 [48.0 kB]
    Get:39 http://archive.ubuntu.com/ubuntu focal/main amd64 libhx509-5-heimdal amd64 7.7.0+dfsg-1ubuntu1 [107 kB]
    Get:40 http://archive.ubuntu.com/ubuntu focal/main amd64 libkrb5-26-heimdal amd64 7.7.0+dfsg-1ubuntu1 [208 kB]
    Get:41 http://archive.ubuntu.com/ubuntu focal/main amd64 libheimntlm0-heimdal amd64 7.7.0+dfsg-1ubuntu1 [15.1 kB]
    Get:42 http://archive.ubuntu.com/ubuntu focal/main amd64 libgssapi3-heimdal amd64 7.7.0+dfsg-1ubuntu1 [96.1 kB]
    Get:43 http://archive.ubuntu.com/ubuntu focal/main amd64 libsasl2-modules-db amd64 2.1.27+dfsg-2 [14.9 kB]
    Get:44 http://archive.ubuntu.com/ubuntu focal/main amd64 libsasl2-2 amd64 2.1.27+dfsg-2 [49.3 kB]
    Get:45 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libldap-common all 2.4.49+dfsg-2ubuntu1.5 [16.8 kB]
    Get:46 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libldap-2.4-2 amd64 2.4.49+dfsg-2ubuntu1.5 [155 kB]
    Get:47 http://archive.ubuntu.com/ubuntu focal/main amd64 libnghttp2-14 amd64 1.40.0-1build1 [78.7 kB]
    Get:48 http://archive.ubuntu.com/ubuntu focal/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2build1 [54.9 kB]
    Get:49 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libssh-4 amd64 0.9.3-2ubuntu2.1 [170 kB]
    Get:50 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libcurl4 amd64 7.68.0-1ubuntu2.4 [234 kB]
    Get:51 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 curl amd64 7.68.0-1ubuntu2.4 [161 kB]
    Get:52 http://archive.ubuntu.com/ubuntu focal/main amd64 fonts-dejavu-core all 2.37-1 [1041 kB]
    Get:53 http://archive.ubuntu.com/ubuntu focal/main amd64 fontconfig-config all 2.13.1-2ubuntu3 [28.8 kB]
    Get:54 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libfreetype6 amd64 2.10.1-2ubuntu0.1 [341 kB]
    Get:55 http://archive.ubuntu.com/ubuntu focal/main amd64 libfontconfig1 amd64 2.13.1-2ubuntu3 [114 kB]
    Get:56 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libjpeg-turbo8 amd64 2.0.3-0ubuntu1.20.04.1 [117 kB]
    Get:57 http://archive.ubuntu.com/ubuntu focal/main amd64 libjpeg8 amd64 8c-2ubuntu8 [2194 B]
    Get:58 http://archive.ubuntu.com/ubuntu focal/main amd64 libjbig0 amd64 2.1-3.1build1 [26.7 kB]
    Get:59 http://archive.ubuntu.com/ubuntu focal/main amd64 libwebp6 amd64 0.6.1-2 [185 kB]
    Get:60 http://archive.ubuntu.com/ubuntu focal/main amd64 libtiff5 amd64 4.1.0+git191117-2build1 [161 kB]
    Get:61 http://archive.ubuntu.com/ubuntu focal/main amd64 libxpm4 amd64 1:3.5.12-1 [34.0 kB]
    Get:62 http://archive.ubuntu.com/ubuntu focal/main amd64 libgd3 amd64 2.2.5-5.2ubuntu2 [118 kB]
    Get:63 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx-common all 1.18.0-0ubuntu1 [37.3 kB]
    Get:64 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-http-image-filter amd64 1.18.0-0ubuntu1 [14.3 kB]
    Get:65 http://archive.ubuntu.com/ubuntu focal/main amd64 libxslt1.1 amd64 1.1.34-4 [152 kB]
    Get:66 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-http-xslt-filter amd64 1.18.0-0ubuntu1 [12.6 kB]
    Get:67 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-mail amd64 1.18.0-0ubuntu1 [42.3 kB]
    Get:68 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-stream amd64 1.18.0-0ubuntu1 [66.9 kB]
    Get:69 http://archive.ubuntu.com/ubuntu focal/main amd64 libsasl2-modules amd64 2.1.27+dfsg-2 [49.1 kB]
    Get:70 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx-core amd64 1.18.0-0ubuntu1 [425 kB]
    Get:71 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx all 1.18.0-0ubuntu1 [3624 B]
    debconf: delaying package configuration, since apt-utils is not installed
    Fetched 19.9 MB in 15s (1289 kB/s)
    Selecting previously unselected package libssl1.1:amd64.
    (Reading database ... 4121 files and directories currently installed.)
    Preparing to unpack .../00-libssl1.1_1.1.1f-1ubuntu2.1_amd64.deb ...
    Unpacking libssl1.1:amd64 (1.1.1f-1ubuntu2.1) ...
    Selecting previously unselected package openssl.
    Preparing to unpack .../01-openssl_1.1.1f-1ubuntu2.1_amd64.deb ...
    Unpacking openssl (1.1.1f-1ubuntu2.1) ...
    Selecting previously unselected package ca-certificates.
    Preparing to unpack .../02-ca-certificates_20201027ubuntu0.20.04.1_all.deb ...
    Unpacking ca-certificates (20201027ubuntu0.20.04.1) ...
    Selecting previously unselected package libbsd0:amd64.
    Preparing to unpack .../03-libbsd0_0.10.0-1_amd64.deb ...
    Unpacking libbsd0:amd64 (0.10.0-1) ...
    Selecting previously unselected package libcap2:amd64.
    Preparing to unpack .../04-libcap2_1%3a2.32-1_amd64.deb ...
    Unpacking libcap2:amd64 (1:2.32-1) ...
    Selecting previously unselected package libelf1:amd64.
    Preparing to unpack .../05-libelf1_0.176-1.1build1_amd64.deb ...
    Unpacking libelf1:amd64 (0.176-1.1build1) ...
    Selecting previously unselected package libmnl0:amd64.
    Preparing to unpack .../06-libmnl0_1.0.4-2_amd64.deb ...
    Unpacking libmnl0:amd64 (1.0.4-2) ...
    Selecting previously unselected package libxtables12:amd64.
    Preparing to unpack .../07-libxtables12_1.8.4-3ubuntu2_amd64.deb ...
    Unpacking libxtables12:amd64 (1.8.4-3ubuntu2) ...
    Selecting previously unselected package libcap2-bin.
    Preparing to unpack .../08-libcap2-bin_1%3a2.32-1_amd64.deb ...
    Unpacking libcap2-bin (1:2.32-1) ...
    Selecting previously unselected package iproute2.
    Preparing to unpack .../09-iproute2_5.5.0-1ubuntu1_amd64.deb ...
    Unpacking iproute2 (5.5.0-1ubuntu1) ...
    Selecting previously unselected package libatm1:amd64.
    Preparing to unpack .../10-libatm1_1%3a2.5.1-4_amd64.deb ...
    Unpacking libatm1:amd64 (1:2.5.1-4) ...
    Selecting previously unselected package libexpat1:amd64.
    Preparing to unpack .../11-libexpat1_2.2.9-1build1_amd64.deb ...
    Unpacking libexpat1:amd64 (2.2.9-1build1) ...
    Selecting previously unselected package tzdata.
    Preparing to unpack .../12-tzdata_2020d-0ubuntu0.20.04_all.deb ...
    Unpacking tzdata (2020d-0ubuntu0.20.04) ...
    Selecting previously unselected package libicu66:amd64.
    Preparing to unpack .../13-libicu66_66.1-2ubuntu2_amd64.deb ...
    Unpacking libicu66:amd64 (66.1-2ubuntu2) ...
    Selecting previously unselected package libpam-cap:amd64.
    Preparing to unpack .../14-libpam-cap_1%3a2.32-1_amd64.deb ...
    Unpacking libpam-cap:amd64 (1:2.32-1) ...
    Selecting previously unselected package libsqlite3-0:amd64.
    Preparing to unpack .../15-libsqlite3-0_3.31.1-4ubuntu0.2_amd64.deb ...
    Unpacking libsqlite3-0:amd64 (3.31.1-4ubuntu0.2) ...
    Selecting previously unselected package libxml2:amd64.
    Preparing to unpack .../16-libxml2_2.9.10+dfsg-5_amd64.deb ...
    Unpacking libxml2:amd64 (2.9.10+dfsg-5) ...
    Selecting previously unselected package ucf.
    Preparing to unpack .../17-ucf_3.0038+nmu1_all.deb ...
    Moving old data out of the way
    Unpacking ucf (3.0038+nmu1) ...
    Selecting previously unselected package krb5-locales.
    Preparing to unpack .../18-krb5-locales_1.17-6ubuntu4.1_all.deb ...
    Unpacking krb5-locales (1.17-6ubuntu4.1) ...
    Selecting previously unselected package libkrb5support0:amd64.
    Preparing to unpack .../19-libkrb5support0_1.17-6ubuntu4.1_amd64.deb ...
    Unpacking libkrb5support0:amd64 (1.17-6ubuntu4.1) ...
    Selecting previously unselected package libk5crypto3:amd64.
    Preparing to unpack .../20-libk5crypto3_1.17-6ubuntu4.1_amd64.deb ...
    Unpacking libk5crypto3:amd64 (1.17-6ubuntu4.1) ...
    Selecting previously unselected package libkeyutils1:amd64.
    Preparing to unpack .../21-libkeyutils1_1.6-6ubuntu1_amd64.deb ...
    Unpacking libkeyutils1:amd64 (1.6-6ubuntu1) ...
    Selecting previously unselected package libkrb5-3:amd64.
    Preparing to unpack .../22-libkrb5-3_1.17-6ubuntu4.1_amd64.deb ...
    Unpacking libkrb5-3:amd64 (1.17-6ubuntu4.1) ...
    Selecting previously unselected package libgssapi-krb5-2:amd64.
    Preparing to unpack .../23-libgssapi-krb5-2_1.17-6ubuntu4.1_amd64.deb ...
    Unpacking libgssapi-krb5-2:amd64 (1.17-6ubuntu4.1) ...
    Selecting previously unselected package libpng16-16:amd64.
    Preparing to unpack .../24-libpng16-16_1.6.37-2_amd64.deb ...
    Unpacking libpng16-16:amd64 (1.6.37-2) ...
    Selecting previously unselected package libpsl5:amd64.
    Preparing to unpack .../25-libpsl5_0.21.0-1ubuntu1_amd64.deb ...
    Unpacking libpsl5:amd64 (0.21.0-1ubuntu1) ...
    Selecting previously unselected package libxau6:amd64.
    Preparing to unpack .../26-libxau6_1%3a1.0.9-0ubuntu1_amd64.deb ...
    Unpacking libxau6:amd64 (1:1.0.9-0ubuntu1) ...
    Selecting previously unselected package libxdmcp6:amd64.
    Preparing to unpack .../27-libxdmcp6_1%3a1.1.3-0ubuntu1_amd64.deb ...
    Unpacking libxdmcp6:amd64 (1:1.1.3-0ubuntu1) ...
    Selecting previously unselected package libxcb1:amd64.
    Preparing to unpack .../28-libxcb1_1.14-2_amd64.deb ...
    Unpacking libxcb1:amd64 (1.14-2) ...
    Selecting previously unselected package libx11-data.
    Preparing to unpack .../29-libx11-data_2%3a1.6.9-2ubuntu1.1_all.deb ...
    Unpacking libx11-data (2:1.6.9-2ubuntu1.1) ...
    Selecting previously unselected package libx11-6:amd64.
    Preparing to unpack .../30-libx11-6_2%3a1.6.9-2ubuntu1.1_amd64.deb ...
    Unpacking libx11-6:amd64 (2:1.6.9-2ubuntu1.1) ...
    Selecting previously unselected package publicsuffix.
    Preparing to unpack .../31-publicsuffix_20200303.0012-1_all.deb ...
    Unpacking publicsuffix (20200303.0012-1) ...
    Selecting previously unselected package libbrotli1:amd64.
    Preparing to unpack .../32-libbrotli1_1.0.7-6ubuntu0.1_amd64.deb ...
    Unpacking libbrotli1:amd64 (1.0.7-6ubuntu0.1) ...
    Selecting previously unselected package libroken18-heimdal:amd64.
    Preparing to unpack .../33-libroken18-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libroken18-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libasn1-8-heimdal:amd64.
    Preparing to unpack .../34-libasn1-8-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libasn1-8-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libheimbase1-heimdal:amd64.
    Preparing to unpack .../35-libheimbase1-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libheimbase1-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libhcrypto4-heimdal:amd64.
    Preparing to unpack .../36-libhcrypto4-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libhcrypto4-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libwind0-heimdal:amd64.
    Preparing to unpack .../37-libwind0-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libwind0-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libhx509-5-heimdal:amd64.
    Preparing to unpack .../38-libhx509-5-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libhx509-5-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libkrb5-26-heimdal:amd64.
    Preparing to unpack .../39-libkrb5-26-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libkrb5-26-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libheimntlm0-heimdal:amd64.
    Preparing to unpack .../40-libheimntlm0-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libheimntlm0-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libgssapi3-heimdal:amd64.
    Preparing to unpack .../41-libgssapi3-heimdal_7.7.0+dfsg-1ubuntu1_amd64.deb ...
    Unpacking libgssapi3-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Selecting previously unselected package libsasl2-modules-db:amd64.
    Preparing to unpack .../42-libsasl2-modules-db_2.1.27+dfsg-2_amd64.deb ...
    Unpacking libsasl2-modules-db:amd64 (2.1.27+dfsg-2) ...
    Selecting previously unselected package libsasl2-2:amd64.
    Preparing to unpack .../43-libsasl2-2_2.1.27+dfsg-2_amd64.deb ...
    Unpacking libsasl2-2:amd64 (2.1.27+dfsg-2) ...
    Selecting previously unselected package libldap-common.
    Preparing to unpack .../44-libldap-common_2.4.49+dfsg-2ubuntu1.5_all.deb ...
    Unpacking libldap-common (2.4.49+dfsg-2ubuntu1.5) ...
    Selecting previously unselected package libldap-2.4-2:amd64.
    Preparing to unpack .../45-libldap-2.4-2_2.4.49+dfsg-2ubuntu1.5_amd64.deb ...
    Unpacking libldap-2.4-2:amd64 (2.4.49+dfsg-2ubuntu1.5) ...
    Selecting previously unselected package libnghttp2-14:amd64.
    Preparing to unpack .../46-libnghttp2-14_1.40.0-1build1_amd64.deb ...
    Unpacking libnghttp2-14:amd64 (1.40.0-1build1) ...
    Selecting previously unselected package librtmp1:amd64.
    Preparing to unpack .../47-librtmp1_2.4+20151223.gitfa8646d.1-2build1_amd64.deb ...
    Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build1) ...
    Selecting previously unselected package libssh-4:amd64.
    Preparing to unpack .../48-libssh-4_0.9.3-2ubuntu2.1_amd64.deb ...
    Unpacking libssh-4:amd64 (0.9.3-2ubuntu2.1) ...
    Selecting previously unselected package libcurl4:amd64.
    Preparing to unpack .../49-libcurl4_7.68.0-1ubuntu2.4_amd64.deb ...
    Unpacking libcurl4:amd64 (7.68.0-1ubuntu2.4) ...
    Selecting previously unselected package curl.
    Preparing to unpack .../50-curl_7.68.0-1ubuntu2.4_amd64.deb ...
    Unpacking curl (7.68.0-1ubuntu2.4) ...
    Selecting previously unselected package fonts-dejavu-core.
    Preparing to unpack .../51-fonts-dejavu-core_2.37-1_all.deb ...
    Unpacking fonts-dejavu-core (2.37-1) ...
    Selecting previously unselected package fontconfig-config.
    Preparing to unpack .../52-fontconfig-config_2.13.1-2ubuntu3_all.deb ...
    Unpacking fontconfig-config (2.13.1-2ubuntu3) ...
    Selecting previously unselected package libfreetype6:amd64.
    Preparing to unpack .../53-libfreetype6_2.10.1-2ubuntu0.1_amd64.deb ...
    Unpacking libfreetype6:amd64 (2.10.1-2ubuntu0.1) ...
    Selecting previously unselected package libfontconfig1:amd64.
    Preparing to unpack .../54-libfontconfig1_2.13.1-2ubuntu3_amd64.deb ...
    Unpacking libfontconfig1:amd64 (2.13.1-2ubuntu3) ...
    Selecting previously unselected package libjpeg-turbo8:amd64.
    Preparing to unpack .../55-libjpeg-turbo8_2.0.3-0ubuntu1.20.04.1_amd64.deb ...
    Unpacking libjpeg-turbo8:amd64 (2.0.3-0ubuntu1.20.04.1) ...
    Selecting previously unselected package libjpeg8:amd64.
    Preparing to unpack .../56-libjpeg8_8c-2ubuntu8_amd64.deb ...
    Unpacking libjpeg8:amd64 (8c-2ubuntu8) ...
    Selecting previously unselected package libjbig0:amd64.
    Preparing to unpack .../57-libjbig0_2.1-3.1build1_amd64.deb ...
    Unpacking libjbig0:amd64 (2.1-3.1build1) ...
    Selecting previously unselected package libwebp6:amd64.
    Preparing to unpack .../58-libwebp6_0.6.1-2_amd64.deb ...
    Unpacking libwebp6:amd64 (0.6.1-2) ...
    Selecting previously unselected package libtiff5:amd64.
    Preparing to unpack .../59-libtiff5_4.1.0+git191117-2build1_amd64.deb ...
    Unpacking libtiff5:amd64 (4.1.0+git191117-2build1) ...
    Selecting previously unselected package libxpm4:amd64.
    Preparing to unpack .../60-libxpm4_1%3a3.5.12-1_amd64.deb ...
    Unpacking libxpm4:amd64 (1:3.5.12-1) ...
    Selecting previously unselected package libgd3:amd64.
    Preparing to unpack .../61-libgd3_2.2.5-5.2ubuntu2_amd64.deb ...
    Unpacking libgd3:amd64 (2.2.5-5.2ubuntu2) ...
    Selecting previously unselected package nginx-common.
    Preparing to unpack .../62-nginx-common_1.18.0-0ubuntu1_all.deb ...
    Unpacking nginx-common (1.18.0-0ubuntu1) ...
    Selecting previously unselected package libnginx-mod-http-image-filter.
    Preparing to unpack .../63-libnginx-mod-http-image-filter_1.18.0-0ubuntu1_amd64.deb ...
    Unpacking libnginx-mod-http-image-filter (1.18.0-0ubuntu1) ...
    Selecting previously unselected package libxslt1.1:amd64.
    Preparing to unpack .../64-libxslt1.1_1.1.34-4_amd64.deb ...
    Unpacking libxslt1.1:amd64 (1.1.34-4) ...
    Selecting previously unselected package libnginx-mod-http-xslt-filter.
    Preparing to unpack .../65-libnginx-mod-http-xslt-filter_1.18.0-0ubuntu1_amd64.deb ...
    Unpacking libnginx-mod-http-xslt-filter (1.18.0-0ubuntu1) ...
    Selecting previously unselected package libnginx-mod-mail.
    Preparing to unpack .../66-libnginx-mod-mail_1.18.0-0ubuntu1_amd64.deb ...
    Unpacking libnginx-mod-mail (1.18.0-0ubuntu1) ...
    Selecting previously unselected package libnginx-mod-stream.
    Preparing to unpack .../67-libnginx-mod-stream_1.18.0-0ubuntu1_amd64.deb ...
    Unpacking libnginx-mod-stream (1.18.0-0ubuntu1) ...
    Selecting previously unselected package libsasl2-modules:amd64.
    Preparing to unpack .../68-libsasl2-modules_2.1.27+dfsg-2_amd64.deb ...
    Unpacking libsasl2-modules:amd64 (2.1.27+dfsg-2) ...
    Selecting previously unselected package nginx-core.
    Preparing to unpack .../69-nginx-core_1.18.0-0ubuntu1_amd64.deb ...
    Unpacking nginx-core (1.18.0-0ubuntu1) ...
    Selecting previously unselected package nginx.
    Preparing to unpack .../70-nginx_1.18.0-0ubuntu1_all.deb ...
    Unpacking nginx (1.18.0-0ubuntu1) ...
    Setting up libexpat1:amd64 (2.2.9-1build1) ...
    Setting up libxau6:amd64 (1:1.0.9-0ubuntu1) ...
    Setting up libkeyutils1:amd64 (1.6-6ubuntu1) ...
    Setting up libpsl5:amd64 (0.21.0-1ubuntu1) ...
    Setting up libssl1.1:amd64 (1.1.1f-1ubuntu2.1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up libbrotli1:amd64 (1.0.7-6ubuntu0.1) ...
    Setting up libsqlite3-0:amd64 (3.31.1-4ubuntu0.2) ...
    Setting up libsasl2-modules:amd64 (2.1.27+dfsg-2) ...
    Setting up libnghttp2-14:amd64 (1.40.0-1build1) ...
    Setting up nginx-common (1.18.0-0ubuntu1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up krb5-locales (1.17-6ubuntu4.1) ...
    Setting up libatm1:amd64 (1:2.5.1-4) ...
    Setting up libldap-common (2.4.49+dfsg-2ubuntu1.5) ...
    Setting up libjbig0:amd64 (2.1-3.1build1) ...
    Setting up libcap2:amd64 (1:2.32-1) ...
    Setting up libkrb5support0:amd64 (1.17-6ubuntu4.1) ...
    Setting up libsasl2-modules-db:amd64 (2.1.27+dfsg-2) ...
    Setting up tzdata (2020d-0ubuntu0.20.04) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Configuring tzdata
    ------------------

    Please select the geographic area in which you live. Subsequent configuration
    questions will narrow this down by presenting a list of cities, representing
    the time zones in which they are located.

    1. Africa      4. Australia  7. Atlantic  10. Pacific  13. Etc
    2. America     5. Arctic     8. Europe    11. SystemV
    3. Antarctica  6. Asia       9. Indian    12. US
    Geographic area:
    Use of uninitialized value $_[1] in join or string at /usr/share/perl5/Debconf/DbDriver/Stack.pm line 111.

    Current default time zone: '/UTC'
    Local time is now:      Mon Dec 28 13:42:39 UTC 2020.
    Universal Time is now:  Mon Dec 28 13:42:39 UTC 2020.
    Run 'dpkg-reconfigure tzdata' if you wish to change it.

    Use of uninitialized value $val in substitution (s///) at /usr/share/perl5/Debconf/Format/822.pm line 83, <GEN6> line 4.
    Use of uninitialized value $val in concatenation (.) or string at /usr/share/perl5/Debconf/Format/822.pm line 84, <GEN6> line 4.
    Setting up libcap2-bin (1:2.32-1) ...
    Setting up libx11-data (2:1.6.9-2ubuntu1.1) ...
    Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build1) ...
    Setting up libpng16-16:amd64 (1.6.37-2) ...
    Setting up libmnl0:amd64 (1.0.4-2) ...
    Setting up libwebp6:amd64 (0.6.1-2) ...
    Setting up fonts-dejavu-core (2.37-1) ...
    Setting up ucf (3.0038+nmu1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up libk5crypto3:amd64 (1.17-6ubuntu4.1) ...
    Setting up libjpeg-turbo8:amd64 (2.0.3-0ubuntu1.20.04.1) ...
    Setting up libxtables12:amd64 (1.8.4-3ubuntu2) ...
    Setting up libsasl2-2:amd64 (2.1.27+dfsg-2) ...
    Setting up libroken18-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libkrb5-3:amd64 (1.17-6ubuntu4.1) ...
    Setting up openssl (1.1.1f-1ubuntu2.1) ...
    Setting up libbsd0:amd64 (0.10.0-1) ...
    Setting up libelf1:amd64 (0.176-1.1build1) ...
    Setting up libpam-cap:amd64 (1:2.32-1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up publicsuffix (20200303.0012-1) ...
    Setting up libheimbase1-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libjpeg8:amd64 (8c-2ubuntu8) ...
    Setting up libnginx-mod-mail (1.18.0-0ubuntu1) ...
    Setting up libxdmcp6:amd64 (1:1.1.3-0ubuntu1) ...
    Setting up libxcb1:amd64 (1.14-2) ...
    Setting up fontconfig-config (2.13.1-2ubuntu3) ...
    Setting up iproute2 (5.5.0-1ubuntu1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up libicu66:amd64 (66.1-2ubuntu2) ...
    Setting up libasn1-8-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libnginx-mod-stream (1.18.0-0ubuntu1) ...
    Setting up libhcrypto4-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up ca-certificates (20201027ubuntu0.20.04.1) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Updating certificates in /etc/ssl/certs...
    138 added, 0 removed; done.
    Setting up libwind0-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libfreetype6:amd64 (2.10.1-2ubuntu0.1) ...
    Setting up libgssapi-krb5-2:amd64 (1.17-6ubuntu4.1) ...
    Setting up libssh-4:amd64 (0.9.3-2ubuntu2.1) ...
    Setting up libx11-6:amd64 (2:1.6.9-2ubuntu1.1) ...
    Setting up libtiff5:amd64 (4.1.0+git191117-2build1) ...
    Setting up libfontconfig1:amd64 (2.13.1-2ubuntu3) ...
    Setting up libxml2:amd64 (2.9.10+dfsg-5) ...
    Setting up libxpm4:amd64 (1:3.5.12-1) ...
    Setting up libhx509-5-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libgd3:amd64 (2.2.5-5.2ubuntu2) ...
    Setting up libxslt1.1:amd64 (1.1.34-4) ...
    Setting up libkrb5-26-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libnginx-mod-http-image-filter (1.18.0-0ubuntu1) ...
    Setting up libheimntlm0-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up libnginx-mod-http-xslt-filter (1.18.0-0ubuntu1) ...
    Setting up libgssapi3-heimdal:amd64 (7.7.0+dfsg-1ubuntu1) ...
    Setting up nginx-core (1.18.0-0ubuntu1) ...
    invoke-rc.d: could not determine current runlevel
    invoke-rc.d: policy-rc.d denied execution of start.
    Setting up nginx (1.18.0-0ubuntu1) ...
    Setting up libldap-2.4-2:amd64 (2.4.49+dfsg-2ubuntu1.5) ...
    Setting up libcurl4:amd64 (7.68.0-1ubuntu2.4) ...
    Setting up curl (7.68.0-1ubuntu2.4) ...
    Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
    Processing triggers for ca-certificates (20201027ubuntu0.20.04.1) ...
    Updating certificates in /etc/ssl/certs...
    0 added, 0 removed; done.
    Running hooks in /etc/ca-certificates/update.d...
    done.
    Removing intermediate container 7f5566ddec31
    ---> 5859eba814f2
    Successfully built 5859eba814f2
    ```
</details>


- Check image
```
>>> docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
<none>               <none>    5859eba814f2   24 seconds ago   169MB
<none>               <none>    8e72883fc3ba   12 hours ago     72.9MB
new-ubuntu           latest    aaf7263913df   7 days ago       72.9MB
jsmack/docker-lean   latest    dfd323755a9f   2 weeks ago      72.9MB
ubuntu               updated   dfd323755a9f   2 weeks ago      72.9MB
ubuntu               latest    f643c72bc252   4 weeks ago      72.9MB
hello-world          latest    bf756fb1ae65   12 months ago    13.3kB
```


- Add cvs package
  - But it takes time to update again.
  - 

```Dockerfile
FROM ubuntu:latest

# For example install the curl and nginx packages
RUN apt-get update && apt-get install -y \
    curl \
    nginx \
    cvs
```

- Use cache
  - First, check that you can install with this

```Dockerfile
FROM ubuntu:latest

# For example install the curl and nginx packages
RUN apt-get update
RUN apt-get install -y \
    curl \
    nginx \
RUN apt-get install -y\
    cvs
```

- Using cache 
```
>>> docker build .
Sending build context to Docker daemon  40.96kB
Step 1/3 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/3 : RUN apt-get update &&     apt-get install -y         curl         nginx
 ---> Using cache                            <- !!!!!!!!!!!
 ---> 3e7d7b6c40b2
Step 3/3 : RUN apt-get install cvs
 ---> Running in ba7fea05c9df
Reading package lists...

snip

```

- Finally
  - Make one layer and reduce the capacity

```Dockerfile
FROM ubuntu:latest

# For example install the curl and nginx packages
RUN apt-get update && \
    apt-get install -y \
        curl \
        cvs  \
        nginx \
```