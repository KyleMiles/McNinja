from llvmlite import ir


def global_string_constant(module, string: str, name: str):
  c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(string)),
                      bytearray(string.encode("utf8")))
  global_fmt = ir.GlobalVariable(module, c_fmt.type, name)
  global_fmt.linkage = 'internal'
  global_fmt.global_constant = True
  global_fmt.initializer = c_fmt
  return global_fmt
