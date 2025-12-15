class PersonRequest: 
    def __init__(self, name: str, sex: str, phoneNumber: str):
        """
        Initialize PersonRequest object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phoneNumber: str, the phone number of the person
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)

    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
        if sex not in ["Man", "Woman", "UGM"]:
            return None
        return sex
    
    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
        if not phoneNumber:
            return None
        if len(phoneNumber) != 11 or not phoneNumber.isdigit():
            return None
        return phoneNumber
    
    def _validate_name(self, name: str) -> str:
        """
        Valida il nome e lo restituisce. Se il nome è vuoto o supera i 33 caratteri di lunghezza, imposta a None.
        :param name: str, il nome da validare
        :return: str, il nome validato o None se non valido
        """
        if not name or len(name) > 33:
            return None
        return name