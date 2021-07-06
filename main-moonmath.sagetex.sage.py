## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file /home/mirco/Leastauthority/MMM/moonmath-manual/main-moonmath.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_492 = Integer(492); _sage_const_246 = Integer(246); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_1290 = Integer(1290); _sage_const_182 = Integer(182); _sage_const_502 = Integer(502); _sage_const_1258 = Integer(1258); _sage_const_296 = Integer(296); _sage_const_23 = Integer(23); _sage_const_22 = Integer(22); _sage_const_522 = Integer(522); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_1372 = Integer(1372); _sage_const_394 = Integer(394); _sage_const_249 = Integer(249); _sage_const_46 = Integer(46); _sage_const_392 = Integer(392); _sage_const_1269 = Integer(1269); _sage_const_85 = Integer(85); _sage_const_1227 = Integer(1227); _sage_const_187 = Integer(187); _sage_const_294 = Integer(294); _sage_const_1189 = Integer(1189); _sage_const_82 = Integer(82); _sage_const_157 = Integer(157); _sage_const_517 = Integer(517); _sage_const_155 = Integer(155); _sage_const_319 = Integer(319); _sage_const_505 = Integer(505); _sage_const_317 = Integer(317); _sage_const_331 = Integer(331); _sage_const_213 = Integer(213); _sage_const_463 = Integer(463); _sage_const_1163 = Integer(1163); _sage_const_334 = Integer(334); _sage_const_218 = Integer(218); _sage_const_1286 = Integer(1286); _sage_const_906 = Integer(906); _sage_const_497 = Integer(497); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_59 = Integer(59); _sage_const_14 = Integer(14); _sage_const_57 = Integer(57); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_15 = Integer(15); _sage_const_50 = Integer(50); _sage_const_1193 = Integer(1193); _sage_const_1362 = Integer(1362); _sage_const_93 = Integer(93); _sage_const_164 = Integer(164); _sage_const_1231 = Integer(1231); _sage_const_79 = Integer(79); _sage_const_160 = Integer(160); _sage_const_903 = Integer(903); _sage_const_1151 = Integer(1151); _sage_const_457 = Integer(457)## This file (main-moonmath.sagetex.sage) was *autogenerated* from main-moonmath.tex with sagetex.sty version 2019/01/09 v3.2.
import sagetex
_st_ = sagetex.SageTeXProcessor('main-moonmath', version='2019/01/09 v3.2', version_check=True)
try:
 _st_.current_tex_line = _sage_const_46 
 _st_.commandline(_sage_const_0 , r"""
sage: Groups()
sage: CommutativeAdditiveGroups()
sage: FiniteGroups()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_50 )
try:
 _st_.current_tex_line = _sage_const_57 
 _st_.commandline(_sage_const_1 , r"""
sage: TrivialGroup = SymmetricGroup(1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_59 )
try:
 _st_.current_tex_line = _sage_const_79 
 _st_.commandline(_sage_const_2 , r"""
sage: CommutativeRings()
sage: CommutativeRings().super_categories()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_85 
 _st_.commandline(_sage_const_3 , r"""
sage: ZZ # A sage notation for the Ring of integers
sage: ZZ(5) # Get an element from the Ring of integers
sage: ZZ(5) + ZZ(3)
sage: ZZ(5) * ZZ(3)
sage: ZZ.random_element(10**50)
sage: ZZ(27713).str(2) # Binary string representation
sage: ZZ(27713).str(16) # Hexadecimal string representation
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_93 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.commandline(_sage_const_4 , r"""
sage: Fields()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.commandline(_sage_const_5 , r"""
sage: QQ
sage: QQ(1/5) # Get an element from the field of rational numbers
sage: QQ(1/5) / QQ(3) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_164 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.commandline(_sage_const_6 , r"""
sage: GF(2)
sage: GF(2)(1) # Get an element from GF(2)
sage: GF(2)(1) + GF(2)(1) # Addition
sage: GF(2)(1) / GF(2)(1) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_213 
 _st_.commandline(_sage_const_7 , r"""
sage: ZZ(-17) // ZZ(4) # Integer quotient
sage: ZZ(-17) % ZZ(4) # remainder
sage: ZZ(-17).divides(ZZ(4))
sage: ZZ(4).divides(ZZ(12))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_218 )
try:
 _st_.current_tex_line = _sage_const_246 
 _st_.commandline(_sage_const_8 , r"""
sage: ZZ(157843853).quo_rem(ZZ(261)) # Euclidean Division
sage: ZZ(604765)*ZZ(261) + ZZ(188) # check
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_249 )
try:
 _st_.current_tex_line = _sage_const_294 
 _st_.commandline(_sage_const_9 , r"""
sage: ZZ(12).xgcd(ZZ(5)) # (gcd,s,t)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_296 )
try:
 _st_.current_tex_line = _sage_const_317 
 _st_.commandline(_sage_const_10 , r"""
sage: ZZ(7) % ZZ(271) == ZZ(2446) % ZZ(271)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_319 )
try:
 _st_.current_tex_line = _sage_const_331 
 _st_.commandline(_sage_const_11 , r"""
sage: ZZ(64)** ZZ(137) % ZZ(137) == ZZ(64)
sage: ZZ(64)** ZZ(137-1) % ZZ(137) == ZZ(1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_334 )
try:
 _st_.current_tex_line = _sage_const_392 
 _st_.commandline(_sage_const_12 , r"""
sage: CRT_list([4,1,3,0], [7,3,5,11])
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_394 )
try:
 _st_.current_tex_line = _sage_const_457 
 _st_.commandline(_sage_const_13 , r"""
sage: Z6=Integers(6) # Define integers modulo 6
sage: Z6(2)+Z6(5) # standard representatives of a class
sage: Z6(14)+Z6(-1) # different representatives for same class
sage: - Z6(2) # additive inverse
sage: Z6(5)**(-1) # multiplicative inverse if exists
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_463 )
try:
 _st_.current_tex_line = _sage_const_492 
 _st_.commandline(_sage_const_14 , r"""
sage: Z6x = Z6['x']
sage: Z6x
sage: p = Z6x([1,2,3,4])
sage: p
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_497 )
try:
 _st_.current_tex_line = _sage_const_502 
 _st_.commandline(_sage_const_15 , r"""
sage: p.degree()
sage: Z6x([0]).degree()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_505 )
try:
 _st_.current_tex_line = _sage_const_517 
 _st_.commandline(_sage_const_16 , r"""
sage: q = Z6x([5,-3,2,])
sage: p + q
sage: p*q
sage: p^2
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_903 
 _st_.commandline(_sage_const_17 , r"""
sage: EllipticCurve(GF(5),[1,0])
sage: EllipticCurve(GF(5),[1,0]).trace_of_frobenius()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_906 )
try:
 _st_.current_tex_line = _sage_const_1151 
 _st_.commandline(_sage_const_18 , r"""
sage: F43 = GF(43)
sage: F43t.<t> = F43[]
sage: F43_6.<v> = GF(43^6, name='v', modulus=t^6+6) # t^6+6 irreducible
sage: BLS6 = EllipticCurve (F43_6,[0 ,6])
sage: INF = BLS6(0) # point at infinity
sage: for P in INF.division_points(13): # PI(P) == [q]P
....:     if P.order() == 13: # exclude point at infinity
....:         PiP = BLS6([a.frobenius() for a in P])
....:         qP = 43*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1163 )
try:
 _st_.current_tex_line = _sage_const_1189 
 _st_.commandline(_sage_const_19 , r"""
sage: g1 = BLS6([13,15])
sage: g2 = BLS6([7*v^2, 16*v^3])
sage: g1.weil_pairing(g2,13)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1193 )
try:
 _st_.current_tex_line = _sage_const_1227 
 _st_.commandline(_sage_const_20 , r"""
sage: F7 = GF(7)
sage: MNT4 = EllipticCurve (F7,[4 ,1])
sage: [P.xy() for P in MNT4.points() if P.order() > 1]
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1231 )
try:
 _st_.current_tex_line = _sage_const_1258 
 _st_.commandline(_sage_const_21 , r"""
sage: F7t.<t> = F7[]
sage: F7_4.<u> = GF(7^4, name='u', modulus=t^4+t+1) # embedding degree is 4
sage: MNT4 = EllipticCurve (F7_4,[4 ,1])
sage: INF = MNT4(0) # point at infinity
sage: for P in INF.division_points(5): # PI(P) == [q]P
....:     if P.order() == 5: # exclude point at infinity
....:         PiP = MNT4([a.frobenius() for a in P])
....:         qP = 7*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1269 )
try:
 _st_.current_tex_line = _sage_const_1286 
 _st_.commandline(_sage_const_22 , r"""
sage: g1 = MNT4([0,1])
sage: g2 = MNT4(2*u^3 + 5*u^2 + 4*u + 2, 2*u^3 + 3*u + 5)
sage: g1.weil_pairing(g2,5)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1290 )
try:
 _st_.current_tex_line = _sage_const_1362 
 _st_.commandline(_sage_const_23 , r"""
sage: G.<x> = GF(5^6) # embedding degree is 6
sage: MNT6 = EllipticCurve (G,[2 ,1])
sage: INF = MNT6(0) # point at infinity
sage: for P in INF.division_points(7): # PI(P) == [q]P
....:     if P.order() == 7: # exclude point at infinity
....:         PiP = MNT6([a.frobenius() for a in P])
....:         qP = 5*P
....:         if PiP == qP:
....:             print(P.xy())
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1372 )
_st_.endofdoc()

