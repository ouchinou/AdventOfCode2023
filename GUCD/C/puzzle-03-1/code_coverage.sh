#!/bin/bash

# Sepcify and test the target selection
echo -n "Specify target : (native/CM0/CM3/CM4/CM7)"
read target

if [ ${target} = "native" ]; then
    NAME="main"
elif [[ ${target} =~ CM[0347] ]]; then
    NAME="main-${target}.elf-main"
else
    echo "Wrong target chosen..."
    exit $1
fi

# Paths config
SRC_PATH="./src"
OUT_PATH="./out"
APP="${SRC_PATH}/${NAME}.c"

# Initialize return code value
ret=0

# GCOV job on the main.c file
gcov -b ${APP} -o ${OUT_PATH} 
ret=$(( ret + $? ))

if [[ ${ret} -eq 0 ]]; then
    echo "[GCOV] Succeed"
else
    echo "[GCOV] Failed"
    exit ${ret}
fi

# GCOVR job on the previous GCOV out file
gcovr --html-details coverage.html
ret=$(( ret + $? ))
if [[ ${ret} -eq 0 ]]; then
    echo "[GCOVR] Succeed"
else
    echo "[GCOVR] Failed"
fi

exit ${ret}
