from ctypes import alignment
import dearpygui.dearpygui as dpg
import webbrowser as web
from os.path import exists as file_exists
import subprocess
import os.path

version = 1.0 # release version
icon = 'icon.ico' #path to window icon

workdir = os.path.dirname(os.path.abspath(__file__))
activator = os.path.join(workdir, 'activate.bat') # get path to activator script

# create dearpygui viewport
dpg.create_context()
dpg.create_viewport(title='Windows10Activator - version '+str(version), width=850, height=600, min_width=850, min_height=600)

#set window icons
dpg.set_viewport_small_icon(icon)
dpg.set_viewport_large_icon(icon)

# content of item / selection lists
dropdown_releases = ["Home","Home N","Home Single Language","Home Country Specific","Professional","Professional N","Education","Education N","Enterprise","Enterprise N"]
dropdown_machines = ["msguides","xspace"]

# default selection of lists
selected_release = "Home"
selected_machine = "msguides"

# code for github button
def github_button():
    web.open('https://github.com/ZervoTheProtogen/Windows10Activator')

# code for ko-fi button
def kofi_button():
    web.open('https://ko-fi.com/zervo')

# code for releases list
def dropdown_releases_callback(Sender, Data):
    selected_release = Data.replace(" ", "")
    print('Selected release: '+selected_release)

# code for kms machines list
def dropdown_machines_callback(Sender, Data):
    selected_machine = Data
    print('Selected KMS: '+Data)

# code for activate button
def activate_button():
    print("Activating with")
    print("release: "+selected_release)
    print("kms: "+selected_machine)

    # delete some UI items
    dpg.delete_item("welcometext")
    dpg.delete_item("release_list")
    dpg.delete_item("machine_list")
    dpg.delete_item("release_text")
    dpg.delete_item("machine_text")
    dpg.delete_item("activate_button")

    subprocess.call(['runas', '/user:[[dommainName]\\]userName', activator, selected_release, selected_machine])

    exit()

# below is the window and it's content
with dpg.window(tag="primary_window"):
    dpg.add_text("Welcome to Windows10Activator!", pos=(300,20), tag='welcometext') # welcome text in middle top
    dpg.add_text("v"+str(version), pos=(798,534)) # version text in bottom right
    dpg.add_button(label='GitHub', pos=(10,534), callback=github_button) # link button to the github repo
    dpg.add_button(label='Donate', pos=(70,534), callback=kofi_button) # link button my ko-fi page, change this to whatever you want or delete it
    dpg.add_listbox(items=dropdown_releases, callback=dropdown_releases_callback, num_items=4, width=200, pos=(170,200), tag='release_list') # selection list of releases
    dpg.add_listbox(items=dropdown_machines, callback=dropdown_machines_callback, num_items=4, width=200, pos=(470,200), tag='machine_list') # selection list of kms machines
    dpg.add_text("Select Release", pos=(220,170), tag='release_text') # text above release selection
    dpg.add_text("Select KMS", pos=(530,170), tag='machine_text') # text above kms machine selection
    dpg.add_button(label='Activate Windows', pos=(320,360), callback=activate_button, width=200, height=50, tag='activate_button') # activate button, launches activator script

# set up and start dearpygui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary_window", True)
dpg.start_dearpygui()
dpg.destroy_context()