import zipfile


class ZipFileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_zip_file(self):
        return self._open_zip_file('r')

    def extract_all(self, output_path):
        return self._extract_zip(output_path)

    def extract_file(self, file_name, output_path):
        return self._extract_specific_file(file_name, output_path)

    def create_zip_file(self, files, output_file_name):
        return self._create_zip(files, output_file_name)

    def _open_zip_file(self, mode):
        try:
            return zipfile.ZipFile(self.file_name, mode)
        except Exception:
            return None

    def _extract_zip(self, output_path):
        with self._open_zip_file('r') as zip_file:
            if zip_file is not None:
                zip_file.extractall(output_path)
                return True
        return False

    def _extract_specific_file(self, file_name, output_path):
        with self._open_zip_file('r') as zip_file:
            if zip_file is not None:
                zip_file.extract(file_name, output_path)
                return True
        return False

    def _create_zip(self, files, output_file_name):
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    zip_file.write(file)
            return True
        except Exception:
            return False