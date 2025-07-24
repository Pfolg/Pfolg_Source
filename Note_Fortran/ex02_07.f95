program ex02_07
    implicit none
    ! 创建一个有格式顺序文件ex02_07.txt，在此文件中写入3种不同类型的数据
    integer::num=100
    real::value=58.93
    character(len=20)::string="Hello,World!"

    open(8,file='ex02_07.txt')! 打开格式顺序文件
    write(8,"(I6)")num
    write(8,"(F8.3)")value
    write(8,"(A10)")string
    close(8)
end program ex02_07