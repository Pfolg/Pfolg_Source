program shuiXianHuaShu
    implicit none
    integer x,y,z,i

    do i=100,999,1
        z=MOD(i,10)  ! ��λ
        y=MOD(INT(i/10),10) ! ʮλ
        x=INT(i/100)  ! ��λ
        if (i.EQ.x**3+y**3+z**3) print*,i,"��ˮ�ɻ���"
        ! 153
        ! 370
        ! 371
        ! 407

    end do
    print*,i  ! 1000
end program shuiXianHuaShu