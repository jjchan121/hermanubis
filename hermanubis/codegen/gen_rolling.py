from jinja2 import Template, Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='templates/')
)

single_var_rolling_tmp = env.get_template('single_var_rolling.html')
two_vars_rolling_tmp = env.get_template('double_var_rolling.html')
single_var_rolling_apply_tmp = env.get_template('single_var_rolling_apply.html')
file_tmp = env.get_template('class_file.html')

funcs = [
    ['count', 'Count', 'n', 'Rolling Count'],
    ['kurt', 'Kurt', 'κ', 'Rolling Kurtosis'],
    ['max', 'Max', 'H', 'Rolling Maxium'],
    ['min', 'Min', 'L', 'Rolling Minimum'],
    ['mean', 'Mean', 'μ', 'Rolling Mean'], # 02C9
    ['median', 'Median', 'ˉ', 'Rolling Median'], #02C8
#    ['pd.rolling_quantile', 'Quantile', 'q', 'Rolling Quantile'],
    ['skew', 'Skew', 'Ω', 'Rolling Skew'],
    ['sum', 'Sum', '∑', 'Rolling Sum'], # 2211
    ['std', 'Stddev', 's', 'Rolling Stddev'],
    ['var', 'Var', 'V', 'Rolling Variance'],
]

two_vars_funcs = [
    ['corr', 'Correlation', 'ρ', 'Rolling Correlation'], #03c1
    ['cov', 'Covariance', 'Ξ', 'Rolling Covariance'], #2211
]

rolling_apply_funcs = [
    ['np.prod', 'Prod', '∏', 'Rolling Product'], # 220F
    ['np.cumprod', 'CumProd', 'ʄ', 'Rolling Cumulative Product'], #0284
    ['np.cumsum', 'CumSum', 'ʃ', 'Rolling Cumulative Sum'], #0283
]

with open('hermanubis/rolling.py', 'w') as outfile:
    class_seq = [single_var_rolling_tmp.render(
        {"className": f[1],
         "shortName": f[2],
         "longName": f[1],
         "desc": f[3],
         "func": f[0]}) for f in funcs]

    two_vars_seq = [two_vars_rolling_tmp.render(
        {"className": f[1],
         "shortName": f[2],
         "longName": f[1],
         "desc": f[3],
         "func": f[0]})
        for f in two_vars_funcs]

    single_var_rolling_apply_seq = [single_var_rolling_apply_tmp.render(
        {"className": f[1],
         "shortName": f[2],
         "longName": f[1],
         "desc": f[3],
         "func": f[0]})
        for f in rolling_apply_funcs ]


    content = file_tmp.render({"seq": class_seq + two_vars_seq + single_var_rolling_apply_seq})
    print(content)
    outfile.write(content)
