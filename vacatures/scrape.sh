#!/bin/bash
#Cron job to run the scraper each day

cd ~/anish/Olympia/vacatures

_now = $(date +"%m_%d_%Y")
_file ="backup_$_now.csv"

scrapy crawl vacatures -o "$_file" -t csv