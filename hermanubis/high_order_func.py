from hermanubis.expressions import Expression
from hermanubis.expressions import SequentialMode

class Fold(Expression):
    def __init__(self, expr, init_expr, *args, **kwargs):
        super(Fold, self).__init__(short_name='F', long_name='Fold', desc='Fold expression with initial expression',
                                   seq_mode=SequentialMode.ON,
                                   *args, **kwargs)
        self.expr = expr
        self.init_expr = init_expr
        self.expr.seq_mode = SequentialMode.ON
        self.init_expr.seq_mode = SequentialMode.ON

    def evaluate(self, table):

        pass

        # for major_key in tab


