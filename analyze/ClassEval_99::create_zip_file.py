import zipfile

class ZipFileProcessor: 
    def __init__(self, file_name):
        """
        Initialize file name
        :param file_name:string
        """
        self.file_name = file_name

    def read_zip_file(self):
        """
        Get open file object
        :return:If successful, returns the open file object; otherwise, returns None
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
        try:
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except:
            return None
    
    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extractall(output_path)
            return True
        except:
            return False
    
    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extract(file_name, output_path)
            return True
        except:
            return False
    
    def create_zip_file(self, files, output_file_name):
        """
        Comprimi l'elenco di file specificato in un file zip e lo salva nel percorso specificato
        :param files: lista di stringhe, Elenco dei file da comprimere
        :param output_file_name: stringa, Percorso di output specificato
        :return: True o False, che rappresenta se l'operazione di compressione è stata riuscita
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc.txt", "ddd.txt"], "output/bcd")
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    zip_file.write(file)
            return True
        except:
            return False