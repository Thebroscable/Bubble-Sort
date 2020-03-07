import cx_Freeze

executables = [cx_Freeze.Executable("run.py", base="Win32GUI")]

cx_Freeze.setup(
    name="bubble sort",
    opions={"build_exe":{"packages":["pygame", "random", "sys", "math"]}},
    executables = executables)
