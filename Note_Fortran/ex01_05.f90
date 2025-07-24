program division   
    implicit none  
    
       ! 定义实数变量   
       real :: p, q, realRes 
       
       ! 定义整型变量
       integer :: i, j, intRes  
       character (len = 40) :: name


       print *,huge(p),huge(i)
       
       ! 赋值
       p = 2.0 
       q = 3.0    
       i = 2 
       j = 3  
       
       ! 浮点除法
       realRes = p/q  
       intRes = i/j
       
       print *, realRes
       print *, intRes

        name = "Pfolg"

        print *,name
       
    end program division  