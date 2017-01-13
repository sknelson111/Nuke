import shutil

def saveAlternateNukeScript(appendedText):

    #Save a copy of your nuke script with a new filename, then continue
    #working on your current copy. 
    
    origScriptName = nuke.root().name()
    scriptLength = len(origScriptName)
    newScriptName = origScriptName[0:scriptLength-3] + str(appendedText) + origScriptName[scriptLength-3:scriptLength]

    shutil.copyfile(origScriptName, newScriptName)
    nuke.scriptSaveAs(filename=newScriptName, overwrite=1)
    nuke.scriptSaveAs(filename=origScriptName, overwrite=1)

    return newScriptName

appendedText = "_alternate"
saveAlternateNukeScript(appendedText)