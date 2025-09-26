class PersonRequest:
    MAX_NAME_LENGTH = 33
    VALID_SEXES = {"Man", "Woman", "UGM"}
    PHONE_NUMBER_LENGTH = 11

    def __init__(self, name: str, sex: str, phone_number: str):
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phone_number = self._validate_phone_number(phone_number)

    def _validate_name(self, name: str) -> str:
        if self._is_name_invalid(name):
            return None
        return name

    def _is_name_invalid(self, name: str) -> bool:
        return not name or len(name) > self.MAX_NAME_LENGTH

    def _validate_sex(self, sex: str) -> str:
        if sex not in self.VALID_SEXES:
            return None
        return sex

    def _validate_phone_number(self, phone_number: str) -> str:
        if self._is_phone_number_invalid(phone_number):
            return None
        return phone_number

    def _is_phone_number_invalid(self, phone_number: str) -> bool:
        return not phone_number or len(phone_number) != self.PHONE_NUMBER_LENGTH or not phone_number.isdigit()