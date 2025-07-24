program sushu
    implicit none
    integer a,b
    do a=101,1001,2
        do b=2,a-1,1
            if (mod(a,b)==0)then
                exit  ! 满足条件即退出
            else if (b==a-1) then
                print*,a,"是素数" 
            end if
        end do
    end do
end program sushu