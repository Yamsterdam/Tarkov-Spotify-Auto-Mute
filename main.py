import cv2, numpy
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pyautogui
screenWidth, screenHeight = pyautogui.size()
sessions = AudioUtilities.GetAllSessions()

while True:
    print("checkStart")
    if (pyautogui.locateOnScreen('start.PNG', confidence=0.7) is not None):  
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Spotify.exe":
                    print("StartEnd")
                    volume.SetMasterVolume(0, None)   
    print("checkEnd")
    if (pyautogui.locateOnScreen('end.PNG', confidence=0.7) is not None):  
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Spotify.exe":
                print("End")
                volume.SetMasterVolume(1, None)