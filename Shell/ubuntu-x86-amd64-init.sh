#!/bin/bash
source ./utils.sh

# --- 读取系统环境变量
release_name=$(lsb_release -cs)
# TODO 设置国外源或者国内源 修改文件
# --- end


# --- 读取命令行参数
# TODO 是否代理
# --- end

# --- 根据参数进行代理设置等
# export https_proxy=socks5://127.0.0.1:1080
deb_tempdir=$(mktemp -d tempdir.XXXXXX) 
# TODO 设置日志出处
# --- end

# --- 通过包管理安装软件
sudo apt update 
sudo apt -y upgrade
programs="vim neofetch git guake firefox chromium-browser redis mariadb-server trojan"

for program in $programs
do
    install_program $program
done
# -- end

# --- 需要另外下载的安装包
wget -c https://go.microsoft.com/fwlink/?LinkID=760868 -O ./$deb_tempdir/code.deb
wget -c https://d1.music.126.net/dmusic/netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb -O ./$deb_tempdir/netease.deb
# TODO 循环安装deb_tempdir 目录下的deb文件
# --- end

# 需要单独安装的软件
install_docker
install_qbittorrent
install_postman
install_telegram
# --- end

# TODO 安装 calibre vpn

# --- 转移文件 恢复数据 处理垃圾数据
# TODO 恢复国内源或者国外源

sudo rm -rf ./$deb_tempdir

# --- end