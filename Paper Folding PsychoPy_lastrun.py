#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Fri Dec  4 00:54:41 2020
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
expInfo = {'participant': '', 'session': 'ex. 23', 'date': 'ex. 11/20/2020'}
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
    originPath='/Users/ramyaramakrishnan/Documents/gan-college/RA/Paper Folding Folder/Paper Folding PsychoPy_lastrun.py',
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

# Initialize components for Routine "titlecard"
titlecardClock = core.Clock()
Titlecard = visual.TextStim(win=win, name='Titlecard',
    text='Welcome to the Paper Folding Experiment\n',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
response = visual.TextStim(win=win, name='response',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr"
instrClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this task, you are to imagine the folding and unfolding of pieces of paper. \n\nIn each problem in the test there are some figures drawn at the left and there are others drawn at the right. The figures at the left represent a square piece of paper being folded, and the last of these figures on the left will have small circles drawn on it to show where the paper has been punched. ',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
response2 = visual.TextStim(win=win, name='response2',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "saminstr"
saminstrClock = core.Clock()
ExProblem = visual.TextStim(win=win, name='ExProblem',
    text='Now try the sample problem on the next slide. In this problem, one hole is punched through the folded paper.\n\nRemember that the hole is punched through all the thicknesses of paper at that point. \n\nOne of the five figures at the right will show where the holes could be when the paper is completely unfolded. You are to decide which one of these figures has the correct placement of the holes and click the correct number (1, 2, 3, 4, or, 5) on your keyboard that you feel corresponds with the correct answer.',
    font='Times New Roman',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "samtrial"
samtrialClock = core.Clock()
sampleimage = visual.ImageStim(
    win=win,
    name='sampleimage', 
    image='sample_task/q1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "analysistrial"
analysistrialClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Good job! \n\n\n',
    font='Times New Roman',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sample_task/q1.png', mask=None,
    ori=0, pos=(0, 0.26), size=(0.7, .155),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
explanation = visual.TextStim(win=win, name='explanation',
    text='Notice how in this sample problem, the first image on the left represented a full paper being folded upward “hot-dog style”. Next, a hole is punched on the left side of this paper. Understanding so, you must then choose from the following 5 answer choices on the right to choose what you think the unfolded paper should now look like having been hole-punched once. \n\nRemembering the hole punch goes through both sides of the paper, a hole punch on a hot-dog style half sheet would entail two hole punches on the left side of the paper when unfolded.\n\nThe answer is 3!\n\nThis is the same paper folding method that will be used for the following problems. Here, only one fold was made, hence there were 2 boxes on the left of the answer choices. But for other problems, keep in mind that there could be more than one fold made before a hole is punched through the paper.',
    font='Times New Roman',
    pos=(0, -0.1), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
part1 = visual.TextStim(win=win, name='part1',
    text='As in the sample problem, in the following problems, all of the folds that are made are shown in the figures at the left before the answer choices. Remember, the paper is not turned or moved in any way except to make and unravel the folds in the figures. Additionally, remember that only one hole is punched through the paper.\n\nThe correct answer is the figure that shows the proper positions of the holes when the paper is completely unfolded. ',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RespInstr = keyboard.Keyboard()
resp1 = visual.TextStim(win=win, name='resp1',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructionspart2"
Instructionspart2Clock = core.Clock()
secondslidein = visual.TextStim(win=win, name='secondslidein',
    text='Your score on this test will be the questions marked correctly minus a fraction of questions marked incorrectly. Therefore, it will not be to your advantage to guess unless you are able to eliminate one or more of the answer choices as wrong.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
resp4 = visual.TextStim(win=win, name='resp4',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructionspart3"
Instructionspart3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This test has two parts. You will have 3 minutes for each of the two parts. You will not be able to go back to previous questions, so please be wary of the clock on the top left of your screen when proceeding. \n\nWhen the time is up, you will be automatically advanced to the next screen. \n',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response7 = keyboard.Keyboard()
resp5 = visual.TextStim(win=win, name='resp5',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Begin"
BeginClock = core.Clock()
Part1 = visual.TextStim(win=win, name='Part1',
    text='Part 1 (3 minutes)\n\n\nRemember to press the number (1, 2, 3, 4, or 5) on your keyboard associated with the image to select it.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Resp = keyboard.Keyboard()
resbeforetrial1 = visual.TextStim(win=win, name='resbeforetrial1',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
Questions_1 = visual.ImageStim(
    win=win,
    name='Questions_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
participant_response_1 = keyboard.Keyboard()
resptrial1 = visual.TextStim(win=win, name='resptrial1',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
countdownStarted = False
Show = visual.TextStim(win=win, name='Show',
    text='default text',
    font='Times New Roman',
    pos=(-0.6, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "intermission"
intermissionClock = core.Clock()
stop = visual.TextStim(win=win, name='stop',
    text='STOP!',
    font='Times New Roman',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
middle = visual.TextStim(win=win, name='middle',
    text='You have finished Part I. \n\nWhen you are instructed to begin Part II, click any key on your keyboard. \n\nYou will again have 3 minutes to finish Part II.',
    font='Times New Roman',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_response = keyboard.Keyboard()
respbeforetrial2 = visual.TextStim(win=win, name='respbeforetrial2',
    text='Press any key to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
Questions_2 = visual.ImageStim(
    win=win,
    name='Questions_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
participant_response_2 = keyboard.Keyboard()
number = visual.TextStim(win=win, name='number',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
countdownStarted=False
secondLoop = 0
Show_2 = visual.TextStim(win=win, name='Show_2',
    text='default text',
    font='Times New Roman',
    pos=(-0.6, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end"
endClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='You have now completed the experiment. \n\nThank you for your participation!',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
final = keyboard.Keyboard()
finalslide = visual.TextStim(win=win, name='finalslide',
    text='Press any key on your keyboard to exit the experiment.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "titlecard"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
titlecardComponents = [Titlecard, key_resp_4, response]
for thisComponent in titlecardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
titlecardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "titlecard"-------
while continueRoutine:
    # get current time
    t = titlecardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=titlecardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Titlecard* updates
    if Titlecard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Titlecard.frameNStart = frameN  # exact frame index
        Titlecard.tStart = t  # local t and not account for scr refresh
        Titlecard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Titlecard, 'tStartRefresh')  # time at next scr refresh
        Titlecard.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *response* updates
    if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response.frameNStart = frameN  # exact frame index
        response.tStart = t  # local t and not account for scr refresh
        response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
        response.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titlecardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "titlecard"-------
for thisComponent in titlecardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Titlecard.started', Titlecard.tStartRefresh)
thisExp.addData('Titlecard.stopped', Titlecard.tStopRefresh)
thisExp.addData('response.started', response.tStartRefresh)
thisExp.addData('response.stopped', response.tStopRefresh)
# the Routine "titlecard" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [Instructions, key_resp, response2]
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
    
    # *response2* updates
    if response2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response2.frameNStart = frameN  # exact frame index
        response2.tStart = t  # local t and not account for scr refresh
        response2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response2, 'tStartRefresh')  # time at next scr refresh
        response2.setAutoDraw(True)
    
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
thisExp.addData('response2.started', response2.tStartRefresh)
thisExp.addData('response2.stopped', response2.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "saminstr"-------
continueRoutine = True
# update component parameters for each repeat
instruction.keys = []
instruction.rt = []
_instruction_allKeys = []
# keep track of which components have finished
saminstrComponents = [ExProblem, instruction, text_2]
for thisComponent in saminstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
saminstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "saminstr"-------
while continueRoutine:
    # get current time
    t = saminstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=saminstrClock)
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
    
    # *instruction* updates
    waitOnFlip = False
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction.status == STARTED and not waitOnFlip:
        theseKeys = instruction.getKeys(keyList=None, waitRelease=False)
        _instruction_allKeys.extend(theseKeys)
        if len(_instruction_allKeys):
            instruction.keys = _instruction_allKeys[-1].name  # just the last key pressed
            instruction.rt = _instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in saminstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "saminstr"-------
for thisComponent in saminstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ExProblem.started', ExProblem.tStartRefresh)
thisExp.addData('ExProblem.stopped', ExProblem.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "saminstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('samplequestion.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "samtrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    samtrialComponents = [sampleimage, key_resp_3, text_3]
    for thisComponent in samtrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    samtrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "samtrial"-------
    while continueRoutine:
        # get current time
        t = samtrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=samtrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sampleimage* updates
        if sampleimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sampleimage.frameNStart = frameN  # exact frame index
            sampleimage.tStart = t  # local t and not account for scr refresh
            sampleimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sampleimage, 'tStartRefresh')  # time at next scr refresh
            sampleimage.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in samtrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "samtrial"-------
    for thisComponent in samtrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('sampleimage.started', sampleimage.tStartRefresh)
    trials_3.addData('sampleimage.stopped', sampleimage.tStopRefresh)
    trials_3.addData('text_3.started', text_3.tStartRefresh)
    trials_3.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "samtrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "analysistrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
analysistrialComponents = [text_4, image_3, explanation, text_7, key_resp_7]
for thisComponent in analysistrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
analysistrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "analysistrial"-------
while continueRoutine:
    # get current time
    t = analysistrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=analysistrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *explanation* updates
    if explanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        explanation.frameNStart = frameN  # exact frame index
        explanation.tStart = t  # local t and not account for scr refresh
        explanation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explanation, 'tStartRefresh')  # time at next scr refresh
        explanation.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=None, waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in analysistrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "analysistrial"-------
for thisComponent in analysistrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
thisExp.addData('explanation.started', explanation.tStartRefresh)
thisExp.addData('explanation.stopped', explanation.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "analysistrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr2"-------
continueRoutine = True
# update component parameters for each repeat
RespInstr.keys = []
RespInstr.rt = []
_RespInstr_allKeys = []
# keep track of which components have finished
Instr2Components = [part1, RespInstr, resp1]
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
    
    # *resp1* updates
    if resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp1.frameNStart = frameN  # exact frame index
        resp1.tStart = t  # local t and not account for scr refresh
        resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp1, 'tStartRefresh')  # time at next scr refresh
        resp1.setAutoDraw(True)
    
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
thisExp.addData('resp1.started', resp1.tStartRefresh)
thisExp.addData('resp1.stopped', resp1.tStopRefresh)
# the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructionspart2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Instructionspart2Components = [secondslidein, key_resp_6, resp4]
for thisComponent in Instructionspart2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructionspart2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructionspart2"-------
while continueRoutine:
    # get current time
    t = Instructionspart2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructionspart2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *secondslidein* updates
    if secondslidein.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        secondslidein.frameNStart = frameN  # exact frame index
        secondslidein.tStart = t  # local t and not account for scr refresh
        secondslidein.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(secondslidein, 'tStartRefresh')  # time at next scr refresh
        secondslidein.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *resp4* updates
    if resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp4.frameNStart = frameN  # exact frame index
        resp4.tStart = t  # local t and not account for scr refresh
        resp4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp4, 'tStartRefresh')  # time at next scr refresh
        resp4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructionspart2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructionspart2"-------
for thisComponent in Instructionspart2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('secondslidein.started', secondslidein.tStartRefresh)
thisExp.addData('secondslidein.stopped', secondslidein.tStopRefresh)
thisExp.addData('resp4.started', resp4.tStartRefresh)
thisExp.addData('resp4.stopped', resp4.tStopRefresh)
# the Routine "Instructionspart2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructionspart3"-------
continueRoutine = True
# update component parameters for each repeat
response7.keys = []
response7.rt = []
_response7_allKeys = []
# keep track of which components have finished
Instructionspart3Components = [text, response7, resp5]
for thisComponent in Instructionspart3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructionspart3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructionspart3"-------
while continueRoutine:
    # get current time
    t = Instructionspart3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructionspart3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *response7* updates
    waitOnFlip = False
    if response7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response7.frameNStart = frameN  # exact frame index
        response7.tStart = t  # local t and not account for scr refresh
        response7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response7, 'tStartRefresh')  # time at next scr refresh
        response7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(response7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(response7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if response7.status == STARTED and not waitOnFlip:
        theseKeys = response7.getKeys(keyList=None, waitRelease=False)
        _response7_allKeys.extend(theseKeys)
        if len(_response7_allKeys):
            response7.keys = _response7_allKeys[-1].name  # just the last key pressed
            response7.rt = _response7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *resp5* updates
    if resp5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp5.frameNStart = frameN  # exact frame index
        resp5.tStart = t  # local t and not account for scr refresh
        resp5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp5, 'tStartRefresh')  # time at next scr refresh
        resp5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructionspart3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructionspart3"-------
for thisComponent in Instructionspart3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('resp5.started', resp5.tStartRefresh)
thisExp.addData('resp5.stopped', resp5.tStopRefresh)
# the Routine "Instructionspart3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Begin"-------
continueRoutine = True
# update component parameters for each repeat
Resp.keys = []
Resp.rt = []
_Resp_allKeys = []
# keep track of which components have finished
BeginComponents = [Part1, Resp, resbeforetrial1]
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
    
    # *resbeforetrial1* updates
    if resbeforetrial1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resbeforetrial1.frameNStart = frameN  # exact frame index
        resbeforetrial1.tStart = t  # local t and not account for scr refresh
        resbeforetrial1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resbeforetrial1, 'tStartRefresh')  # time at next scr refresh
        resbeforetrial1.setAutoDraw(True)
    
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
thisExp.addData('resbeforetrial1.started', resbeforetrial1.tStartRefresh)
thisExp.addData('resbeforetrial1.stopped', resbeforetrial1.tStopRefresh)
# the Routine "Begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images and Correct Answers Part_1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Questions_1.setImage(ImageFile)
    participant_response_1.keys = []
    participant_response_1.rt = []
    _participant_response_1_allKeys = []
    #Setting Clock
    if not countdownStarted:
        countdownClock = core.CountdownTimer(180.0)
        countdownStarted = True
    # keep track of which components have finished
    trial_1Components = [Questions_1, participant_response_1, resptrial1, Show]
    for thisComponent in trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_1"-------
    while continueRoutine:
        # get current time
        t = trial_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Questions_1* updates
        if Questions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Questions_1.frameNStart = frameN  # exact frame index
            Questions_1.tStart = t  # local t and not account for scr refresh
            Questions_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Questions_1, 'tStartRefresh')  # time at next scr refresh
            Questions_1.setAutoDraw(True)
        
        # *participant_response_1* updates
        waitOnFlip = False
        if participant_response_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_response_1.frameNStart = frameN  # exact frame index
            participant_response_1.tStart = t  # local t and not account for scr refresh
            participant_response_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_response_1, 'tStartRefresh')  # time at next scr refresh
            participant_response_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(participant_response_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(participant_response_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if participant_response_1.status == STARTED and not waitOnFlip:
            theseKeys = participant_response_1.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _participant_response_1_allKeys.extend(theseKeys)
            if len(_participant_response_1_allKeys):
                participant_response_1.keys = _participant_response_1_allKeys[0].name  # just the first key pressed
                participant_response_1.rt = _participant_response_1_allKeys[0].rt
                # was this correct?
                if (participant_response_1.keys == str(corrAns)) or (participant_response_1.keys == corrAns):
                    participant_response_1.corr = 1
                else:
                    participant_response_1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *resptrial1* updates
        if resptrial1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resptrial1.frameNStart = frameN  # exact frame index
            resptrial1.tStart = t  # local t and not account for scr refresh
            resptrial1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resptrial1, 'tStartRefresh')  # time at next scr refresh
            resptrial1.setAutoDraw(True)
        #Establishing and Displaying Timer
        timeRemaining = countdownClock.getTime()
        if timeRemaining <=0.00:
            continueRoutine = False
            trials.finished = True
            countdownStarted = False
            continueExperiment = True
        else:
            minutes = int (timeRemaining/60.00)
            seconds = int (timeRemaining - (minutes*60.00))
            timeText = str(minutes) + ':'  + str(seconds) 
        
            
        
        # *Show* updates
        if Show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Show.frameNStart = frameN  # exact frame index
            Show.tStart = t  # local t and not account for scr refresh
            Show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Show, 'tStartRefresh')  # time at next scr refresh
            Show.setAutoDraw(True)
        if Show.status == STARTED:  # only update if drawing
            Show.setText(timeText, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_1"-------
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Questions_1.started', Questions_1.tStartRefresh)
    trials.addData('Questions_1.stopped', Questions_1.tStopRefresh)
    # check responses
    if participant_response_1.keys in ['', [], None]:  # No response was made
        participant_response_1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           participant_response_1.corr = 1;  # correct non-response
        else:
           participant_response_1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('participant_response_1.keys',participant_response_1.keys)
    trials.addData('participant_response_1.corr', participant_response_1.corr)
    if participant_response_1.keys != None:  # we had a response
        trials.addData('participant_response_1.rt', participant_response_1.rt)
    trials.addData('participant_response_1.started', participant_response_1.tStartRefresh)
    trials.addData('participant_response_1.stopped', participant_response_1.tStopRefresh)
    trials.addData('resptrial1.started', resptrial1.tStartRefresh)
    trials.addData('resptrial1.stopped', resptrial1.tStopRefresh)
    trials.addData('Show.started', Show.tStartRefresh)
    trials.addData('Show.stopped', Show.tStopRefresh)
    # the Routine "trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "intermission"-------
continueRoutine = True
# update component parameters for each repeat
key_response.keys = []
key_response.rt = []
_key_response_allKeys = []
# keep track of which components have finished
intermissionComponents = [stop, middle, key_response, respbeforetrial2]
for thisComponent in intermissionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intermissionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intermission"-------
while continueRoutine:
    # get current time
    t = intermissionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intermissionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop* updates
    if stop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop.frameNStart = frameN  # exact frame index
        stop.tStart = t  # local t and not account for scr refresh
        stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop, 'tStartRefresh')  # time at next scr refresh
        stop.setAutoDraw(True)
    
    # *middle* updates
    if middle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        middle.frameNStart = frameN  # exact frame index
        middle.tStart = t  # local t and not account for scr refresh
        middle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(middle, 'tStartRefresh')  # time at next scr refresh
        middle.setAutoDraw(True)
    
    # *key_response* updates
    waitOnFlip = False
    if key_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_response.frameNStart = frameN  # exact frame index
        key_response.tStart = t  # local t and not account for scr refresh
        key_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
        key_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_response.status == STARTED and not waitOnFlip:
        theseKeys = key_response.getKeys(keyList=None, waitRelease=False)
        _key_response_allKeys.extend(theseKeys)
        if len(_key_response_allKeys):
            key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
            key_response.rt = _key_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *respbeforetrial2* updates
    if respbeforetrial2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respbeforetrial2.frameNStart = frameN  # exact frame index
        respbeforetrial2.tStart = t  # local t and not account for scr refresh
        respbeforetrial2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respbeforetrial2, 'tStartRefresh')  # time at next scr refresh
        respbeforetrial2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intermissionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intermission"-------
for thisComponent in intermissionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop.started', stop.tStartRefresh)
thisExp.addData('stop.stopped', stop.tStopRefresh)
thisExp.addData('middle.started', middle.tStartRefresh)
thisExp.addData('middle.stopped', middle.tStopRefresh)
thisExp.addData('respbeforetrial2.started', respbeforetrial2.tStartRefresh)
thisExp.addData('respbeforetrial2.stopped', respbeforetrial2.tStopRefresh)
# the Routine "intermission" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images and Correct Answers Part_2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Questions_2.setImage(ImageFile)
    participant_response_2.keys = []
    participant_response_2.rt = []
    _participant_response_2_allKeys = []
    #Clock
    if secondLoop<=0:
        countdownClock = core.CountdownTimer(180)
        countdownStarted = True
        secondLoop = secondLoop +1
    # keep track of which components have finished
    trial_2Components = [Questions_2, participant_response_2, number, Show_2]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2"-------
    while continueRoutine:
        # get current time
        t = trial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Questions_2* updates
        if Questions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Questions_2.frameNStart = frameN  # exact frame index
            Questions_2.tStart = t  # local t and not account for scr refresh
            Questions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Questions_2, 'tStartRefresh')  # time at next scr refresh
            Questions_2.setAutoDraw(True)
        
        # *participant_response_2* updates
        waitOnFlip = False
        if participant_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_response_2.frameNStart = frameN  # exact frame index
            participant_response_2.tStart = t  # local t and not account for scr refresh
            participant_response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_response_2, 'tStartRefresh')  # time at next scr refresh
            participant_response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(participant_response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(participant_response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if participant_response_2.status == STARTED and not waitOnFlip:
            theseKeys = participant_response_2.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _participant_response_2_allKeys.extend(theseKeys)
            if len(_participant_response_2_allKeys):
                participant_response_2.keys = _participant_response_2_allKeys[0].name  # just the first key pressed
                participant_response_2.rt = _participant_response_2_allKeys[0].rt
                # was this correct?
                if (participant_response_2.keys == str(corrAns)) or (participant_response_2.keys == corrAns):
                    participant_response_2.corr = 1
                else:
                    participant_response_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *number* updates
        if number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            number.frameNStart = frameN  # exact frame index
            number.tStart = t  # local t and not account for scr refresh
            number.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(number, 'tStartRefresh')  # time at next scr refresh
            number.setAutoDraw(True)
        #Creating Clock
        timeRemaining = countdownClock.getTime()
        if timeRemaining <=0.00:
            continueRoutine = False
            trials2.finished = True
            countdownStarted = False
            continueExperiment = True
        else:
            minutes = int (timeRemaining/60.00)
            seconds = int (timeRemaining - (minutes*60.00))
            timeText = str(minutes) + ':'  + str(seconds) 
        
        # *Show_2* updates
        if Show_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Show_2.frameNStart = frameN  # exact frame index
            Show_2.tStart = t  # local t and not account for scr refresh
            Show_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Show_2, 'tStartRefresh')  # time at next scr refresh
            Show_2.setAutoDraw(True)
        if Show_2.status == STARTED:  # only update if drawing
            Show_2.setText(timeText, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Questions_2.started', Questions_2.tStartRefresh)
    trials_2.addData('Questions_2.stopped', Questions_2.tStopRefresh)
    # check responses
    if participant_response_2.keys in ['', [], None]:  # No response was made
        participant_response_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           participant_response_2.corr = 1;  # correct non-response
        else:
           participant_response_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('participant_response_2.keys',participant_response_2.keys)
    trials_2.addData('participant_response_2.corr', participant_response_2.corr)
    if participant_response_2.keys != None:  # we had a response
        trials_2.addData('participant_response_2.rt', participant_response_2.rt)
    trials_2.addData('participant_response_2.started', participant_response_2.tStartRefresh)
    trials_2.addData('participant_response_2.stopped', participant_response_2.tStopRefresh)
    trials_2.addData('number.started', number.tStartRefresh)
    trials_2.addData('number.stopped', number.tStopRefresh)
    trials_2.addData('Show_2.started', Show_2.tStartRefresh)
    trials_2.addData('Show_2.stopped', Show_2.tStopRefresh)
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
final.keys = []
final.rt = []
_final_allKeys = []
# keep track of which components have finished
endComponents = [thankyou, final, finalslide]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if thankyou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.tStart = t  # local t and not account for scr refresh
        thankyou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankyou, 'tStartRefresh')  # time at next scr refresh
        thankyou.setAutoDraw(True)
    
    # *final* updates
    waitOnFlip = False
    if final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final.frameNStart = frameN  # exact frame index
        final.tStart = t  # local t and not account for scr refresh
        final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final, 'tStartRefresh')  # time at next scr refresh
        final.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(final.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(final.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if final.status == STARTED and not waitOnFlip:
        theseKeys = final.getKeys(keyList=None, waitRelease=False)
        _final_allKeys.extend(theseKeys)
        if len(_final_allKeys):
            final.keys = _final_allKeys[-1].name  # just the last key pressed
            final.rt = _final_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *finalslide* updates
    if finalslide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalslide.frameNStart = frameN  # exact frame index
        finalslide.tStart = t  # local t and not account for scr refresh
        finalslide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalslide, 'tStartRefresh')  # time at next scr refresh
        finalslide.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thankyou.started', thankyou.tStartRefresh)
thisExp.addData('thankyou.stopped', thankyou.tStopRefresh)
# check responses
if final.keys in ['', [], None]:  # No response was made
    final.keys = None
thisExp.addData('final.keys',final.keys)
if final.keys != None:  # we had a response
    thisExp.addData('final.rt', final.rt)
thisExp.addData('final.started', final.tStartRefresh)
thisExp.addData('final.stopped', final.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('finalslide.started', finalslide.tStartRefresh)
thisExp.addData('finalslide.stopped', finalslide.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
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
