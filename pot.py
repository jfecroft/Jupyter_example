from scipy.interpolate import CubicSpline
from numpy import loadtxt

v_kk_1 = loadtxt('kk_singlet')
v_kk_3 = loadtxt('kk_triplet')

v_krb_1 = loadtxt('krb_singlet')
v_krb_3 = loadtxt('krb_triplet')

pot_singlet = CubicSpline(v_kk_1[:, 0], v_kk_1[:, 1])
pot_triplet = CubicSpline(v_kk_3[:, 0], v_kk_3[:, 1])
