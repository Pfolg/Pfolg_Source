program gradeJudgement
    implicit none

    ! 多分支，还可以内部嵌套
    ! 这里相当于java式

    real g
    print *,"input="
    read (*,*)g
    if (g<60) then
        print *,"不及格bujjige"
    else if (g<90) then
        print*,"通过tongguo"
    else
        print*,"优秀youxiu"
    end if
    end