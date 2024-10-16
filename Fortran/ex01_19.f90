program calculateY
    implicit none
    real y
    integer n
    y=1
    n=1
    do while(y<2)
        y=y+1/(2*n-1)
        n=n+1

    end do
    print*,y,n

    ! ÎÞÏÞÑ­»·
    ! y=1
    ! n=1
    ! do while(.true.)
    !     y=y+1
    !     print*,y
    ! end do



end program calculateY