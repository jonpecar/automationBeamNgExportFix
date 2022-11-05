# automationBeamNgExportFix
Small python package to fix immediate turbo overheating in cars exported from Automation into BeamNG Drive.

This is a basic python module which will modify the engine configurations as exported from Automation: The Car Company Tycoon Game for use in BeamNG Drive. 
It will modify `cylinderWallTemperatureDamageThreshold` and `damageThresholdTemperature` to have the value `99999999` so that there is no risk of the different
 thermal modelling between the games causing cars to fail immediately due to overheat.
 
Can be used with the `-f FILE` argument to operate on a given zip or with the `-a N` argument to operate on N number of most recent zips in the BeamNG Drive mods folder of 
the current user. Tool will automatically detect the latest BeamNG version directory, but a different version can be specified with the `-v V` argument.
