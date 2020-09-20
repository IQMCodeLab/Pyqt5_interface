import numpy as np
from palettable.cmocean.diverging import Balance_5,Balance_5_r,Curl_4,Delta_3,Curl_4_r,Curl_5,Curl_5_r,Curl_9,Curl_9_r,Delta_18,Delta_18_r,Curl_3,Curl_3_r
from palettable.cmocean.sequential import Solar_10,Amp_10,Amp_10_r,Gray_16_r,Ice_10_r,Matter_10_r,Gray_16,Ice_10,Matter_10
from palettable.colorbrewer.diverging import BrBG_8,BrBG_8_r,RdBu_10_r,RdBu_10,Spectral_7,Spectral_7_r
#from palettable.colorbrewer.diverging import BrBG_8,RdBu_10,Sperctral_7,
from palettable.colorbrewer.sequential import Blues_9,Blues_9_r,Purples_6,Purples_6_r,YlOrRd_6,YlOrRd_6_r
from palettable.lightbartlein.diverging import BlueDarkOrange18_9,BlueDarkOrange18_9_r,BlueGray_2,BlueGray_2_r,BrownBlue10_7,BrownBlue10_7_r
from palettable.lightbartlein.sequential import Blues7_2,Blues7_2_r
from palettable.scientific.diverging import Broc_13,Broc_13_r,Roma_8,Roma_8_r,Vik_4,Vik_4_r,Vik_20_r,Vik_20
from palettable.scientific.sequential import Bamako_7,Bamako_7_r,Davos_3,Davos_3_r,LaJolla_7,LaJolla_7_r,Nuuk_6,Nuuk_6_r,Oslo_15,Oslo_15_r
from palettable.cartocolors.diverging import Fall_4,Fall_4_r ,Earth_3,Earth_3_r,TealRose_4,TealRose_4_r,Temps_4,Temps_4_r
from palettable.cartocolors.sequential import BluGrn_7,BluGrn_7_r,BluYl_4,BluYl_4_r,DarkMint_3,DarkMint_3_r,OrYel_4_r,OrYel_4,Teal_5,Teal_5_r
def colorlistfunction():
    cnumbers = []
    cnamelist = []



    cdicts = Balance_5.colors
    cnumbers.append(np.shape(Balance_5.colors)[0])
    cnamelist.append(Balance_5.name)

    cdicts = np.append(cdicts, Earth_3.colors, axis=0)
    cnumbers.append(np.shape(Earth_3.colors)[0])
    cnamelist.append(Earth_3.name)

    cdicts = np.append(cdicts, Earth_3_r.colors, axis=0)
    cnumbers.append(np.shape(Earth_3_r.colors)[0])
    cnamelist.append(Earth_3_r.name)


    cdicts = np.append(cdicts, Balance_5_r.colors, axis=0)
    cnumbers.append(np.shape(Balance_5_r.colors)[0])
    cnamelist.append(Balance_5_r.name)

    cdicts = np.append(cdicts, Fall_4.colors, axis=0)
    cnumbers.append(np.shape(Fall_4.colors)[0])
    cnamelist.append(Fall_4.name)


    cdicts = np.append(cdicts, Fall_4_r.colors, axis=0)
    cnumbers.append(np.shape(Fall_4_r.colors)[0])
    cnamelist.append(Fall_4_r.name)

    cdicts = np.append(cdicts, Curl_4.colors, axis=0)
    cnumbers.append(np.shape(Curl_4.colors)[0])
    cnamelist.append(Curl_4.name)


    cdicts = np.append(cdicts, Delta_3.colors, axis=0)
    cnumbers.append(np.shape(Delta_3.colors)[0])
    cnamelist.append(Delta_3.name)


    cdicts = np.append(cdicts, Curl_3.colors, axis=0)
    cnumbers.append(np.shape(Curl_3.colors)[0])
    cnamelist.append(Curl_3.name)

    cdicts = np.append(cdicts, Curl_3_r.colors, axis=0)
    cnumbers.append(np.shape(Curl_3_r.colors)[0])
    cnamelist.append(Curl_3_r.name)

    cdicts = np.append(cdicts, Curl_4_r.colors, axis=0)
    cnumbers.append(np.shape(Curl_4_r.colors)[0])
    cnamelist.append(Curl_4_r.name)


    cdicts = np.append(cdicts, Curl_5.colors, axis=0)
    cnumbers.append(np.shape(Curl_5.colors)[0])
    cnamelist.append(Curl_5.name)

    cdicts = np.append(cdicts, Curl_5_r.colors, axis=0)
    cnumbers.append(np.shape(Curl_5_r.colors)[0])
    cnamelist.append(Curl_5_r.name)

    cdicts = np.append(cdicts, Curl_9.colors, axis=0)
    cnumbers.append(np.shape(Curl_9.colors)[0])
    cnamelist.append(Curl_9.name)

    cdicts = np.append(cdicts, Curl_9_r.colors, axis=0)
    cnumbers.append(np.shape(Curl_9_r.colors)[0])
    cnamelist.append(Curl_9_r.name)

    cdicts = np.append(cdicts, Amp_10.colors, axis=0)
    cnumbers.append(np.shape(Amp_10.colors)[0])
    cnamelist.append(Amp_10.name)

    cdicts = np.append(cdicts, Amp_10_r.colors, axis=0)
    cnumbers.append(np.shape(Amp_10_r.colors)[0])
    cnamelist.append(Amp_10_r.name)

    cdicts = np.append(cdicts, Gray_16.colors, axis=0)
    cnumbers.append(np.shape(Gray_16.colors)[0])
    cnamelist.append(Gray_16.name)

    cdicts = np.append(cdicts, Ice_10.colors, axis=0)
    cnumbers.append(np.shape(Ice_10.colors)[0])
    cnamelist.append(Ice_10.name)

    cdicts = np.append(cdicts, Ice_10_r.colors, axis=0)
    cnumbers.append(np.shape(Ice_10_r.colors)[0])
    cnamelist.append(Ice_10_r.name)

    cdicts = np.append(cdicts, Matter_10.colors, axis=0)
    cnumbers.append(np.shape(Matter_10.colors)[0])
    cnamelist.append(Matter_10.name)

    cdicts = np.append(cdicts, Matter_10_r.colors, axis=0)
    cnumbers.append(np.shape(Matter_10_r.colors)[0])
    cnamelist.append(Matter_10_r.name)

    cdicts = np.append(cdicts, BrBG_8.colors, axis=0)
    cnumbers.append(np.shape(BrBG_8.colors)[0])
    cnamelist.append(BrBG_8.name)

    cdicts = np.append(cdicts, BrBG_8_r.colors, axis=0)
    cnumbers.append(np.shape(BrBG_8_r.colors)[0])
    cnamelist.append(BrBG_8_r.name)

    cdicts = np.append(cdicts, RdBu_10.colors, axis=0)
    cnumbers.append(np.shape(RdBu_10.colors)[0])
    cnamelist.append(RdBu_10.name)

    cdicts = np.append(cdicts, RdBu_10_r.colors, axis=0)
    cnumbers.append(np.shape(RdBu_10_r.colors)[0])
    cnamelist.append(RdBu_10_r.name)

    cdicts = np.append(cdicts, Spectral_7.colors, axis=0)
    cnumbers.append(np.shape(Spectral_7.colors)[0])
    cnamelist.append(Spectral_7.name)

    cdicts = np.append(cdicts, Blues_9.colors, axis=0)
    cnumbers.append(np.shape(Blues_9.colors)[0])
    cnamelist.append(Blues_9.name)

    cdicts = np.append(cdicts, Blues_9_r.colors, axis=0)
    cnumbers.append(np.shape(Blues_9_r.colors)[0])
    cnamelist.append(Blues_9_r.name)

    cdicts = np.append(cdicts, Solar_10.colors, axis=0)
    cnumbers.append(np.shape(Solar_10.colors)[0])
    cnamelist.append(Solar_10.name)

    cdicts = np.append(cdicts, Purples_6.colors, axis=0)
    cnumbers.append(np.shape(Purples_6.colors)[0])
    cnamelist.append(Purples_6.name)

    cdicts = np.append(cdicts, Purples_6_r.colors, axis=0)
    cnumbers.append(np.shape(Purples_6_r.colors)[0])
    cnamelist.append(Purples_6_r.name)

    cdicts = np.append(cdicts, YlOrRd_6.colors, axis=0)
    cnumbers.append(np.shape(YlOrRd_6.colors)[0])
    cnamelist.append(YlOrRd_6.name)

    cdicts = np.append(cdicts, YlOrRd_6_r.colors, axis=0)
    cnumbers.append(np.shape(YlOrRd_6_r.colors)[0])
    cnamelist.append(YlOrRd_6_r.name)

    cdicts = np.append(cdicts, BlueDarkOrange18_9.colors, axis=0)
    cnumbers.append(np.shape(BlueDarkOrange18_9.colors)[0])
    cnamelist.append(BlueDarkOrange18_9.name)

    cdicts = np.append(cdicts, BlueDarkOrange18_9_r.colors, axis=0)
    cnumbers.append(np.shape(BlueDarkOrange18_9_r.colors)[0])
    cnamelist.append(BlueDarkOrange18_9_r.name)

    cdicts = np.append(cdicts, BlueGray_2.colors, axis=0)
    cnumbers.append(np.shape(BlueGray_2.colors)[0])
    cnamelist.append(BlueGray_2.name)

    cdicts = np.append(cdicts, BlueGray_2_r.colors, axis=0)
    cnumbers.append(np.shape(BlueGray_2_r.colors)[0])
    cnamelist.append(BlueGray_2_r.name)

    cdicts = np.append(cdicts, BrownBlue10_7.colors, axis=0)
    cnumbers.append(np.shape(BrownBlue10_7.colors)[0])
    cnamelist.append(BrownBlue10_7.name)

    cdicts = np.append(cdicts, BrownBlue10_7_r.colors, axis=0)
    cnumbers.append(np.shape(BrownBlue10_7_r.colors)[0])
    cnamelist.append(BrownBlue10_7_r.name)

    cdicts = np.append(cdicts, Blues7_2.colors, axis=0)
    cnumbers.append(np.shape(Blues7_2.colors)[0])
    cnamelist.append(Blues7_2.name)

    cdicts = np.append(cdicts, Blues7_2_r.colors, axis=0)
    cnumbers.append(np.shape(Blues7_2_r.colors)[0])
    cnamelist.append(Blues7_2_r.name)

    cdicts = np.append(cdicts, Broc_13.colors, axis=0)
    cnumbers.append(np.shape(Broc_13.colors)[0])
    cnamelist.append(Broc_13.name)

    cdicts = np.append(cdicts, Broc_13_r.colors, axis=0)
    cnumbers.append(np.shape(Broc_13_r.colors)[0])
    cnamelist.append(Broc_13_r.name)

    cdicts = np.append(cdicts, Roma_8.colors, axis=0)
    cnumbers.append(np.shape(Roma_8.colors)[0])
    cnamelist.append(Roma_8.name)

    cdicts = np.append(cdicts, Roma_8_r.colors, axis=0)
    cnumbers.append(np.shape(Roma_8_r.colors)[0])
    cnamelist.append(Roma_8_r.name)

    cdicts = np.append(cdicts, Vik_4.colors, axis=0)
    cnumbers.append(np.shape(Vik_4.colors)[0])
    cnamelist.append(Vik_4.name)

    cdicts = np.append(cdicts, Vik_4_r.colors, axis=0)
    cnumbers.append(np.shape(Vik_4_r.colors)[0])
    cnamelist.append(Vik_4_r.name)

    cdicts = np.append(cdicts, Vik_20.colors, axis=0)
    cnumbers.append(np.shape(Vik_20.colors)[0])
    cnamelist.append(Vik_20.name)

    cdicts = np.append(cdicts, Vik_20_r.colors, axis=0)
    cnumbers.append(np.shape(Vik_20_r.colors)[0])
    cnamelist.append(Vik_20_r.name)

    cdicts = np.append(cdicts, Bamako_7.colors, axis=0)
    cnumbers.append(np.shape(Bamako_7.colors)[0])
    cnamelist.append(Bamako_7.name)

    cdicts = np.append(cdicts, Bamako_7_r.colors, axis=0)
    cnumbers.append(np.shape(Bamako_7_r.colors)[0])
    cnamelist.append(Bamako_7_r.name)

    cdicts = np.append(cdicts, Davos_3.colors, axis=0)
    cnumbers.append(np.shape(Davos_3.colors)[0])
    cnamelist.append(Davos_3.name)

    cdicts = np.append(cdicts, Davos_3_r.colors, axis=0)
    cnumbers.append(np.shape(Davos_3_r.colors)[0])
    cnamelist.append(Davos_3_r.name)

    cdicts = np.append(cdicts, LaJolla_7.colors, axis=0)
    cnumbers.append(np.shape(LaJolla_7.colors)[0])
    cnamelist.append(LaJolla_7.name)

    cdicts = np.append(cdicts, LaJolla_7_r.colors, axis=0)
    cnumbers.append(np.shape(LaJolla_7_r.colors)[0])
    cnamelist.append(LaJolla_7_r.name)

    cdicts = np.append(cdicts, Nuuk_6.colors, axis=0)
    cnumbers.append(np.shape(Nuuk_6.colors)[0])
    cnamelist.append(Nuuk_6.name)

    cdicts = np.append(cdicts, Nuuk_6_r.colors, axis=0)
    cnumbers.append(np.shape(Nuuk_6_r.colors)[0])
    cnamelist.append(Nuuk_6_r.name)

    cdicts = np.append(cdicts, Oslo_15.colors, axis=0)
    cnumbers.append(np.shape(Oslo_15.colors)[0])
    cnamelist.append(Oslo_15.name)

    cdicts = np.append(cdicts, Oslo_15_r.colors, axis=0)
    cnumbers.append(np.shape(Oslo_15_r.colors)[0])
    cnamelist.append(Oslo_15_r.name)

    cdicts = np.append(cdicts, TealRose_4.colors, axis=0)
    cnumbers.append(np.shape(TealRose_4.colors)[0])
    cnamelist.append(TealRose_4.name)

    cdicts = np.append(cdicts, TealRose_4_r.colors, axis=0)
    cnumbers.append(np.shape(TealRose_4_r.colors)[0])
    cnamelist.append(TealRose_4_r.name)

    cdicts = np.append(cdicts, Temps_4.colors, axis=0)
    cnumbers.append(np.shape(Temps_4.colors)[0])
    cnamelist.append(Temps_4.name)

    cdicts = np.append(cdicts, Temps_4_r.colors, axis=0)
    cnumbers.append(np.shape(Temps_4_r.colors)[0])
    cnamelist.append(Temps_4_r.name)

    cdicts = np.append(cdicts, BluGrn_7.colors, axis=0)
    cnumbers.append(np.shape(BluGrn_7.colors)[0])
    cnamelist.append(BluGrn_7.name)

    cdicts = np.append(cdicts, BluGrn_7_r.colors, axis=0)
    cnumbers.append(np.shape(BluGrn_7_r.colors)[0])
    cnamelist.append(BluGrn_7_r.name)

    cdicts = np.append(cdicts, BluYl_4.colors, axis=0)
    cnumbers.append(np.shape(BluYl_4.colors)[0])
    cnamelist.append(BluYl_4.name)

    cdicts = np.append(cdicts, BluYl_4_r.colors, axis=0)
    cnumbers.append(np.shape(BluYl_4_r.colors)[0])
    cnamelist.append(BluYl_4_r.name)

    cdicts = np.append(cdicts, DarkMint_3.colors, axis=0)
    cnumbers.append(np.shape(DarkMint_3.colors)[0])
    cnamelist.append(DarkMint_3.name)

    cdicts = np.append(cdicts, DarkMint_3_r.colors, axis=0)
    cnumbers.append(np.shape(DarkMint_3_r.colors)[0])
    cnamelist.append(DarkMint_3_r.name)

    cdicts = np.append(cdicts, OrYel_4.colors, axis=0)
    cnumbers.append(np.shape(OrYel_4.colors)[0])
    cnamelist.append(OrYel_4.name)

    cdicts = np.append(cdicts, OrYel_4_r.colors, axis=0)
    cnumbers.append(np.shape(OrYel_4_r.colors)[0])
    cnamelist.append(OrYel_4_r.name)

    cdicts = np.append(cdicts, Teal_5.colors, axis=0)
    cnumbers.append(np.shape(Teal_5.colors)[0])
    cnamelist.append(Teal_5.name)

    cdicts = np.append(cdicts, Teal_5_r.colors, axis=0)
    cnumbers.append(np.shape(Teal_5_r.colors)[0])
    cnamelist.append(Teal_5_r.name)

    cdicts_normalize = np.divide(cdicts,256)
    colorlist = {}
    start = 0
    end = 0
    lens = np.shape(cnumbers)[0]
    print(lens)
    for i in range(lens):
        end = start + cnumbers[i]
        colorlist[cnamelist[i]] = cdicts_normalize[start:end, :]
        start = cnumbers[i]+start

    return colorlist,lens,cnamelist
if __name__ == '__main__':
    colo,lens,cnamelist = colorlistfunction()
    print(cnamelist)
    print(colo['Curl_4'])
    print(Curl_4.colors)