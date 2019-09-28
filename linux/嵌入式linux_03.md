# 嵌入式linux开发 03

## 嵌入式编程基础知识

### 3.1 交叉编译工具选项说明

#### 3.1.1 arm-linux-gcc选项

一个C/C++程序文件要经过预处理（preprocessing）、编译（compilation）、汇编（assembly）、连接（linking）等四步骤才能生成可执行文件。

-c 预处理、编译和汇编源文件，但是不作连接，编译器根据源文件生成OBJ文件。可以配合 -o 选项生成自定义名称.o文件

-S 编译后即停止，不进行汇编。

-E 预处理后即停止，不进行编译。

-o 制定输出文件。

-v 显示GCC工具自身时的配置命令，同时显示编译器驱动程序、预处理器、编译器的版本号。


-Wall 告警选项（Waring Option）打开所有需要注意的告警信息。

-g 以操作系统的本地格式（stabs\COFF\XCOFF或DWARF）产生调试信息，GDB能够使用这些调试信息。

-O 或者 -O1 优化
-O2 更进一步优化
-O3 
-O0 不优化

连接器选项（Linker Option）
object-file-name X.o文件

-library 连接名为library的库文件
-L 指定库路径

-nostartfiles 不连接系统标准启动文件，而标准库文件仍然正常使用。

-nostdlib 不连接系统标准启动文件和标准库，只把指定的文件传递给连接器。这个选项常用于内核、bootloader等程序，他们不需要启动文件、标准库文件。

-static 在支持动态连接的系统上阻止连接共享库

-shared 生产一个共享OBJ文件，它可以和其他OBJ文件连接产生可执行文件。只有部分系统支持该选项。

-Xlinker option 把选选option传递给连接器。可用来传递系统特定的连接选项，GCC无法识别这些选项。如果需要传递携带参数的选项，必须使用两次-Xlinker,一次传递选项，一次传递参数。

-Wl,option 把选项传option 传递给连接器。如果option内含有逗号，就在逗号处分割成多个选项。连接器通常是通过gcc、arm-linux-gcc等命令间接启动的，要向它传入参数时，参数前边加上 -Wl,

-u symbol 使连接器认为取消了symbol的符合定义，从而连接库模块以取得定义。

目录选项（Directory Option）
-Idir 头文件路径

-Ldir 库路径

-Bprefix 指出何处寻找可执行文件

#### 3.1.2 arm-linux-ld
arm-linux-ld 用于将多个目标文件、库文件连接成可执行文件。
1.直接指定代码段、数据段、bss段的起始地址
-Ttext startaddr
-Tdata startaddr
-Tbss  startaddr

2.使用连接脚本设置地址

#### 3.1.3 arm-linux-objcopy 选项
arm-linux-objcopy被用来复制一个目标文件的内容到另一个文件中，可以使用不同源文件的格式来输出目标文件，即可以进行格式转换。

#### 3.1.4 arm-linux-objdump
arm-linux-objdump用于显示二进制文件信息，常用来查看反汇编代码。

#### 3.1.5 汇编代码、机器码和存储器的关系以及数据的表示

#### 3.2 Makefile介绍
linux中使用make命令编译较大的程序。make命令依赖Makefile文件

Makefile规则

目标：依赖
    命令

#### 3.3 常用ARM汇编指令及ATPCS规则
1.相对跳转指令b 、bl

2.数据传送指令mov 地址读取伪指令ldr

3.内存访问指令ldr str ldm stm

4.加减 add sub

5.程序状态寄存器的访问指令 msr mrs

6.其他伪指令

