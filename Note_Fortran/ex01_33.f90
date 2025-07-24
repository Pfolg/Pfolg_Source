program ex01_33
    implicit none
    integer x(4,5)
    integer sum,avg,i,j
    data x/2,5,12,7,6,-1,0,6,4,3,4,-9,9,8,10,5,-13,7,2,3/
    sum=0
    do i=1,5
        do j=1,4
            sum=sum+x(i,j)
        end do
    end do
    avg=sum/size(x)
    do i=1,4
        do j=1,5
            if (x(i,j)<=avg) x(i,j)=0
        end do
    end do
    write(*,20)((x(i,j),i=1,4),j=1,5)
    20 format(1X,4I5)
    ! print*,x
    write(*,*)"sum=",sum,",average=",avg

end program ex01_33