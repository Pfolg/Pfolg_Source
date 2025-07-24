program forWhile

    ! 总之就是循环
    implicit none
    real s

    integer i,x,y,z,k,m,n
    x=1
    y=7
    z=2

    ! 3
    do m=1,10,4  ! 小心，这里有一个if
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
    do k=x,y,z+1  ! 会先计算循环的次数，改变会重新计算？大概……
        ! 循环体开始  这里循环变量不允许再赋值
        x=2
        y=y+x
        z=z*k
        print*,k,x,y,z
        ! 循环体结束
        !    1           2           9           2
        !    4           2          11           8
        !    7           2          13          56
    end do


    

end program forWhile
