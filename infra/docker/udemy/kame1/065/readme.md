# Modify Dockerfile

```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

WORKDIR /opt

RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh && \
    sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -f /opt/Anaconda3-2020.11-Linux-x86_64.sh

ENV PATH /opt/anaconda3/bin:$PATH

RUN pip install --upgrade pip
WORKDIR /

CMD [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''" ]
```

```bash
>>> docker build .
Sending build context to Docker daemon  2.048kB
Step 1/8 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/8 : RUN apt-get update && apt-get install -y     sudo     wget     vim
 ---> Using cache
 ---> 1370e43890e8
Step 3/8 : WORKDIR /opt
 ---> Using cache
 ---> 1ff565a55995
Step 4/8 : RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh &&     sh Anaconda3-2020.11-Linux-x86_64.sh -b -p /opt/anaconda3 &&     rm -f /opt/Anaconda3-2020.11-Linux-x86_64.sh
 ---> Using cache
 ---> 9e0a775f5a35
Step 5/8 : ENV PATH /opt/anaconda3/bin:$PATH
 ---> Using cache
 ---> afa8aa729511
Step 6/8 : RUN pip install --upgrade pip
 ---> Running in 6e28e2e3fb7a
Collecting pip
  Downloading pip-20.3.3-py2.py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.4
    Uninstalling pip-20.2.4:
      Successfully uninstalled pip-20.2.4
Successfully installed pip-20.3.3
Removing intermediate container 6e28e2e3fb7a
 ---> 7a350a2ac053
Step 7/8 : WORKDIR /
 ---> Running in 97fad36ae519
Removing intermediate container 97fad36ae519
 ---> b4c63436d772
Step 8/8 : CMD [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''" ]
 ---> Running in d8744985bd73
Removing intermediate container d8744985bd73
 ---> cc0eedb8f63e
Successfully built cc0eedb8f63e
 >>>
```

- run
```bash
 >>> docker run -it -p 8888:8888 cc0eedb8f63e
/opt/anaconda3/lib/python3.8/site-packages/traitlets/traitlets.py:2196: FutureWarning: Supporting extra quotes around Unicode is deprecated in traitlets 5.0. Use '' instead of "''" – or use CUnicode.
  warn(
[I 14:10:10.302 LabApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 14:10:10.870 LabApp] All authentication is disabled.  Anyone who can connect to this server will be able to run code.
[I 14:10:10.884 LabApp] JupyterLab extension loaded from /opt/anaconda3/lib/python3.8/site-packages/jupyterlab
[I 14:10:10.885 LabApp] JupyterLab application directory is /opt/anaconda3/share/jupyter/lab
[I 14:10:10.899 LabApp] Serving notebooks from local directory: /
[I 14:10:10.901 LabApp] Jupyter Notebook 6.1.4 is running at:
[I 14:10:10.902 LabApp] http://385b7534d7cb:8888/
[I 14:10:10.904 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 14:10:10.921 LabApp] No web browser found: could not locate runnable browser.
```

- Access http://localhost:8888
