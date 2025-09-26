class PersonRequest:
    MAX_NAME_LENGTH = 33
    VALID_SEXES = {"Man", "Woman", "UGM"}
    PHONE_NUMBER_LENGTH = 11

    def __init__(self, name: str, sex: str, phone_number: str):
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phone_number = self._validate_phone_number(phone_number)

    def _validate_name(self, name: str) -> str:
        if self._is_name_valid(name):
            return name
        return None

    def _is_name_valid(self, name: str) -> bool:
        return name and len(name) <= self.MAX_NAME_LENGTH

    def _validate_sex(self, sex: str) -> str:
        if sex in self.VALID_SEXES:
            return sex
        return None

    def _validate_phone_number(self, phone_number: str) -> str:
        if self._is_phone_number_valid(phone_number):
            return phone_number
        return None

    def _is_phone_number_valid(self, phone_number: str) -> bool:
        return phone_number and len(phone_number) == self.PHONE_NUMBER_LENGTH and phone_number.isdigit()