program testingInt
    implicit none
    
         integer :: largeval  ! kind=4
       
        
        !两字节整数
        integer(kind = 2) :: shortval
           
        !四字节整数
        integer(kind = 4) :: longval
           
        !八字节整数
        integer(kind = 8) :: verylongval
           
        !十六字节整数
        integer(kind = 16) :: veryverylongval
           
        !默认整数
                
        print *,"shortval:", huge(shortval)
        print *, "longval",huge(longval)
        print *, "verylongval:",huge(verylongval)
        print *, "veryverylongval:",huge(veryverylongval)
        print *, "largeval",huge(largeval)  ! 2147483647

           
    end program testingInt