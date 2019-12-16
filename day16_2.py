input = "59713137269801099632654181286233935219811755500455380934770765569131734596763695509279561685788856471420060118738307712184666979727705799202164390635688439701763288535574113283975613430058332890215685102656193056939765590473237031584326028162831872694742473094498692690926378560215065112055277042957192884484736885085776095601258138827407479864966595805684283736114104361200511149403415264005242802552220930514486188661282691447267079869746222193563352374541269431531666903127492467446100184447658357579189070698707540721959527692466414290626633017164810627099243281653139996025661993610763947987942741831185002756364249992028050315704531567916821944"

def real_signal(s):
    offset = int(s[:7])
    signal = s * 10000

    digits = [int(d) for d in signal[offset:]]
    for _ in range(100):
        total = 0
        for i, d in reversed(list(enumerate(digits))):
            total += d
            digits[i] = total % 10
    return ''.join([str(d) for d in digits])[:8]

assert real_signal("03036732577212944063491565474664") == "84462026"
assert real_signal("02935109699940807407585447034323") == "78725270"
assert real_signal("03081770884921959731165446850517") == "53553731"
print(real_signal(input))  # 80722126