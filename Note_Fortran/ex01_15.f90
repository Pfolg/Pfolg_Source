program fortran
    implicit none

    logical f1,f2
    f1=.TRUE.
    f2=.false.


    ! if嵌套
    if (.FALSE.) then        
        if (.TRUE.) then            
            if (.false.) then
            else
                 print*,"c"
            end if
        else
            print*,"b"
        end if  
    else
        print*,"a"  ! 拿到下面的else中
    end if
    
    end