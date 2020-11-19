#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Fri Oct 30 20:45:47 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'Paper Folding PsychoPy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ramyaramakrishnan/Documents/gan-college/stroop/Paper Folding PsychoPy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='Paper Folding Test\n\n\nIn this test you are to imagine the folding and unfolding of pieces of paper. In each problem in the test there are some figures drawn at the left and there are others drawn at the right. The figures at the left represent a square piece of paper being folded, and the last of these figures has one or two small circles drawn on it to show where the paper has been punched. Each hole is punched through all the thicknesses of paper at that point. One of the five figures at the right shows where the holes will be when the paper is completely unfolded. You are to decide which one of these figures is correct and click that number below the figure on your keyboard (‘1’, ‘2’, ‘3’, ‘4’, or ‘5’). \n\n\nOn the next slide, you will be given an example problem in which only one hole was punched in the folded paper. When you are ready, click any key to go to the sample problem.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
ExProblem = visual.TextStim(win=win, name='ExProblem',
    text='Now try the sample problem below. (In this problem only one hole was punched in the folded paper.)',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ExResponse = keyboard.Keyboard()

# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
part1 = visual.TextStim(win=win, name='part1',
    text='Good job! Please read the rest of the instructions below before beginning the exam.  \n\nIn these problems all of the folds that are made are shown in the figures at the left, and the paper is not turned or moved in any way except to make the folds shown in the figures. Remember, the correct answer is the figure that shows the positions of the holes when the paper is completely unfolded. \n\nYour score on this test will be the number marked correctly minus a fraction of the number marked incorrectly. Therefore, it will not be to your advantage to guess unless you are able to eliminate one or more of the answer choices as wrong.\n\nThis test has two parts. You will have 3 minutes for each of the two parts. Please use the entire time to select and check over your answers. When the time is up, you will be automatically advanced to the next screen. \n\nPress any key to continue',
    font='Times New Roman',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RespInstr = keyboard.Keyboard()

# Initialize components for Routine "Begin"
BeginClock = core.Clock()
Part1 = visual.TextStim(win=win, name='Part1',
    text='Part 1 (3 minutes)\n\n\nRemember to press the number associated with your image to click it. \n\n\nPress any key to begin',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [Instructions, key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ExTrial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ExTrial')
thisExp.addLoop(ExTrial)  # add the loop to the experiment
thisExTrial = ExTrial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExTrial.rgb)
if thisExTrial != None:
    for paramName in thisExTrial:
        exec('{} = thisExTrial[paramName]'.format(paramName))

for thisExTrial in ExTrial:
    currentLoop = ExTrial
    # abbreviate parameter names if possible (e.g. rgb = thisExTrial.rgb)
    if thisExTrial != None:
        for paramName in thisExTrial:
            exec('{} = thisExTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    ExResponse.keys = []
    ExResponse.rt = []
    _ExResponse_allKeys = []
    # keep track of which components have finished
    trialComponents = [ExProblem, ExResponse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ExProblem* updates
        if ExProblem.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ExProblem.frameNStart = frameN  # exact frame index
            ExProblem.tStart = t  # local t and not account for scr refresh
            ExProblem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExProblem, 'tStartRefresh')  # time at next scr refresh
            ExProblem.setAutoDraw(True)
        
        # *ExResponse* updates
        waitOnFlip = False
        if ExResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExResponse.frameNStart = frameN  # exact frame index
            ExResponse.tStart = t  # local t and not account for scr refresh
            ExResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExResponse, 'tStartRefresh')  # time at next scr refresh
            ExResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ExResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ExResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ExResponse.status == STARTED and not waitOnFlip:
            theseKeys = ExResponse.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _ExResponse_allKeys.extend(theseKeys)
            if len(_ExResponse_allKeys):
                ExResponse.keys = _ExResponse_allKeys[-1].name  # just the last key pressed
                ExResponse.rt = _ExResponse_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ExTrial.addData('ExProblem.started', ExProblem.tStartRefresh)
    ExTrial.addData('ExProblem.stopped', ExProblem.tStopRefresh)
    # check responses
    if ExResponse.keys in ['', [], None]:  # No response was made
        ExResponse.keys = None
    ExTrial.addData('ExResponse.keys',ExResponse.keys)
    if ExResponse.keys != None:  # we had a response
        ExTrial.addData('ExResponse.rt', ExResponse.rt)
    ExTrial.addData('ExResponse.started', ExResponse.tStartRefresh)
    ExTrial.addData('ExResponse.stopped', ExResponse.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'ExTrial'


# ------Prepare to start Routine "Instr2"-------
continueRoutine = True
# update component parameters for each repeat
RespInstr.keys = []
RespInstr.rt = []
_RespInstr_allKeys = []
# keep track of which components have finished
Instr2Components = [part1, RespInstr]
for thisComponent in Instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr2"-------
while continueRoutine:
    # get current time
    t = Instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *part1* updates
    if part1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part1.frameNStart = frameN  # exact frame index
        part1.tStart = t  # local t and not account for scr refresh
        part1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part1, 'tStartRefresh')  # time at next scr refresh
        part1.setAutoDraw(True)
    
    # *RespInstr* updates
    waitOnFlip = False
    if RespInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RespInstr.frameNStart = frameN  # exact frame index
        RespInstr.tStart = t  # local t and not account for scr refresh
        RespInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RespInstr, 'tStartRefresh')  # time at next scr refresh
        RespInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RespInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RespInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RespInstr.status == STARTED and not waitOnFlip:
        theseKeys = RespInstr.getKeys(keyList=None, waitRelease=False)
        _RespInstr_allKeys.extend(theseKeys)
        if len(_RespInstr_allKeys):
            RespInstr.keys = _RespInstr_allKeys[-1].name  # just the last key pressed
            RespInstr.rt = _RespInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr2"-------
for thisComponent in Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('part1.started', part1.tStartRefresh)
thisExp.addData('part1.stopped', part1.tStopRefresh)
# the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Begin"-------
continueRoutine = True
# update component parameters for each repeat
Resp.keys = []
Resp.rt = []
_Resp_allKeys = []
# keep track of which components have finished
BeginComponents = [Part1, Resp]
for thisComponent in BeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Begin"-------
while continueRoutine:
    # get current time
    t = BeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Part1* updates
    if Part1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Part1.frameNStart = frameN  # exact frame index
        Part1.tStart = t  # local t and not account for scr refresh
        Part1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Part1, 'tStartRefresh')  # time at next scr refresh
        Part1.setAutoDraw(True)
    
    # *Resp* updates
    waitOnFlip = False
    if Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Resp.frameNStart = frameN  # exact frame index
        Resp.tStart = t  # local t and not account for scr refresh
        Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Resp, 'tStartRefresh')  # time at next scr refresh
        Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Resp.status == STARTED and not waitOnFlip:
        theseKeys = Resp.getKeys(keyList=None, waitRelease=False)
        _Resp_allKeys.extend(theseKeys)
        if len(_Resp_allKeys):
            Resp.keys = _Resp_allKeys[-1].name  # just the last key pressed
            Resp.rt = _Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begin"-------
for thisComponent in BeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Part1.started', Part1.tStartRefresh)
thisExp.addData('Part1.stopped', Part1.tStopRefresh)
# the Routine "Begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
