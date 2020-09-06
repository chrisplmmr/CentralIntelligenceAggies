import challenges


class Ransomeware(challenges.Challenge):
    # Variables
    promt = "Bevo has installed ransomware on our system! " \
            "He is aiming to encrypt all our data and hold HowdyHack hostage " \
            "until we pay him 1 million dogecoins. However... if you are able to decrypt his username " \
            "and password we can destroy the malware! Hint: Key = 3."

    points = 0

    usernameEncrypted = "IdwFrzlqDxvwlq"
    passwordEncrypted = "kruqvgrzq"

    usernameDecrypted = "FatCowinAustin"
    passwordDecrypted = "hornsdown"

    def getIntelEncypted(self):
        return "Username: "+self.usernameEncrypted+" Password: "+self.passwordEncrypted

    # Use this to access points earned for this challenge after calling getResult()
    def getPoints(self):
        return self.points

    def computePoints(self, userResult, passResult):
        if self.usernameDecrypted.lower() == userResult.lower():
            self.points += 5
        if self.passwordDecrypted.lower() == passResult.lower():
            self.points += 5

    def getResult(self, userResult, passResult):
        self.computePoints(userResult, passResult)
        if self.usernameDecrypted.lower() == userResult.lower() and self.passwordDecrypted.lower() == passResult.lower():
            return True
        else:
            return False
