#!/bin/sh
/home/vhserver/gsm/vhserver stop
timestamp=$(date +"%Y-%m-%d-%H%M%S")
worlds_tarball="worlds-${timestamp}.tar.gz"
s3_prefix="s3://valheim-gsm-backups"

rm -f /home/vhserver/gsm/lgsm/backup/*
/home/vhserver/gsm/vhserver backup
aws s3 cp /home/vhserver/gsm/lgsm/backup/* ${s3_prefix}/server/

mkdir -p /home/vhserver/worlds-backup
find /home/vhserver/worlds-backup -mtime 7 -type f -delete
tar czfP /home/vhserver/worlds-backup/${worlds_tarball} /home/vhserver/.config/unity3d/IronGate/Valheim/worlds
aws s3 cp /home/vhserver/worlds-backup/${worlds_tarball} ${s3_prefix}/worlds/$worlds_tarball
