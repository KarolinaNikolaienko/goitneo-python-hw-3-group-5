from model.model.errors import PhoneNumError, BirthdayError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("No phone was found")
            return False
        except KeyError:
            print("Record wasn't found")
            return False
        except IndexError: 
            print("Give me Name and Phone number please")
            return False
        except PhoneNumError:
            print("Phone must consist of 10 digits")
            return False
        except BirthdayError:
            print("Birthday must have format DD.MM.YYYY")
            return False
        # except:
        #     print("Something went wrong")
    return inner