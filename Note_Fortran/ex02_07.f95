program ex02_07
    implicit none
    ! ����һ���и�ʽ˳���ļ�ex02_07.txt���ڴ��ļ���д��3�ֲ�ͬ���͵�����
    integer::num=100
    real::value=58.93
    character(len=20)::string="Hello,World!"

    open(8,file='ex02_07.txt')! �򿪸�ʽ˳���ļ�
    write(8,"(I6)")num
    write(8,"(F8.3)")value
    write(8,"(A10)")string
    close(8)
end program ex02_07