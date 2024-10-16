program ex01_29
    ! 回头研究一下where
    implicit none
    character(len=10) judge(5)
    real grades(5)
    integer i
    print*,"请输入5个成绩："
    read *,grades
    where (grades<60)
        judge="不及格"
    elsewhere (grades<85)
        judge="合格"
    elsewhere (grades>=85)
        judge="优秀"
    end where
    do i=1,size(grades)
        print*,grades(i),judge(i)
    end do
end program ex01_29