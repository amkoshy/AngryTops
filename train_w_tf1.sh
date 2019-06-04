#!/usr/bin/env bash
source /home/fsyed/.bashrc
#source /home/fsyed/tf/bin/activate

/usr/bin/python train_simple_model.py training_$1 $2 $3 $4

/usr/bin/python fit.py CheckPoints/training_$1
/usr/bin/python histograms.py CheckPoints/training_$1
/usr/bin/python MakeContourPlots.py CheckPoints/training_$1
/usr/bin/python plot_observables.py CheckPoints/training_$1
