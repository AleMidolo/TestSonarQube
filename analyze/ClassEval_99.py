import zipfile


class ZipFileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_zip_file(self):
        return self._open_zip_file('r')

    def extract_all(self, output_path):
        return self._extract_zip_file(output_path, self.file_name)

    def extract_file(self, file_name, output_path):
        return self._extract_zip_file(output_path, self.file_name, file_name)

    def create_zip_file(self, files, output_file_name):
        return self._create_zip_file(files, output_file_name)

    def _open_zip_file(self, mode):
        try:
            return zipfile.ZipFile(self.file_name, mode)
        except Exception:
            return None

    def _extract_zip_file(self, output_path, zip_file_name, file_name=None):
        try:
            with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
                if file_name:
                    zip_file.extract(file_name, output_path)
                else:
                    zip_file.extractall(output_path)
            return True
        except Exception:
            return False

    def _create_zip_file(self, files, output_file_name):
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    zip_file.write(file)
            return True
        except Exception:
            return False