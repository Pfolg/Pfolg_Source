program ex02_05
    ! implicit none
    integer,dimension(4,4)::A
    do I = 1, 4
        do J = 1, 4
            A(I,J)=I+J
            
        end do
        
    end do
    print*,FSUB(A(3,1))
    
end program ex02_05
function FSUB(X)
    integer, dimension(2,6)::X
    S=0
    do I = 1, 2
        do J = 1, 6
            if(mod(I+J,3)==0)then
                S=S+X(I,J)
            end if
            
        end do
        
    end do
    FSUB=S

    
end function FSUB