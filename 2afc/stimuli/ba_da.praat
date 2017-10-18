#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Create a ba/da continuum in Praat.app                                   # 
# The script is taken from the praat manual                               # 
# and can be accessed here:                                               # 
# https://github.com/praat/praat/blob/master/dwtest/ba-da-continuum.praat # 
#                                                                         #
# Modifications by Joseph V. Casillas (8/31/2017)                         # 
# ba_da.praat                                                             # 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


nsounds = 10
t1 = 0.05
t2 = t1+0.05
tm = 0.3

kg = Create KlattGrid... kg 0 tm 9 1 1 6  1 1 1

Add pitch point... 0 150

Add pitch point... tm 100

Add voicing amplitude point... t1 65
Add voicing amplitude point... t2 80
Add open phase point... t1 0.7
Add collision phase point... t1 0.05

#Add aspiration amplitude point... t1 30
#Add aspiration amplitude point... t2 40
 
Add oral formant frequency point... 1 t1 100
Add oral formant bandwidth point... 1 t1 50
Add oral formant frequency point... 1 t2 800

Add oral formant bandwidth point... 2 t1 100
Add delta formant bandwidth point... 1 t1 100

for iformant from 3 to 9
  frequency = (2 * iformant - 1) * 500
  Add oral formant frequency point... iformant t2 frequency
  Add oral formant bandwidth point... iformant t1 frequency 
  Add oral formant bandwidth point... iformant t2 frequency / 15
endfor

for isound to nsounds
  select kg
  Remove oral formant frequency points... 2 0 tm
  f2 = 100 + (2900 / (nsounds - 1)) * (isound - 1)
  Add oral formant frequency point... 2 t1 f2
  Add oral formant frequency point... 2 t2 1200
  To Sound
  Fade out... All tm -0.005 y
  Rename... bada'isound'
endfor

# cleanup

select kg
Remove


##################
# Save continuum #
##################

# Save file prompt with opt out
beginPause ("Save file")
  comment ("Would you like to save the files?")
clicked = endPause ("No", "Yes", 2, 1)
if clicked = 1
  exit The contimuum was not saved
endif

# Where to save
dir$ = chooseDirectory$ ("Where you woud like to save the sound files?")
if dir$ = ""
  exit The continuum was not saved.
endif

# Final check
beginPause ("Save files")
  comment ("Ok! Save continuum.")
clicked = endPause ("Save", 1)
if clicked = 1

  select all
  k = numberOfSelected ("Sound")
  for i from 1 to k
    sound'i'= selected ("Sound",i)
  endfor

  for i from 1 to k
    select sound'i'
    sound$ = selected$("Sound")
    printline 'sound$'
    Save as WAV file... 'dir$'/'sound$'.wav
  endfor
endif
