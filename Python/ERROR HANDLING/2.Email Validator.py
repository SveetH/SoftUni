class Error(Exception):
    """Base class for other exceptions"""
    pass


class NameTooShortError(Error):
    """Raised when name is too short"""
    def __init__(self):
        self.massage = "Name must be more than 4 characters"

    def __str__(self):
        return self.massage


class MustContainAtSymbolError(Error):
    """Raised when there is no '@' in the email"""
    pass


class InvalidDomainError(Error):
    """Raised when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)"""


Email = input()
while Email != "End":
    if '@' not in Email:
        raise MustContainAtSymbolError("Email must contain @")
    index_dot = Email.index('@')
    if len(Email[:index_dot]) < 4:
        raise NameTooShortError
    valid_domains = (
        '.com',
        '.bg',
        '.net',
        '.org',
    )
    validation = False
    for el in valid_domains:
        if el in Email:
            validation = True
            break
    if not validation:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')

    Email = input()
