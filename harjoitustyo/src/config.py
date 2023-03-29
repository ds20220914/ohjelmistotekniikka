import os

dirname=os.path.dirname(__file__)

Smonitor_username=os.getenv("Smonitor_username") or "User.csv"
Smonitor_File_path1=os.path.join(dirname,"..", "data", "Smonitor_username.csv")

