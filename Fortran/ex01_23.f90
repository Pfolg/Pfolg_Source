program ball
    implicit none
    real g,s,h
    integer n
    PARAMETER(g=9.8)
    s=0
    n=0
    h=100
    do while(n<10)
        print*,n
        n=n+1
        s=s+h
        h=h/2
        s=s+h

    end do
    print*,n,s,h




end program ball