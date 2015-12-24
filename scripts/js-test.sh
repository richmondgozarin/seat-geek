#!/bin/bash

BASE_DIR=`dirname $0`

karma start $BASE_DIR/../angular-app/tests/config/karma.conf.js $*
