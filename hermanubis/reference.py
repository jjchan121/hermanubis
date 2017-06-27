from hermanubis.expressions import Expression

class Reference(Expression):
    def __init__(self, value, *args, **kwargs):
        super(Reference, self).__init__(short_name='&', long_name='Reference', desc='A Placeholder Reference')
        self.value = value

    def evaluate(self, table):
        return self.value


