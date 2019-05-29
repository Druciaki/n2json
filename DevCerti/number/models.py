from django.db import models

class CertiNumber():

    def __init__(self, value=None):
        if not value:
            self.value = ""
        if type(value) != type(""):
            self.value = str(value)
        else: # Just assuring we will be handling strings further
            self.value = value

    NUMS = {
    '0':'',
    '1':'um',
    '2':'dois',
    '3':'três',
    '4':'quatro',
    '5':'cinco',
    '6':'seis',
    '7':'sete',
    '8':'oito',
    '9':'nove',
    '10':'dez',
    '11':'onze',
    '12':'doze',
    '13':'treze',
    '14':'quatorze',
    '15':'quinze',
    '16':'dezesseis',
    '17':'dezesete',
    '18':'dezoito',
    '19':'dezenove',
    '20':'vinte',
    '30':'trinta',
    '40':'quarenta',
    '50':'cinquenta',
    '60':'sessenta',
    '70':'setenta',
    '80':'oitenta',
    '90':'noventa',
    '100':'cento',
    '200':'duzentos',
    '300':'trezentos',
    '400':'quatrocentos',
    '500':'quinhentos',
    '600':'seissentos',
    '700':'setecentos',
    '800':'oitocentos',
    '900':'novecentos',
    }


    def get_string_pt_split(self, xyz):
        ''' divide and conquer '''
        NUMS = self.NUMS
        ans = ""
        if xyz in NUMS: # Best case, answer on our dictionary
            if xyz == '100':
                return 'cem'
            else:
                return NUMS[xyz]
        if xyz[:-2]: # Checking X ('centene')
            check_cent = NUMS.get(xyz[:-2]+"00", False)
            if check_cent:
                ans += check_cent
                if xyz[-2:] != '00':
                    ans += " e "
        if len(xyz[-2:]) > 1: # Y anx YZ
            check_dez = NUMS.get(xyz[-2:], False)
            if check_dez:
                ans += check_dez
            else:
                check_dez = NUMS.get(xyz[-2:-1]+"0", False)
                ans += check_dez
                if xyz[-1] != "0":
                    ans += " e "
                    ans += NUMS.get(xyz[-1])
        else: # Z
            ans += NUMS.get(xyz[-1])
        return ans


    def get_string_portuguese(self, sign):
        thouNum = None
        firstNum = None
        ans = ""
        if len(self.value) > 5:
            return {'error':'valor muito longo'}
        if len(self.value) > 3:
            thouNum = self.get_string_pt_split(self.value[:-3])
            firstNum = self.get_string_pt_split(self.value[-3:])
        else:
            firstNum = self.get_string_pt_split(self.value[-3:])

        if sign<0:
            ans += "menos "
        if thouNum:
            if thouNum == 'um':
                thouNum = "mil "
            else:
                thouNum += " mil "
            ans += thouNum
        ans += firstNum
        return ans