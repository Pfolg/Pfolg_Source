program ex02_08
    implicit none
    ! p287 li-12.2
    integer,parameter::m=5,n=4
    real t(m,n),DayAverTemp(m),RowSum,sum,aver
    character*10 DateMark(m)
    integer i,j
    ! ��ȡ���ݲ�����
    open(unit=10,file="source.dat")! Ĭ��˳��
    print*,"�������ں�ÿ���ĸ�ʱ�̵��¶ȣ�"
    read*,(DateMark(i),(t(i,j),j=1,n),i=1,m)
    write(10,100) (DateMark(i),(t(i,j),j=1,n),i=1,m)
    ! ��ȡ����
    rewind(10)! ָ�뷴�Ƶ��ļ�ͷ
    read(10,100)(DateMark(i),(t(i,j),j=1,n),i=1,m)
    sum=0
    do i=1,m
        RowSum=0
        do j=1,n
            RowSum=RowSum+t(i,j)
            sum=sum+t(i,j)
        end do
        DayAverTemp(i)=RowSum/n
    end do
    aver=sum/(m*n)
    ! �����result.dat
    open(unit=11,file="result.dat")
    write(11,"(A)")"    ����        ��ƽ���¶�"
    write(11,"(A10,I6)")(DateMark(i),DayAverTemp(i),i=1,m)
    write(11,"('�ܵ�ƽ���¶�Ϊ��',I5)")aver
    100 format(A10,2X,4I4)
    200 format(A15,4I8)
    close(10)
    close(11)

end program ex02_08