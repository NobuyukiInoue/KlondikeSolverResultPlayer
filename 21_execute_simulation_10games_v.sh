#!/bin/bash

GAME_RESULT_PATH="./game_results"
DISP_DIRRECTION="-v"
ENABLE_WAIT_ENTERKEY=false
WAIT_TIME=10

for i in {1..10} ; do
  FNAME=$(printf "${GAME_RESULT_PATH}/G%05d.txt" ${i})
  printf "python ./KlondikeSolverResultPlayer.py ${FNAME} ${DISP_DIRRECTION} ${ENABLE_WAIT_ENTERKEY} ${WAIT_TIME}\n "
  python ./KlondikeSolverResultPlayer.py ${FNAME} ${DISP_DIRRECTION} ${ENABLE_WAIT_ENTERKEY} ${WAIT_TIME}
done
