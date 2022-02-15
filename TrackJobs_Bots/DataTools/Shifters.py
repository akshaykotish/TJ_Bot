class Shifters(object):
    


    def Is_Diploma(self, tokens):
        if "diploma" in tokens:
            return True
        elif "polytechnic" in tokens:
            return True

        return False

    def Is_Bachelors(self, tokens):
        if "bachelor" in tokens:
            return True
        elif "bachelors" in tokens:
            return True
        elif "bachelor's" in tokens:
            return True
        elif "b" in tokens:
            return True
        elif "degree" in tokens:
            return True
        elif "graduation" in tokens:
            return True

        return False

    
    def Is_Masters(self, tokens):
        if "master" in tokens:
            return True
        elif "masters" in tokens:
            return True
        elif "master's" in tokens:
            return True
        elif "m" in tokens:
            return True
        elif "post" in tokens:
            return True

        return False

    
    def Is_Doctorate(self, tokens):
        if "doctorate" in tokens:
            return True
        elif "phd" in tokens:
            return True

        return False





