input = """3 CFGBR, 9 PFMFC, 2 FQFPN => 2 PKPWN
9 XQHK => 3 KDXDC
9 MPQFZ, 6 SGHLD => 6 DXPTR
6 QDBK, 2 SGHLD => 3 WDJKB
1 RXJS, 9 XQHK => 4 GTXPN
2 XJHR, 3 WNFC => 4 NRLM
3 RHWD => 7 NDQK
3 PZXG, 3 TNCBS, 1 GNSW => 7 CFGBR
1 VRMZK => 2 TVDH
3 JQFP => 8 VRMZK
124 ORE => 6 NKRXN
2 KRDMT, 11 MPQFZ => 2 WDWNX
3 ZPCP => 9 WLMB
2 MPQFZ => 1 DQRQW
13 KHXVX => 8 RHWD
5 ZPVWS => 8 JQFP
1 NDQK, 1 JZQN, 1 GNSW => 6 XHRQW
4 KRDMT => 7 HCVLB
3 NRLM => 9 WHWK
172 ORE => 5 ZPCP
104 ORE => 1 TJHD
1 LFPG => 6 TNCBS
3 XJHR => 9 TVBNZ
3 JQFP => 4 DSJK
3 ZPVWS => 3 SGHLD
15 NRLM, 5 KDXDC, 1 DQRQW, 5 WDWNX, 12 RXJS, 3 GTXPN => 5 QTSK
1 WDWNX => 1 GNSW
1 QDBK => 1 LBTRH
3 FQFPN, 13 WDWNX => 4 RXJS
1 QDBK => 7 MPQFZ
6 LBTRH, 6 TVDH => 6 JDKMB
4 KWXF, 8 XJHR => 9 JZQN
8 MPQFZ, 8 VRMZK => 7 WNFC
16 QGZSZ, 9 XHRQW, 17 MRBFL, 10 WHWK, 36 JDKMB, 82 LFNZ, 11 TDRWG, 7 QTSK, 7 MNWVT, 6 CDNHC, 3 NDQK, 4 TNCBS => 1 FUEL
1 DQRQW, 1 MRBFL, 1 GTXPN, 1 CFGBR, 2 HCVLB, 1 DGXBN, 3 GZQSX => 8 QGZSZ
13 SGHLD, 11 XQHK, 17 PKPWN, 1 RXJS, 1 FQFPN, 11 JZQN => 1 CDNHC
21 NKRXN, 9 TJHD, 2 ZXJCJ => 5 KHXVX
2 WLMB => 8 XJKTS
2 WDJKB => 6 KRDMT
2 MGXB, 1 KWXF => 8 LFNZ
1 TVBNZ, 5 VRMZK => 8 CSDWQ
7 LFPG => 8 TDRWG
1 RHWD, 8 XJKTS => 2 QDBK
182 ORE => 4 ZXJCJ
3 ZXJCJ => 8 ZPVWS
1 WNFC, 2 CSDWQ, 2 NRLM => 6 GZQSX
4 TVDH, 2 DGXBN => 6 MRBFL
3 DSJK => 4 FQFPN
9 NDQK, 7 WLMB => 2 KWXF
4 CSDWQ => 2 XQHK
1 NKRXN => 5 PZXG
2 LFPG => 2 DGXBN
7 MGXB => 7 XJHR
2 WLMB => 7 LFPG
8 DXPTR, 7 WNFC, 5 MPQFZ => 9 PFMFC
5 PFMFC, 4 NRLM => 9 MNWVT
7 ZPVWS, 14 ZPCP, 11 TJHD => 2 MGXB"""

ex1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

ex2 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

ex3 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

ex4 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

ex5 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""


def factory(s, fuel):
    recipes = {}
    for recipe in s.splitlines():
        ingredients, product = recipe.split(' => ')
        prod_quantity, prod_item = product.split()
        ingredients_list = [(int(i.split()[0]), i.split()[1]) for i in ingredients.split(', ')]
        recipes[prod_item] = (int(prod_quantity), ingredients_list)

    current = {r: 0 for r in recipes.keys()}
    current['ORE'] = 0
    current['FUEL'] = fuel

    while any(i != 'ORE' and q > 0 for i, q in current.items()):
        for i, q in current.items():
            if q <= 0 or i == 'ORE':
                continue
            result_i, parts = recipes[i]
            crafts = max(current[i] // result_i, 1)
            current[i] -= result_i * crafts

            for part_q, part_i in parts:
                current[part_i] += part_q * crafts

    return current['ORE']


assert factory(ex1, 1) == 31
assert factory(ex2, 1) == 165
assert factory(ex3, 1) == 13312
assert factory(ex4, 1) == 180697
assert factory(ex5, 1) == 2210736
print(factory(input, 1))  # 273638


def count_fuel(s, ore):
    lo = 1
    hi = ore

    while lo < hi:
        mid = (lo + hi) // 2
        if factory(s, mid) > ore:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


ore = 1000000000000
assert count_fuel(ex3, ore) == 82892753
assert count_fuel(ex4, ore) == 5586022
assert count_fuel(ex5, ore) == 460664
print(count_fuel(input, ore))  # 4200533
