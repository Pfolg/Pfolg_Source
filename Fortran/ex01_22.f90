program sushu
    implicit none
    integer a,b
    do a=101,1001,2
        do b=2,a-1,1
            if (mod(a,b)==0)then
                exit  ! �����������˳�
            else if (b==a-1) then
                print*,a,"������" 
            end if
        end do
    end do
end program sushu