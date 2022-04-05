import os, winshell, time
from win32com.client import Dispatch

if __name__ == '__main__':

	desktop = winshell.desktop()
	path1 = os.path.join(desktop, "LAN Login (Anaconda).lnk")
	path2 = os.path.join(desktop, "LAN Login (Python).lnk")

	if not os.path.exists(path1) and not os.path.exists(path2):
		print('Creating shortcuts...')

		wDir = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)
		target1 = os.path.join(wDir, 'lan_login_anaconda.bat')
		target2 = os.path.join(wDir, 'lan_login_python.bat')

		shell = Dispatch('WScript.Shell')

		shortcut = shell.CreateShortCut(path1)
		shortcut.Targetpath = target1
		shortcut.WorkingDirectory = wDir
		shortcut.save()

		shortcut = shell.CreateShortCut(path2)
		shortcut.Targetpath = target2
		shortcut.WorkingDirectory = wDir
		shortcut.save()

		print('Done')

		time.sleep(1)