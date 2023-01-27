# AudioMute_Maya

1. Download the audioMuterScript.py file, and place it in your scripts folder where your Maya is installed. 

2. Copy the following lines and make them a button inside of Maya.

#################################

import audioMuterScript as aMS
aMST = aMS.audioMuter()

#################################

3. When you launch this button, you will be prompted to type in the name of your audio node - the name that appears in the outliner. 

4. Press load and the window will close.

5. Copy the following lines and make them a custom shortcut inside of Maya. 

#################################

import audioMuterScript as aMS
aMST.muteToggle()

#################################

6. The custom shortcut should now toggle the mute of the audio clip you inputted in step 3. 

7. Be aware that in order for the toggle to take effect, the playback must be paused. You can still use the toggle while it is playing, but it won't take 
effect until it has been paused again. 
