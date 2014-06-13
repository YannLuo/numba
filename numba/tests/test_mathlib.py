from __future__ import print_function, absolute_import, division
import math
import numpy as np
from numba import unittest_support as unittest
from numba.compiler import compile_isolated, Flags, utils
from numba import types

PY27_AND_ABOVE = utils.PYVERSION > (2, 6)



enable_pyobj_flags = Flags()
enable_pyobj_flags.set("enable_pyobject")

no_pyobj_flags = Flags()


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def sinh(x):
    return math.sinh(x)


def cosh(x):
    return math.cosh(x)


def tanh(x):
    return math.tanh(x)


def asin(x):
    return math.asin(x)


def acos(x):
    return math.acos(x)


def atan(x):
    return math.atan(x)


def atan2(y, x):
    return math.atan2(y, x)


def asinh(x):
    return math.asinh(x)


def acosh(x):
    return math.acosh(x)


def atanh(x):
    return math.atanh(x)


def sqrt(x):
    return math.sqrt(x)


def npy_sqrt(x):
    return np.sqrt(x)


def exp(x):
    return math.exp(x)


def expm1(x):
    return math.expm1(x)


def log(x):
    return math.log(x)


def log1p(x):
    return math.log1p(x)


def log10(x):
    return math.log10(x)


def floor(x):
    return math.floor(x)


def ceil(x):
    return math.ceil(x)


def trunc(x):
    return math.trunc(x)


def isnan(x):
    return math.isnan(x)


def isinf(x):
    return math.isinf(x)


def hypot(x, y):
    return math.hypot(x, y)


def degrees(x):
    return math.degrees(x)


def radians(x):
    return math.radians(x)


def erf(x):
    return math.erf(x)


def erfc(x):
    return math.erfc(x)


def gamma(x):
    return math.gamma(x)


def lgamma(x):
    return math.lgamma(x)


class TestMathLib(unittest.TestCase):

    def run_unary(self, pyfunc, x_types, x_values, flags=enable_pyobj_flags,
                  places=6):
        for tx, vx in zip(x_types, x_values):
            cr = compile_isolated(pyfunc, [tx], flags=flags)
            cfunc = cr.entry_point
            self.assertAlmostEqual(cfunc(vx), pyfunc(vx), places=places)

    def test_sin(self, flags=enable_pyobj_flags):
        pyfunc = sin
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_sin_npm(self):
        self.test_sin(flags=no_pyobj_flags)

    def test_cos(self, flags=enable_pyobj_flags):
        pyfunc = cos
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_cos_npm(self):
        self.test_cos(flags=no_pyobj_flags)

    def test_tan(self, flags=enable_pyobj_flags):
        pyfunc = tan
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_tan_npm(self):
        self.test_tan(flags=no_pyobj_flags)

    def test_sqrt(self, flags=enable_pyobj_flags):
        pyfunc = sqrt
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [2, 1, 2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_sqrt_npm(self):
        self.test_sqrt(flags=no_pyobj_flags)

    def test_npy_sqrt(self, flags=enable_pyobj_flags):
        pyfunc = npy_sqrt
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [2, 1, 2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_npy_sqrt_npm(self):
        self.test_npy_sqrt(flags=no_pyobj_flags)

    def test_exp(self, flags=enable_pyobj_flags):
        pyfunc = exp
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_exp_npm(self):
        self.test_exp(flags=no_pyobj_flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_expm1(self, flags=enable_pyobj_flags):
        pyfunc = expm1
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_expm1_npm(self):
        self.test_expm1(flags=no_pyobj_flags)

    def test_log(self, flags=enable_pyobj_flags):
        pyfunc = log
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 10, 100, 1000, 100000, 1000000, 0.1, 1.1]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_log_npm(self):
        self.test_log(flags=no_pyobj_flags)

    def test_log1p(self, flags=enable_pyobj_flags):
        pyfunc = log1p
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 10, 100, 1000, 100000, 1000000, 0.1, 1.1]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_log1p_npm(self):
        self.test_log1p(flags=no_pyobj_flags)

    def test_log10(self, flags=enable_pyobj_flags):
        pyfunc = log10
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 10, 100, 1000, 100000, 1000000, 0.1, 1.1]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_log10_npm(self):
        self.test_log10(flags=no_pyobj_flags)

    def test_asin(self, flags=enable_pyobj_flags):
        pyfunc = asin
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_asin_npm(self):
        self.test_asin(flags=no_pyobj_flags)

    def test_acos(self, flags=enable_pyobj_flags):
        pyfunc = acos
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_acos_npm(self):
        self.test_acos(flags=no_pyobj_flags)

    def test_atan(self, flags=enable_pyobj_flags):
        pyfunc = atan
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_atan_npm(self):
        self.test_atan(flags=no_pyobj_flags)

    def test_atan2(self, flags=enable_pyobj_flags):
        pyfunc = atan2
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [-2, -1, -2, 2, 1, 2, .1, .2]

        for ty, xy in zip(x_types, x_values):
            cres = compile_isolated(pyfunc, (ty, ty), flags=flags)
            cfunc = cres.entry_point
            x = xy
            y = x * 2
            self.assertAlmostEqual(pyfunc(x, y), cfunc(x, y))

    def test_atan2_npm(self):
        self.test_atan2(flags=no_pyobj_flags)

    def test_asinh(self, flags=enable_pyobj_flags):
        pyfunc = asinh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_asinh_npm(self):
        self.test_asinh(flags=no_pyobj_flags)

    def test_acosh(self, flags=enable_pyobj_flags):
        pyfunc = acosh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_acosh_npm(self):
        self.test_acosh(flags=no_pyobj_flags)

    def test_atanh(self, flags=enable_pyobj_flags):
        pyfunc = atanh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, 0.1, 0.1]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_atanh_npm(self):
        self.test_atanh(flags=no_pyobj_flags)

    def test_sinh(self, flags=enable_pyobj_flags):
        pyfunc = sinh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_sinh_npm(self):
        self.test_sinh(flags=no_pyobj_flags)

    def test_cosh(self, flags=enable_pyobj_flags):
        pyfunc = cosh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_cosh_npm(self):
        self.test_cosh(flags=no_pyobj_flags)

    def test_tanh(self, flags=enable_pyobj_flags):
        pyfunc = tanh
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, 0.1, 0.1]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_tanh_npm(self):
        self.test_tanh(flags=no_pyobj_flags)

    def test_floor(self, flags=enable_pyobj_flags):
        pyfunc = floor
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, 0.1, 1.9]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_floor_npm(self):
        self.test_floor(flags=no_pyobj_flags)

    def test_ceil(self, flags=enable_pyobj_flags):
        pyfunc = ceil
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, 0.1, 1.9]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_ceil_npm(self):
        self.test_ceil(flags=no_pyobj_flags)

    def test_trunc(self, flags=enable_pyobj_flags):
        pyfunc = trunc
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, 0.1, 1.9]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_trunc_npm(self):
        self.test_trunc(flags=no_pyobj_flags)

    def test_isnan(self, flags=enable_pyobj_flags):
        pyfunc = isnan
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float32, types.float64, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, float('nan'), 0.0, float('nan'), 0.0]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_isnan_npm(self):
        self.test_isnan(flags=no_pyobj_flags)

    def test_isinf(self, flags=enable_pyobj_flags):
        pyfunc = isinf
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float32, types.float64, types.float64]
        x_values = [0, 0, 0, 0, 0, 0, float('inf'), 0.0, float('inf'), 0.0]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_isinf_npm(self):
        self.test_isinf(flags=no_pyobj_flags)

    def test_hypot(self, flags=enable_pyobj_flags):
        pyfunc = hypot
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 2, 3, 4, 5, 6, .21, .34]

        for ty, xy in zip(x_types, x_values):
            x = xy
            y = xy * 2
            cres = compile_isolated(pyfunc, (ty, ty), flags=flags)
            cfunc = cres.entry_point
            self.assertAlmostEqual(pyfunc(x, y), cfunc(x, y))

    def test_hypot_npm(self):
        self.test_hypot(flags=no_pyobj_flags)

    def test_degrees(self, flags=enable_pyobj_flags):
        pyfunc = degrees
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags, places=5)

    def test_degrees_npm(self):
        self.test_degrees(flags=no_pyobj_flags)

    def test_radians(self, flags=enable_pyobj_flags):
        pyfunc = radians
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    def test_radians_npm(self):
        self.test_radians(flags=no_pyobj_flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_erf(self, flags=enable_pyobj_flags):
        pyfunc = erf
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    @unittest.expectedFailure
    def test_erf_npm(self):
        self.test_erf(flags=no_pyobj_flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_erfc(self, flags=enable_pyobj_flags):
        pyfunc = erfc
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    @unittest.expectedFailure
    def test_erfc_npm(self):
        self.test_erfc(flags=no_pyobj_flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_gamma(self, flags=enable_pyobj_flags):
        pyfunc = gamma
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    @unittest.expectedFailure
    def test_gamma_npm(self):
        self.test_gamma(flags=no_pyobj_flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    def test_lgamma(self, flags=enable_pyobj_flags):
        pyfunc = lgamma
        x_types = [types.int16, types.int32, types.int64,
                   types.uint16, types.uint32, types.uint64,
                   types.float32, types.float64]
        x_values = [1, 1, 1, 1, 1, 1, 1., 1.]
        self.run_unary(pyfunc, x_types, x_values, flags)

    @unittest.skipIf(not PY27_AND_ABOVE, "Only support for 2.7+")
    @unittest.expectedFailure
    def test_lgamma_npm(self):
        self.test_lgamma(flags=no_pyobj_flags)


if __name__ == '__main__':
    unittest.main()