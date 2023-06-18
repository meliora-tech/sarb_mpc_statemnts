
import glob 
import os 
import pandas as pd 
import PyPDF2

from progress.bar import Bar

def read_mpc_statements(file:str = "") -> pd.DataFrame:
    """
    Read all the MPC statements

    :params file is the path to the pdf/txt mpc statements
    :type :str

    :return: (pd.DataFrame)
    """
    
    if file == "":
        path       = os.path.abspath('')
        pdf_files  = glob.glob(os.path.join(path,"mpc statements","*.pdf"))
        txt_files  = glob.glob(os.path.join(path,"mpc statements","*.txt"))

        # Combine all file paths 
        mpc_files = []
        mpc_files.extend(txt_files)
        mpc_files.extend(pdf_files)
        
        # Placeholder for data 
        all_files = {}
        
        bar = Bar("Reading in mpc statements...", max=len(mpc_files))
        for file in mpc_files:
            ext      = os.path.splitext(os.path.basename(file))[1]
            key_file = os.path.splitext(os.path.basename(file))[0]
            if ext == '.pdf':
            
                obj       = open(file, 'rb')
                pdfReader = PyPDF2.PdfReader(obj)
                page_text = ""
                for page in pdfReader.pages:
                
                    page_text+= page.extract_text()

                all_files[key_file] = page_text   
                obj.close()

            elif ext == '.txt':
                with open(file, 'r', encoding='UTF-8') as f:
                    page_text = f.read()

                    all_files[key_file] = page_text  

            bar.next()
        bar.finish()

        df = pd.DataFrame.from_dict(all_files, orient='index')
        df.reset_index(inplace=True)
        df.rename(columns={"index": "MPC Date", 0:"Content"}, inplace=True)
        
        return df 