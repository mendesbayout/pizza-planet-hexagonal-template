#!/bin/sh

set -e
echo "Entering local folder..."
cd local
echo "Deleting old conflicting files to avoid errors..."

if [ -f /tmp/done ] ; then
  rm /tmp/done
fi

if [ -d .terraform ] ; then
  rm -rf .terraform
fi

if [ -f terraform.tfstate ] ; then
  rm terraform.tfstate
fi

echo "Executing tflocal init..."
tflocal init
echo "Executing tflocal apply..."
tflocal apply -auto-approve
echo "tflocal commands applied successfully"
touch /tmp/done
sleep 10s
exit 0
