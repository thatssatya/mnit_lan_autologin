import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path = os.path.join(desktop, "LAN Login.lnk")

if not os.path.exists(path):
	print('Creating shortcut...')

	wDir = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)
	target = os.path.join(wDir, 'lan_login_anaconda.bat')

	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.WorkingDirectory = wDir
	shortcut.save()

	print('Done')