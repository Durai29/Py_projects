class demo:
    def __init__(self,a):
        self.a =a

    def __str__(self):
        return f'U r an {self.a}'

akash = demo('idiot')

print(akash)