program ex02_03 
    integer index,j
    do index = 50, 100
        j=judge(index)
        if (j==1) print*,index,"is single num"
        ! print*,index,j
    end do
end program ex02_03

integer(kind=4) function judge(arg) result(retval)
    implicit none
    integer, intent(in) :: arg
    integer index
    do index = 2, arg-1! Ï¸½Ú£¡£¡£¡
        if (mod(arg,index)==0)then
            retval=0
            exit
        else if (index==arg-1)then
            retval=1
        end if
    end do
    
end function judge