import os

from IPython.lib import passwd

c = get_config()

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8080
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root=True
c.NotebookApp.token=''
c.NotebookApp.password=passwd('liquid_crystal')
c.NotebookApp.allow_password_change=False
c.NotebookApp.base_url='/notebook/'
