program ex01_30
    implicit none
    integer,dimension(3,3)::w
    integer i,j
    read(*,*)w
    write(*,20)((w(i,j),j=1,3),i=1,3)
    20 format(1X,3I3)
    ! 1,4,7,2,5,8,3,6,9
    ! 1  2  3
    ! 4  5  6
    ! 7  8  9
    write(*,*)((w(i,j),j=1,3),i=1,3)
    ! 1           2           3           4           5           6           7           8           9
end program ex01_30
