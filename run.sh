#!/bin/bash

GODEBUG=gctrace=1 go run main.go |& tee $1
