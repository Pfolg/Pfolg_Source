program boolCalculate
    ! .NE.��������
    ! .EQ.�����ڣ�Equal��
    ! .LT.��С�ڣ�Less Than��
    ! .LE.��С�ڵ��ڣ�Less Than or Equal��
    ! .GT.�����ڣ�Greater Than��
    ! .GE.�����ڵ��ڣ�Greater Than or Equal��
    implicit none
    real A,B,C,D
    logical :: flag1, flag2,f1,f2,f3,f4,f5,f6
    flag1 = .TRUE.  ! L
    flag2 = .FALSE.  ! M
    A=2.5
    B=7.5
    C=5.0
    D=6.0

    f1=(A+B).LT.(C+D).AND.A.EQ.3.5  ! F
    f2=A+B/2.0.NE.C-D.OR.C.NE.D  ! T
    f3=.NOT.flag1.OR.C.EQ.D.AND.flag2  ! T �ģ�and>or
    f4=C/2.0+D.LT.A.AND..NOT..TRUE..OR.C.EQ.D  ! F
    f5=(C.GT.D).OR..NOT.(A+B.LT.D)  ! T
    print *,C.GT.D
    f6=(A.LT.B).AND.(B.LT.A)  ! F

    ! f1-6���ע�������Լ���Ľ��

    print*,"1",f1,"2",f2,"3",f3,"4",f4,"5",f5,"6",f6
    

end program boolCalculate