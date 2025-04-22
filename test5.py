class Parent:
    def __init__(self):
        self.x=333
    def property(self):
        print('golf+land+cash')
class Child(Parent):
    def education(self):
        print('B-Tech Qualification + job')
c=Child()
c.education()
c.property()
print(c.x)
