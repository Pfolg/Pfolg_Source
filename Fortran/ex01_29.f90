program ex01_29
    ! ��ͷ�о�һ��where
    implicit none
    character(len=10) judge(5)
    real grades(5)
    integer i
    print*,"������5���ɼ���"
    read *,grades
    where (grades<60)
        judge="������"
    elsewhere (grades<85)
        judge="�ϸ�"
    elsewhere (grades>=85)
        judge="����"
    end where
    do i=1,size(grades)
        print*,grades(i),judge(i)
    end do
end program ex01_29