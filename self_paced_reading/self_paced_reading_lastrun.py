#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Sun Oct 29 15:40:09 2017
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
expName = u'self_paced_reading'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/casillas/Desktop/self_paced_reading/self_paced_reading.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_ins = visual.TextStim(win=win, name='text_ins',
    text=u'Read the sentences.\n\nUse the spacebar to advance.\n\n',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
text_fix = visual.TextStim(win=win, name='text_fix',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "w1"
w1Clock = core.Clock()
text_w1 = visual.TextStim(win=win, name='text_w1',
    text='default text',
    font=u'Arial',
    pos=(-0.3, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "w2"
w2Clock = core.Clock()
text_w2 = visual.TextStim(win=win, name='text_w2',
    text='default text',
    font=u'Arial',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "w3"
w3Clock = core.Clock()
text_w3 = visual.TextStim(win=win, name='text_w3',
    text='default text',
    font=u'Arial',
    pos=(0.0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "w4"
w4Clock = core.Clock()
text_w4 = visual.TextStim(win=win, name='text_w4',
    text='default text',
    font=u'Arial',
    pos=(0.1, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "w5"
w5Clock = core.Clock()
text_w5 = visual.TextStim(win=win, name='text_w5',
    text='default text',
    font=u'Arial',
    pos=(0.3, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "follow_up"
follow_upClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker=u'triangle', size=1.0, pos=[0.0, 0.0], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale=u'How did the sentence sound?', singleClick=True, disappear=True)

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text=u'Thank you',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
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
instructionsComponents = [text_ins, key_resp_ins]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ins* updates
    if t >= 0.0 and text_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_ins.tStart = t
        text_ins.frameNStart = frameN  # exact frame index
        text_ins.setAutoDraw(True)
    
    # *key_resp_ins* updates
    if t >= 0.0 and key_resp_ins.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_ins.tStart = t
        key_resp_ins.frameNStart = frameN  # exact frame index
        key_resp_ins.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
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
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'condition_file.csv'),
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
    
    # ------Prepare to start Routine "fix"-------
    t = 0
    fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [text_fix]
    for thisComponent in fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fix* updates
        if t >= 0.0 and text_fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fix.tStart = t
            text_fix.frameNStart = frameN  # exact frame index
            text_fix.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_fix.status == STARTED and t >= frameRemains:
            text_fix.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "w1"-------
    t = 0
    w1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_w1.setText(w1)
    key_resp_w1 = event.BuilderKeyResponse()
    # keep track of which components have finished
    w1Components = [text_w1, key_resp_w1]
    for thisComponent in w1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "w1"-------
    while continueRoutine:
        # get current time
        t = w1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_w1* updates
        if t >= 0.5 and text_w1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_w1.tStart = t
            text_w1.frameNStart = frameN  # exact frame index
            text_w1.setAutoDraw(True)
        
        # *key_resp_w1* updates
        if t >= 0.5 and key_resp_w1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_w1.tStart = t
            key_resp_w1.frameNStart = frameN  # exact frame index
            key_resp_w1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_w1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_w1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_w1.keys == []:  # then this was the first keypress
                    key_resp_w1.keys = theseKeys[0]  # just the first key pressed
                    key_resp_w1.rt = key_resp_w1.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in w1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w1"-------
    for thisComponent in w1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_w1.keys in ['', [], None]:  # No response was made
        key_resp_w1.keys=None
    trials.addData('key_resp_w1.keys',key_resp_w1.keys)
    if key_resp_w1.keys != None:  # we had a response
        trials.addData('key_resp_w1.rt', key_resp_w1.rt)
    # the Routine "w1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "w2"-------
    t = 0
    w2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_w2.setText(w2)
    key_resp_w2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    w2Components = [text_w2, key_resp_w2]
    for thisComponent in w2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "w2"-------
    while continueRoutine:
        # get current time
        t = w2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_w2* updates
        if t >= 0.0 and text_w2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_w2.tStart = t
            text_w2.frameNStart = frameN  # exact frame index
            text_w2.setAutoDraw(True)
        
        # *key_resp_w2* updates
        if t >= 0.0 and key_resp_w2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_w2.tStart = t
            key_resp_w2.frameNStart = frameN  # exact frame index
            key_resp_w2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_w2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_w2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_w2.keys == []:  # then this was the first keypress
                    key_resp_w2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_w2.rt = key_resp_w2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in w2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w2"-------
    for thisComponent in w2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_w2.keys in ['', [], None]:  # No response was made
        key_resp_w2.keys=None
    trials.addData('key_resp_w2.keys',key_resp_w2.keys)
    if key_resp_w2.keys != None:  # we had a response
        trials.addData('key_resp_w2.rt', key_resp_w2.rt)
    # the Routine "w2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "w3"-------
    t = 0
    w3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_w3.setText(w3)
    key_resp_w3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    w3Components = [text_w3, key_resp_w3]
    for thisComponent in w3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "w3"-------
    while continueRoutine:
        # get current time
        t = w3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_w3* updates
        if t >= 0.0 and text_w3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_w3.tStart = t
            text_w3.frameNStart = frameN  # exact frame index
            text_w3.setAutoDraw(True)
        
        # *key_resp_w3* updates
        if t >= 0.0 and key_resp_w3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_w3.tStart = t
            key_resp_w3.frameNStart = frameN  # exact frame index
            key_resp_w3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_w3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_w3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_w3.keys == []:  # then this was the first keypress
                    key_resp_w3.keys = theseKeys[0]  # just the first key pressed
                    key_resp_w3.rt = key_resp_w3.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in w3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w3"-------
    for thisComponent in w3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_w3.keys in ['', [], None]:  # No response was made
        key_resp_w3.keys=None
    trials.addData('key_resp_w3.keys',key_resp_w3.keys)
    if key_resp_w3.keys != None:  # we had a response
        trials.addData('key_resp_w3.rt', key_resp_w3.rt)
    # the Routine "w3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "w4"-------
    t = 0
    w4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_w4.setText(w4)
    key_resp_w4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    w4Components = [text_w4, key_resp_w4]
    for thisComponent in w4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "w4"-------
    while continueRoutine:
        # get current time
        t = w4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_w4* updates
        if t >= 0.0 and text_w4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_w4.tStart = t
            text_w4.frameNStart = frameN  # exact frame index
            text_w4.setAutoDraw(True)
        
        # *key_resp_w4* updates
        if t >= 0.0 and key_resp_w4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_w4.tStart = t
            key_resp_w4.frameNStart = frameN  # exact frame index
            key_resp_w4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_w4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_w4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_w4.keys == []:  # then this was the first keypress
                    key_resp_w4.keys = theseKeys[0]  # just the first key pressed
                    key_resp_w4.rt = key_resp_w4.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in w4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w4"-------
    for thisComponent in w4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_w4.keys in ['', [], None]:  # No response was made
        key_resp_w4.keys=None
    trials.addData('key_resp_w4.keys',key_resp_w4.keys)
    if key_resp_w4.keys != None:  # we had a response
        trials.addData('key_resp_w4.rt', key_resp_w4.rt)
    # the Routine "w4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "w5"-------
    t = 0
    w5Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_w5.setText(w5)
    key_resp_w5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    w5Components = [text_w5, key_resp_w5]
    for thisComponent in w5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "w5"-------
    while continueRoutine:
        # get current time
        t = w5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_w5* updates
        if t >= 0.0 and text_w5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_w5.tStart = t
            text_w5.frameNStart = frameN  # exact frame index
            text_w5.setAutoDraw(True)
        
        # *key_resp_w5* updates
        if t >= 0.0 and key_resp_w5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_w5.tStart = t
            key_resp_w5.frameNStart = frameN  # exact frame index
            key_resp_w5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_w5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_w5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_w5.keys == []:  # then this was the first keypress
                    key_resp_w5.keys = theseKeys[0]  # just the first key pressed
                    key_resp_w5.rt = key_resp_w5.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in w5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "w5"-------
    for thisComponent in w5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_w5.keys in ['', [], None]:  # No response was made
        key_resp_w5.keys=None
    trials.addData('key_resp_w5.keys',key_resp_w5.keys)
    if key_resp_w5.keys != None:  # we had a response
        trials.addData('key_resp_w5.rt', key_resp_w5.rt)
    # the Routine "w5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "follow_up"-------
    t = 0
    follow_upClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating.reset()
    # keep track of which components have finished
    follow_upComponents = [rating]
    for thisComponent in follow_upComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "follow_up"-------
    while continueRoutine:
        # get current time
        t = follow_upClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in follow_upComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "follow_up"-------
    for thisComponent in follow_upComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    # the Routine "follow_up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_end.status == STARTED and t >= frameRemains:
        text_end.setAutoDraw(False)
    
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
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
