import re
def validation(standard,rollno,englishmarks,mathsmarks,socialmarks,sciencemarks):
    val1=re.match("^[1-9]{1}|10$",standard)
    val2=re.match("[0-9]{1,7}",rollno)
    val3=re.search("^[0-9]{1}[0-9]{1}|100$",str(englishmarks))
    val4=re.search("^[0-9]{1}[0-9]{1}|100$",str(mathsmarks))
    val5=re.search("^[0-9]{1}[0-9]{1}|100$",str(socialmarks))
    val6=re.search("^[0-9]{1}[0-9]{1}|100$",str(sciencemarks))
    if val1 and val2 and val3 and val3 and val4 and val6:
        return True
    else:
        return False
