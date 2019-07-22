#!/bin/bash

# ##########################################
# シェル実行時に引数を変数で指定し、その引数を値にevalで評価して値を取得
# multi_args.sh A B
# ##########################################


# A=1
# B=2
# C=3

## target file
TARGET="/hogehoge/hogehoeg"

## Empty the log file
/bin/cp /dev/null  ${TARGET}

## Get  statistics
${CMD} > /dev/null 2>&1

## 引数分回す
_resut=""
for((i=1;i<$#+1;i++))
do
  # 引数Aを評価し、1を取得
  arg=$(eval echo \"\$$i\")
  
  # 1の値をfigに入れてawkにわたし、対象ファイルの1カラム目を取得し変数に格納する
  # 変数には追記で格納し複数の引数指定に対応
  _result+=$(awk -v "fig=$(eval echo '$'${arg})" -F' ' '{printf "%s,", $fig}' ${TARGET})
done

## ゴミ消し
echo ${_result} | sed -e 's/,$//g'

# exit
exit 0
