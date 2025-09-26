import zipfile


class ZipFileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def _open_zip_file(self, mode):
        try:
            return zipfile.ZipFile(self.file_name, mode)
        except Exception:
            return None

    def read_zip_file(self):
        return self._open_zip_file('r')

    def extract_all(self, output_path):
        zip_file = self._open_zip_file('r')
        if zip_file is None:
            return False
        try:
            zip_file.extractall(output_path)
            return True
        finally:
            zip_file.close()

    def extract_file(self, file_name, output_path):
        zip_file = self._open_zip_file('r')
        if zip_file is None:
            return False
        try:
            zip_file.extract(file_name, output_path)
            return True
        finally:
            zip_file.close()

    def create_zip_file(self, files, output_file_name):
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    zip_file.write(file)
            return True
        except Exception:
            return False