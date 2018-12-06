def credit(gender,age,status,status1):
    """


    :rtype:
    """
    if gender:
        if (age <=30):
            if(status == 'single'):
                if(status1 =='work'):
                    print("Credit approved for 300 000 rubs.   ")
                elif(status1 == 'jobless'):
                    print("Credit approved for zero rubs.   ")
            elif(status == 'married'):
                if(status1 =='work'):
                    print("Credit approved for 200 000 rubs.   ")
                elif(status1 == 'jobless'):
                    print("Credit approved for 150 000 rubs.   ")
        else:
            if(30 <= age < 40):
                if(status == 'single'):
                    if(status1 =='work'):
                        print("Credit approved for 200 000 rubs.   ")
                    elif(status1 == 'jobless'):
                        print("Credit approved for zero rubs.   ")
                elif(status == 'married'):
                    if(status1 =='work'):
                        print("Credit approved for 150 000 rubs.   ")
                    elif(status1 == 'jobless'):
                        print("Credit approved for 50 000 rubs.   ")
    else:
        if (age <=30):
            if(status == 'single'):
                if(status1 =='work'):
                    print("Credit approved for 250 000 rubs.   ")
                elif(status1 == 'jobless'):
                    print("Credit approved for 150 000 rubs.   ")
            elif(status == 'married'):
                if(status1 =='work'):
                    print("Credit approved for 200 000 rubs.   ")
                elif(status1 == 'jobless'):
                    print("Credit approved for 150 000 rubs.   ")
        else:
            if(30 <= age < 40):
                if(status == 'single'):
                    if(status1 =='work'):
                        print("Credit approved for 200 000 rubs.   ")
                    elif(status1 == 'jobless'):
                        print("Credit approved for zero rubs.   ")
                elif(status == 'married'):
                    if(status1 =='work'):
                        print("Credit approved for 150 000 rubs.   ")
                    elif(status1 == 'jobless'):
                        print("Credit approved for 50 000 rubs.   ")
