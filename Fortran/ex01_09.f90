! .and.	称为逻辑AND运算符。 如果两个操作数均非零，则条件为 true。	(A .and. B) 为 false。
! .or.	称为逻辑或运算符。 如果两个操作数中有任何一个非零，则条件为 true。	(A .or. B) 为 true。
! .not.	称为逻辑非运算符。 用于反转其操作数的逻辑状态。 如果条件为 true，则逻辑 NOT 运算符将为 false。	!(A .and. B) 为 true。
! .eqv.	称为逻辑 EQUIVALENT 运算符。 用于检查两个逻辑值是否相等。	(A .eqv. B) 为 false。
! .neqv.	称为逻辑非等效运算符。 用于检查两个逻辑值不相等。	(A .neqv. B) 为 true。

program logicalOp
    ! 该程序检查逻辑运算符
    implicit none
    
       ! 变量声明
       logical :: a, b
       
       ! 赋值
       a = .true.
       b = .false.
       
       if (a .and. b) then
          print *, "Line 1 - Condition is true"
       else
          print *, "Line 1 - Condition is false"  !
       end if
       
       if (a .or. b) then
          print *, "Line 2 - Condition is true"  !
       else
          print *, "Line 2 - Condition is false"
       end if
       
       ! 改变值
       a = .false.
       b = .true.
       
       if (.not.(a .and. b)) then
          print *, "Line 3 - Condition is true"  !
       else
          print *, "Line 3 - Condition is false"
       end if
       
       if (b .neqv. a) then
          print *, "Line 4 - Condition is true"  !
       else
          print *, "Line 4 - Condition is false"
       end if
       
       if (b .eqv. a) then
          print *, "Line 5 - Condition is true"
       else
          print *, "Line 5 - Condition is false"  !
       end if
       
       print *, '程序执行完毕，按任意键继续...'
       read(*,*)  ! 等待用户输入，任何输入都会结束程序
    end program logicalOp