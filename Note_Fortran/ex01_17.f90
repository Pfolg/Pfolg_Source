program calculateXN
    implicit none
    
    real x,y,j
    integer n,i,m
    m=0

    y=1
    j=1
    print*," ‰»Îx,n"
    read (*,*)x,n
    do i=1,n,1
        j=j*i
        y=x**i/j+y
    end do
    print*,y

    ! do while —≠ª∑
    do while(m<11)
        m=m+1
        print*,m
        ! if () print*,"do something"
    end do
    


end program calculateXN


