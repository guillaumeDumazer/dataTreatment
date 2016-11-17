#!/usr/bin/awk -f

# Moving average over every column of a data file
# Directly derived from :
# RosettaCodeData/Task/Averages-Simple-moving-average/AWK/averages-simple-moving-average.awk

BEGIN{ P = 5; }

{
    data = "";
    i = NR % P;
    for (t = 1; t<=NF; t++){
      x = $t;
      MA += (x - Z[i]) / P;
      Z[i] = x;
      printf("%f%s",MA,"\t");}
    printf "\n";
}
