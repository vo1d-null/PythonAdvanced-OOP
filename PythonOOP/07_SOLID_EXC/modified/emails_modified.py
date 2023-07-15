from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class SenderTemplate(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class ReceiverTemplate(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class IMSender(SenderTemplate):
    def format(self):
        return ' '.join(["I'm", self.text])


class IMReceiver(ReceiverTemplate):
    def format(self):
        return ' '.join(["I'm", self.text])


class Vo1dSender(SenderTemplate):
    def format(self):
        return ' '.join(["Vo1d", self.text])


class Vo1dReceiver(ReceiverTemplate):
    def format(self):
        return ' '.join(["Vo1d", self.text])


class MyML(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class Vo1dML(IContent):
    def format(self):
        return '\n'.join(['<Vo1dML>', self.text, '</Vo1dML>'])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, ):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# Default Test
myml = MyML('Hello, there!')
email = Email()
# Hate this typo in the name.That's why I changed it :)
email.set_sender('Kemal')
email.set_receiver('james')
email.set_content(myml)
print(email)
#For better readability
print()

# Implemented features Test
# P.S : Don't cringe too much at the names.They fit thematically my GitHub xd

vo1dml = Vo1dML('Welcome to oblivion!')
email = Email()
email.set_sender('Eternal Darkness')
email.set_receiver('Little Light')
email.set_content(vo1dml)
print(email)
