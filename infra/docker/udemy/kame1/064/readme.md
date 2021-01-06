# Verification of how to install anaconda

- RUN
```bash
>>> docker run -it 66709d3e3c70 bash
root@9c0601c7038f:/opt#
```

- Why /opt is the login diretory?
  - Becouse it is moved by WORKDIR of Dockerfile.
```Dockerfile
WORKDIR /opt
```

- Install anaconda
  - Response
    - `Please, press ENTER to continue`
      - ENTER
    - `Anaconda3 will now be installed into this location:`
      - `/opt/anaconda3`
    - `Do you wish the installer to initialize Anaconda3by running conda init? [yes|no]`
      - `yes`
```bash
root@9c0601c7038f:/opt# sh Anaconda3-2020.11-Linux-x86_64.sh
```

- Exec python
  - Error.
  - Because the PATH to the python command is no in the PATH.
```bash
root@9c0601c7038f:/opt# python
bash: python: command not found
root@9c0601c7038f:/opt#
```

- Setting PATH & run python
```bash
root@9c0601c7038f:/opt# export PATH=/opt/anaconda3/bin:$PATH
root@9c0601c7038f:/opt# python
Python 3.8.5 (default, Sep  4 2020, 07:30:14)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
root@9c0601c7038f:/opt#
```

-  Test if you can install in interactive mode
```bash
root@9c0601c7038f:/opt# sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3
ERROR: File or directory already exists: '/opt/anaconda3'
If you want to update an existing installation, use the -u option.
root@9c0601c7038f:/opt# 
root@9c0601c7038f:/opt# rm -rf /opt/anaconda3
root@9c0601c7038f:/opt# 
root@9c0601c7038f:/opt# sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3
PREFIX=/opt/anaconda3
WARNING: md5sum mismatch of tar archive
expected: a8f71d57955d4618ab3c1b02b963f667
     got: bec25f4d969522369298111f0d4384c4  -
Unpacking payload ...
Collecting package metadata (current_repodata.json): done
Solving environment: done
```
