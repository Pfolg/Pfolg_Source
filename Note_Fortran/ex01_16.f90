program forWhile

    ! ��֮����ѭ��
    implicit none
    real s

    integer i,x,y,z,k,m,n
    x=1
    y=7
    z=2

    ! 3
    do m=1,10,4  ! С�ģ�������һ��if
        n=m
    end do
    print *,m,n



    ! 1
    s=0
    do i=1,100,1
        s=s+i
    end do
    print*,s,MAX(INT((5.6-1.2+1.4)/1.4),0)

    ! 2
    do k=x,y,z+1  ! ���ȼ���ѭ���Ĵ������ı�����¼��㣿��š���
        ! ѭ���忪ʼ  ����ѭ�������������ٸ�ֵ
        x=2
        y=y+x
        z=z*k
        print*,k,x,y,z
        ! ѭ�������
        !    1           2           9           2
        !    4           2          11           8
        !    7           2          13          56
    end do


    

end program forWhile
