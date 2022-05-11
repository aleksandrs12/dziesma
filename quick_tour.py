from earsketch import *

init()
setTempo(120)


# Add Sounds
fitMedia(COMMON_LOVE_VOX_COMMON_1, 1, 11, 15)
fitMedia(COMMON_LOVE_VOX_COMMON_2, 1, 15, 16)
fitMedia(COMMON_LOVE_VOX_COMMON_3, 1, 16, 20)
fitMedia(COMMON_LOVE_VOX_COMMON_4, 1, 20, 24)
fitMedia(COMMON_LOVE_VOX_COMMON_5, 1, 24, 28)
fitMedia(COMMON_LOVE_VOX_COMMON_6, 1, 28, 32)
fitMedia(COMMON_LOVE_VOX_COMMON_7, 1, 32, 36)
fitMedia(COMMON_LOVE_VOX_COMMON_1, 1, 36, 40)

fitMedia(YG_HIP_HOP_VOX_1, 1, 40, 41)


fitMedia(MILKNSIZZ_ADIOS_CONGA_GOLD, 6, 1, 9)
fitMedia(MILKNSIZZ_BOSSA_CLUBA_LOFI_GUITAR, 5, 1, 5)
fitMedia(MILKNSIZZ_CALIENTE_DIGITAL_PERCUSSION, 4, 3, 10)
#fitMedia(MILKNSIZZ_BOSSA_CLUBA_LANEZ_BASS, 3, 5, 9)
#fitMedia(MILKNSIZZ_BUENA_VOX, 3, 5, 9)
fitMedia(MILKNSIZZ_BAYSIQUE_VOCAL_LOOP, 2, 5, 40)


# Effects fade in
#setEffect(2, VOLUME,GAIN, -20, 1, 6, 5)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
fillD = "00-0-0--0-------"
fillE = "0-0-0-0-0-0-0-0-"
fillF = "0000-00---000--0"
fillG = "-0-0-0-0-0-0-0-0"
fillH = "-00-00-00-00-00-"
fillI = "0000000000000000"
makeBeat(OS_SNARE03, 3, 4, fillA)
for n in range(10, 11):
    makeBeat(OS_SNARE03, 4, n, fillA)
for n in range(8, 11):
    makeBeat(COMMON_LOVE_DRUMBEAT_1, 3, n, fillB)
for n in range(5, 40):
    makeBeat(MILKNSIZZ_BOSSA_CLUBA_LANEZ_BASS, 5, n, fillC)
    
for n in range(16, 17):
    makeBeat(OS_SNARE03, 4, n, fillA)
for n in range(14, 17):
    makeBeat(COMMON_LOVE_DRUMBEAT_1, 3, n, fillB)


for n in range (11, 40):
    makeBeat(OS_SNARE03, 7, n, fillD)
setEffect(7, VOLUME, GAIN, -13, 40, 7)

for n in range (38, 44):
    makeBeat(MILKNSIZZ_AFROSENSE_ACCENT_PERCUSSION, 8, n, fillD)
    makeBeat(MILKNSIZZ_AFROSENSE_CLOSED_HAT, 9, n, fillE)
    
setEffect(7, VOLUME, GAIN, -13, 40, 7)
makeBeat(OS_SNARE03, 10, 37, fillG)
makeBeat(OS_SNARE03, 10, 38, fillI)
makeBeat(OS_SNARE03, 10, 39, fillI)
makeBeat(EIGHT_BIT_ANALOG_DRUM_LOOP_010, 11, 41, fillF)
setEffect(11, VOLUME, GAIN, 11)



    

    

finish()