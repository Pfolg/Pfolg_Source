program ex01_31
    ! ��һ�������ֵ���������һ������Сֵ����
    ! ��������
    implicit none
    real x(10)
    real a,b,mid
    integer i,ia,ib
    ! ��ֵ
    read*, x
    a=0
    b=999999999
    ! ������
    do i=1,10
        if (x(i)>a)then
            a=x(i)
            ia=i
        else if (x(i)<b)then
            b=x(i)
            ib=i
        end if
    end do
    mid=x(1)
    x(1)=a
    x(ia)=mid
    mid=x(10)
    x(10)=b
    x(ib)=mid
    ! ���
    print*,x
    ! ���
!     4,5,6,8,9,1,2,5,8,7
!    9.00000000       5.00000000       6.00000000       8.00000000       4.00000000       7.00000000       2.00000000       5.00000000       8.00000000       1.00000000
end program ex01_31