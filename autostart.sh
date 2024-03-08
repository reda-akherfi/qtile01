#!/bin/bash 

kill $(pgrep sxhkd)
sxhkd &
redshift -x
redshift -O 3000

