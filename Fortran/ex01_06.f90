!>>>>>>>> Fortran - 变量
! 1	
! Integer

! 它只能保存整数值。

! 2	
! Real

! 它存储浮点数。

! 3	
! Complex

! 它用于存储复数。

! 4	
! Logical

! 它存储逻辑布尔值。

! 5	
! Character

! 它存储字符或字符串。

! type-specifier :: variable_name

program variableTesting
    implicit none
    
       !声明变量
       integer :: total      
       real :: average 
       complex :: cx  
       logical :: done 
       character(len=80) :: message ! a string of 80 characters
       
       !赋值
       total = 20000  
       average = 1666.67   
       done = .true.   
       message = "A big Hello from Tutorials Point" 
       cx = (3.0, 5.0) ! cx = 3.0 + 5.0i
    
       Print *, total
       Print *, average
       Print *, cx
       Print *, done
       Print *, message
       
    end program variableTesting