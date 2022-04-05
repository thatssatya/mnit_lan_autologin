# mnit_lan_autologin

**How to use this?**
1. Clone this repo to your system
2. Modify the **login_details.yml** files in the config directory with your respective details \
   (Optional: Modify the browser_details.yml in this directory if your browser is different than Google Chrome (x64))
3. Onetime Setup: \
   a) Ensure Python3 is installed in your system \
   b) Run **setup_with_python.bat** (It'll do everything on its own)
4. Just double click the appropriate login shortcut which got created on the desktop right now. \
   (If you move the project folder to some other place on your system, then delete these shortcuts and rerun the aforementioned script to get new shortcuts)

**Note:** If you are using **conda environment**, then follow this in place of of Step 4:
1. Add an environment variable as **ANACONDA_ROOT** containing the path to the installation directory of Anaconda
2. Run **setup_with_anaconda.bat**

**Platforms supported:** Windows (x86, x64)