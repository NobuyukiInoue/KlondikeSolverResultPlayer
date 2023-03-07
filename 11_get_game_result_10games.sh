#!/bin/bash

GAME_RESULT_PATH="./game_results"

for i in {1..10} ; do
  FNAME=$(printf "${GAME_RESULT_PATH}/G%05d.txt" ${i})
# printf "FNAME=${FNAME}\n"
  printf "./KlondikeSolver /G ${i} /MVS > ${FNAME}\n"
  ./KlondikeSolver /G ${i} /MVS > ${FNAME}
done
