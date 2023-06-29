#!/bin/bash

# example usage: source channel_files.sh nc_9.8_MeV.csv nc_Ar40_1n

#mkdir -p smear/ar40kt effic/ar40kt xscns
python3 adjust.py $1 $2 #csv first then output
mv xs_$2.dat ../xscns/. # temp xs dir
cp ../smear/smear_nc_nue_Ar40_ar40kt.dat ../smear/smear_$2_ar40kt.dat 
cp ../effic/effic_nc_nue_Ar40_ar40kt.dat ../effic/effic_$2_ar40kt.dat


var="energy(#$2_smear)<"
sed -i "1s/.*/$var/" ../smear/smear_$2_ar40kt.dat


# need three files
#xscns/xs_nc_Ar40_1n.dat
#smear/ar40kt/smear_nc_Ar40_1n_ar40kt.dat
#effic/ar40kt/effic_nc_Ar40_1n_ar40kt.dat


# first line for smear energy(#nc_Ar40_1n_smear)<
