import os
import pylnk
import csv

path = "C:\\"

def _csv_windows_lnk():
    with open(self.output_dir + '\\' + self.computer_name + '_lnk' + self.rand_ext, 'wb') as output:
        for (path, dir, files) in os.walk(path):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.lnk':
                    write_to_csv(("LNK_FILE_NAME", "TARGET_FiLE_NAME"), csv_writer)
                    filepath =  path+"\\"+filename
                    lnkfile = pylnk.parse(filename)                         
                    write_to_csv((filename, lnkfile.relative_path), csv_writer)
                
           