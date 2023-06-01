from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class UserIsBotError(Exception):
    pass

MIN_LENGTH = 4

VALID_DOMAINS = ['.com', '.bg', '.net', '.org']

pattern_name = r'\w+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != 'END':

    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError('Email should contain only 1 @ symbol!')
    if len(email.split('@')[0]) < MIN_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    # custom errors added
    if findall(pattern_name, email)[0] != email.split('@')[0]:
        raise InvalidNameError('Name can contain only letters,digits and underscores!')
    if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    if 'bot' in email:
        raise UserIsBotError('You are a bot!Bot accounts are permitted!')

    print('Email is valid')

    email = input()
