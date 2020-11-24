

def mesImpots(revenu):
    tranche1= 9964
    tranche2= 27519
    tranche3= 73779
    tranche4=  156244
    
    if revenu<tranche1:
        return 0
    elif revenu<tranche2:
        return (revenu-tranche1)*0.14
    elif revenu<tranche3:
        return (revenu-tranche2)*0.30+(tranche2-tranche1)*0.14
    elif revenu<tranche4:
        return (revenu-tranche3)*0.41+(tranche3-tranche2)*0.30+(tranche2-tranche1)*0.14
    elif revenu>tranche4:
        return (revenu-tranche4)*0.45+(tranche4-tranche3)*0.41+(tranche3-tranche2)*0.30+(tranche2-tranche1)*0.14

print(mesImpots(50000))


