import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    def uploadfile(self, filesfrom, filesto):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(filesfrom):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,filesfrom)
                dropbox_path=os.path.join(filesto, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accesstoken = "sl.Bs-8Brra2_mj2gTyVmATNONZs3TkZkhxg-ZRz3kzu015pJgNI9EI4V0iteXM2GB1d0R8NDT_eNbYPnuRrY5qroxuIXacGiP1XL-DHKrBaDA2HtSJoSeDsViAn_Ty2FovUNB096D9Oon3"
    transfer = TransferData(accesstoken)
    filesfrom = input("Enter the file path to transfer \n")
    filesto = input("Enter the full path to upload to Dropbox")
    transfer.uploadfile(filesfrom, filesto)
    console.log("Files have been moved")
