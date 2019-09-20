# python 3.6.2
# coding: utf-8
#
# only called in bat because the file name and path have been locked.
#
import sys
import os

import shutil
import struct
import binascii


# -----------------------------------------------------------------------------
# pack several ‘bin’ files into one ‘bin’ file
# -----------------------------------------------------------------------------
def PackBins(bin1_filename, bin2_filename, bin_result_filename):

    print("\nstart to PackBins")

    # targets
    #bin1_offset = 0x00000000
    bin2_offset = 0x00020000
    mark_offset = 0x000C0000
    
    # total in chip flash size, count by sector11 start at 0x080E0000 of size 128KB
    bin_size = 0x100000
	
    # prepare the mark data
    mark_name = b'MARK'
    mark_flag = int(0xAA5500FF)

    print("mark_flag =", hex(mark_flag))

    mark_bytes = struct.pack("4sI", mark_name,
                                    mark_flag)

    # read in
    bin1_fd = open(bin1_filename, 'rb')
    bin2_fd = open(bin2_filename, 'rb')
    bin_merge_fd = open(bin_result_filename, 'wb')

    # start to pack bin 1 and bin 2 into one file
	# bin-1
    bin_merge_fd.seek(0)
    bin_merge_fd.write(bin1_fd.read())
    bin_merge_fd.tell()

    # gab between bin-1 and bin-2
    bin1_gabdata_bin2 = struct.pack("b", 0)
    bin_merge_fd.write(bin1_gabdata_bin2 * (bin2_offset - os.path.getsize(bin1_filename)))
    bin_merge_fd.tell()
	
    # bin-2
    bin_merge_fd.write(bin2_fd.read())
    bin_merge_fd.tell()

    # gab between bin-2 and mark area
    bin2_gabdata_mark = struct.pack("b", 0)
    bin_merge_fd.write(bin2_gabdata_mark * (mark_offset - bin2_offset - os.path.getsize(bin2_filename)))
    bin_merge_fd.tell()
	
    # mark area
    bin_merge_fd.write(mark_bytes)
    bin_merge_fd.tell()

    # gab to the end
    gab_to_end = struct.pack("b", 0)
    bin_merge_fd.write(gab_to_end * (bin_size - mark_offset - len(mark_bytes)))
    bin_merge_fd.tell()

    # close all
    bin_merge_fd.close()
    bin_merge_fd.close()
    bin_merge_fd.close()

    print("\nend of PackBins.")


# -----------------------------------------------------------------------------
# add head to file
# -----------------------------------------------------------------------------
def AddHead(in_filename, out_filename, main_version, sub_version, change_version):
    
    print("\nstart to AddHead:")

    head_bytes_offset = 0x200

    # read in
    in_file  = open(in_filename, 'rb')
    out_file = open(out_filename, 'wb')

    # prepare the head file
    firmware_name = b'SYSM'
    firmware_versiona = int(main_version<<8) | int(sub_version<<4) | change_version
    firmware_crcval = binascii.crc32(in_file.read())
    firmware_length = os.path.getsize(in_filename)

    print("firmware_versiona =", hex(firmware_versiona))
    print("firmware_crcval =", hex(firmware_crcval))
    print("firmware_length =", hex(firmware_length))

    head_bytes = struct.pack("4siIi", firmware_name,
                                       firmware_versiona,
                                       firmware_crcval,
                                       firmware_length)

    # start to pack head data and in file into out file
    out_file.seek(0)
    out_file.write(head_bytes)
    out_file.tell()

    # gab between head and file content
    head_gab = struct.pack("b", 0)
    out_file.write(head_gab*(head_bytes_offset - len(head_bytes)))
    out_file.tell()

    # in_file.read() used before, need seek(0) back to the head of in_file
    in_file.seek(0)

    out_file.write(in_file.read())
    out_file.tell()
    
    # close all
    in_file.close()
    out_file.close()

    print("\nend of AddHead.")


# -----------------------------------------------------------------------------
# make directory
# -----------------------------------------------------------------------------
def mkdir(path):

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则删除，并重新创建
        shutil.rmtree(path)

        # 创建目录操作函数
        os.makedirs(path) 

        print(path+' 目录已删除重建')
        return False


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__=='__main__':
    
    print("Program name", sys.argv[0])

    for i in range(1, len(sys.argv)):
        print("arg%d"%i, sys.argv[i])

    version = 'v{MAIN_VERSION}.{SUB_VERSION}.{CHANGE_VERSION}'.\
              format(MAIN_VERSION=sys.argv[1], SUB_VERSION=sys.argv[2], CHANGE_VERSION=sys.argv[3])

    print(version)

    # 定义要创建的目录
    mkpath = ".\\Released\\" + version
    print(mkpath)

    # 调用函数
    mkdir(mkpath)

    # rename bootloader
    bootfileorg  = ".\\Project\\bootloader\\Debug\\Exe\\bootloader.bin"
    bootfiledest = ".\\Released\\" + version + "\\bootloader-" + version + ".bin"
    shutil.copy(bootfileorg, bootfiledest)

    # add head for app
    appfileorg  = ".\\Project\\app\\Debug\\Exe\\app.bin"
    appfiledest = ".\\Released\\" + version + "\\app-" + version + ".fw"
    AddHead(appfileorg, appfiledest, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
	
    # rename unittest
    unittestfileorg  = ".\\Project\\unittest\\Debug\\Exe\\unittest.bin"
    unittestfiledest = ".\\Released\\" + version + "\\unittest-" + version + ".bin"
    shutil.copy(unittestfileorg, unittestfiledest)
	
    # pack app and bootloader into one file
    resultfiledest = ".\\Released\\" + version + "\\full-" + version + ".bin"
    PackBins(bootfiledest, appfiledest, resultfiledest)
