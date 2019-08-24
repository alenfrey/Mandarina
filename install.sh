#!/bin/bash

cd ..
current_dir="$PWD"
site_package_dir=$(python -m site --user-site)
sudo cp -r $current_dir/mandarina $site_package_dir