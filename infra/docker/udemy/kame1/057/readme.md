# Connect port from host to container
- ` -p 8888:4444`
  - -p is publish

## Exanple
```bash
>>> docker run -itd --rm -p 10000:8888 jupyter/datascience-notebook /bin/bash
606aae570dd680634145569b3b29a286c3b43d4bb03bd515dd8a50db7e119552
>>>
>>> docker exec -it 606aae570dd680634145569b3b29a286c3b43d4bb03bd515dd8a50db7e119552 bash
(base) jovyan@606aae570dd6:~$
(base) jovyan@606aae570dd6:~$
(base) jovyan@606aae570dd6:~$ jupyter notebook
[I 10:08:52.827 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 10:08:53.590 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.8/site-packages/jupyterlab
[I 10:08:53.590 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 10:08:53.598 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 10:08:53.598 NotebookApp] Jupyter Notebook 6.1.6 is running at:
[I 10:08:53.599 NotebookApp] http://606aae570dd6:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
[I 10:08:53.599 NotebookApp]  or http://127.0.0.1:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
[I 10:08:53.599 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 10:08:53.604 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-948-open.html
    Or copy and paste one of these URLs:
        http://606aae570dd6:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
     or http://127.0.0.1:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
[I 10:08:58.938 NotebookApp] 302 GET / (172.17.0.1) 1.290000ms
[I 10:08:58.952 NotebookApp] 302 GET /tree? (172.17.0.1) 1.440000ms
[I 10:09:09.249 NotebookApp] 302 GET /?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0 (172.17.0.1) 0.660000ms
^C[I 10:11:42.886 NotebookApp] interrupted
Serving notebooks from local directory: /home/jovyan
0 active kernels
Jupyter Notebook 6.1.6 is running at:
http://606aae570dd6:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
 or http://127.0.0.1:8888/?token=cb8671f91abaeed8b419c03901e30c33479c23ecef55dcf0
Shutdown this notebook server (y/[n])? y
[C 10:11:43.803 NotebookApp] Shutdown confirmed
[I 10:11:43.804 NotebookApp] Shutting down 0 kernels
[I 10:11:43.804 NotebookApp] Shutting down 0 terminals
(base) jovyan@606aae570dd6:~$ exit
exit
```