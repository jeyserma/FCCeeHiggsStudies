# FCCeeHiggsStudies
ZH recoil studies (mass and xsec measurement)

The FCCee Higgs studies consists of two main steps:

1. Analysis of Ntuples (Whizard/Pythia + Delphes) using the FCCee framework tools
2. Statistical analysis with Combine

Analysis
--------

Analysis framework based on RDataframe to run over all the Ntuples.

For each session, run

```
source initFCC.sh
```


Combine
-------
Installation standalone version of Combine: instructions see comments in initCombine.sh (lxplus7). For each session, run

```
source initCombine.sh
```

The main scripts are stored in the fitAnalysis directory.

Steps to run Combine (provided the necessary recoil distributions obtaind from step 1):

1. Prepare datacard (text file) and make workspace (ROOT file). 
2. Convert datacard + workspace to Combine workspace
3. Run the necessary grid scans

**Step 1** Datacard can be found in fitAnalysis/combine/datacard.txt. It contains the signal and background process, their links to the RooFit workspaces and a list of nuisance parameters to be taken into account. The workspace is generated using fitAnalysis/fitAnalysis/makeWS_2CBG.py. It basically models the signal and backgrounds with RooFit objects, as well as the systematics. 

**Step 2** Conversion of workspace to a Combine workspace:

```
text2workspace datacard.txt -o ws.root
```
This command is attached to the end of the makeWS_2CBG.py file. It produces the Combine workspace ws.root, which is used for all Combine commands and run the fits.

**Step 3** Using the ws.root, one can run a single fit to the signal strength (r):
```
combine -M FitDiagnostics -t -1 --expectSignal=1 ws.root -m 125 -v 10 --X-rtd ADDNLL_CBNLL=0 
```
It does a likelihood fit and returns the signal strength with the uncertainty. As we inject 1 unit of signal (--expectSignal=1), the fit result should give identical results.

To run a grid scan for the signal strength between 0.95 and 1.05 (100 points equally spaced), run:
```
combine -M MultiDimFit -t -1 --setParameterRanges r=0.95,1.05 --points=100 --algo=grid ws.root --expectSignal=1 -m 125 --X-rtd TMCSO_AdaptivePseudoAsimov -v 10 --X-rtd ADDNLL_CBNLL=0
```
For a grid scan using the Higgs mass as parameter of interest (between 124.99 and 125.01 GeV) use:
```
combine -M MultiDimFit -t -1 --setParameterRanges MH=124.99,125.01 --points=%d --algo=grid ws.root --expectSignal=1 -m 125 --redefineSignalPOIs MH --X-rtd TMCSO_AdaptivePseudoAsimov -v 10 --X-rtd ADDNLL_CBNLL=0
```
A script to run, analyze and make plots of the grid scans can be found at fitAnalysis/gridScans.py.
