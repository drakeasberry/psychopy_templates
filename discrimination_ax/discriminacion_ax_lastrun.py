#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.03),
    on Mon Oct 16 15:47:11 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'discrimination_ax'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/code/psychopy/psychopy_templates/discrimination_ax/discriminacion_ax.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
insructions = visual.TextStim(win=win, name='insructions',
    text=u'Listen to the following sequences of sounds. \n\nYour task is to determine if they are the same or different. \n\nIf they are the same, press 1. If they are different, press 0.\n\nRespond as quickly as possible without making mistakes. \n\nPress the space bar to begin. ',
    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_stim1 = sound.Sound('A', secs=-1)
sound_stim1.setVolume(1)
sound_stim2 = sound.Sound('A', secs=-1)
sound_stim2.setVolume(1)
text_response_same = visual.TextStim(win=win, name='text_response_same',
    text=u'Same',
    font=u'Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_response_diff = visual.TextStim(win=win, name='text_response_diff',
    text=u'Different',
    font=u'Arial',
    pos=[0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_trial_cross = visual.TextStim(win=win, name='text_trial_cross',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-5.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text=u'Thank you.',
    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_ins = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [insructions, key_resp_ins]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insructions* updates
    if t >= 0.0 and insructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        insructions.tStart = t
        insructions.frameNStart = frameN  # exact frame index
        insructions.setAutoDraw(True)
    
    # *key_resp_ins* updates
    if t >= 0.0 and key_resp_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_ins.tStart = t
        key_resp_ins.frameNStart = frameN  # exact frame index
        key_resp_ins.status = STARTED
        # keyboard checking is just starting
    if key_resp_ins.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'condition_file/trials.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    sound_stim1.setSound(stim1, secs=0.25)
    sound_stim2.setSound(stim2, secs=0.25)
    key_resp_trial = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [sound_stim1, sound_stim2, text_response_same, text_response_diff, key_resp_trial, text_trial_cross]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_stim1
        if t >= 0.25 and sound_stim1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_stim1.tStart = t
            sound_stim1.frameNStart = frameN  # exact frame index
            sound_stim1.play()  # start the sound (it finishes automatically)
        frameRemains = 0.25 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_stim1.status == STARTED and t >= frameRemains:
            sound_stim1.stop()  # stop the sound (if longer than duration)
        # start/stop sound_stim2
        if t >= 1 and sound_stim2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_stim2.tStart = t
            sound_stim2.frameNStart = frameN  # exact frame index
            sound_stim2.play()  # start the sound (it finishes automatically)
        frameRemains = 1 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_stim2.status == STARTED and t >= frameRemains:
            sound_stim2.stop()  # stop the sound (if longer than duration)
        
        # *text_response_same* updates
        if t >= 0.25 and text_response_same.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_response_same.tStart = t
            text_response_same.frameNStart = frameN  # exact frame index
            text_response_same.setAutoDraw(True)
        frameRemains = 0.25 + 2.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_response_same.status == STARTED and t >= frameRemains:
            text_response_same.setAutoDraw(False)
        
        # *text_response_diff* updates
        if t >= 0.25 and text_response_diff.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_response_diff.tStart = t
            text_response_diff.frameNStart = frameN  # exact frame index
            text_response_diff.setAutoDraw(True)
        frameRemains = 0.25 + 2.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_response_diff.status == STARTED and t >= frameRemains:
            text_response_diff.setAutoDraw(False)
        
        # *key_resp_trial* updates
        if t >= 1.0 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
        frameRemains = 1.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_trial.status == STARTED and t >= frameRemains:
            key_resp_trial.status = STOPPED
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_trial.keys == []:  # then this was the first keypress
                    key_resp_trial.keys = theseKeys[0]  # just the first key pressed
                    key_resp_trial.rt = key_resp_trial.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_trial.keys == str(isCorrect)) or (key_resp_trial.keys == isCorrect):
                        key_resp_trial.corr = 1
                    else:
                        key_resp_trial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *text_trial_cross* updates
        if t >= 0.0 and text_trial_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_trial_cross.tStart = t
            text_trial_cross.frameNStart = frameN  # exact frame index
            text_trial_cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_trial_cross.status == STARTED and t >= frameRemains:
            text_trial_cross.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_stim1.stop()  # ensure sound has stopped at end of routine
    sound_stim2.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
        key_resp_trial.keys=None
        # was no response the correct answer?!
        if str(isCorrect).lower() == 'none':
           key_resp_trial.corr = 1  # correct non-response
        else:
           key_resp_trial.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    trials.addData('key_resp_trial.corr', key_resp_trial.corr)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_end = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [text_end, key_resp_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t
        text_end.frameNStart = frameN  # exact frame index
        text_end.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_end.status == STARTED and t >= frameRemains:
        text_end.setAutoDraw(False)
    
    # *key_resp_end* updates
    if t >= 0.0 and key_resp_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_end.tStart = t
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
    if key_resp_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_end.keys = theseKeys[-1]  # just the last key pressed
            key_resp_end.rt = key_resp_end.clock.getTime()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_end.keys in ['', [], None]:  # No response was made
    key_resp_end.keys=None
thisExp.addData('key_resp_end.keys',key_resp_end.keys)
if key_resp_end.keys != None:  # we had a response
    thisExp.addData('key_resp_end.rt', key_resp_end.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
