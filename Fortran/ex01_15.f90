program fortran
    implicit none

    logical f1,f2
    f1=.TRUE.
    f2=.false.


    ! ifǶ��
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
        print*,"a"  ! �õ������else��
    end if
    
    end