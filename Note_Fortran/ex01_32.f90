program ex01_32
    implicit none
    ! integer::n=5
    real::x(5)=(/1,2,3,4,5/)
    integer i
    real A
    print*," ‰»ÎA:"
    read*,A
    do i=1,size(x)
        if (x(i)==A)then
            print*,x(i),i
            exit
        else if(.NOT. x(size(x))==A)then
            print*,"’“≤ªµΩ"
        end if
    end do
    
end program ex01_32